import json
import re

table_name_pattern = re.compile(
    r"""
    (?i)   # Case-insensitive matching
    \bFROM\s+([`'"]?[a-zA-Z_][\w$]*[`'"]?)|   
    \bJOIN\s+([`'"]?[a-zA-Z_][\w$]*[`'"]?)|   
    \bINTO\s+([`'"]?[a-zA-Z_][\w$]*[`'"]?)|  
    \bUPDATE\s+([`'"]?[a-zA-Z_][\w$]*[`'"]?)| 
    \bDELETE\s+FROM\s+([`'"]?[a-zA-Z_][\w$]*[`'"]?)  
    """,
    re.VERBOSE
)

def extract_table_names(sql):
    matches = table_name_pattern.findall(sql)
    #matches = [
    #('employees', '', '', '', '', '', ''),
    #('', 'customers', '', '', '', '', '')]
    # filters out empty matches ('') and flattens result to normal list
    return [match for sublist in matches for match in sublist if match]

def is_number(value):
   try:
        float(value)
        return True
   except ValueError:
        return False

class Log:
    def __init__(self, span_id, trace_id, parent_id, db_statements, http_target):
        self.span_id = span_id
        self.trace_id = trace_id
        self.parent_id = parent_id
        self.db_statements = db_statements
        self.http_target = http_target
        self.parent_endpoint = None

    def __repr__(self):
        return f"Log(span_id={self.span_id}, trace_id={self.trace_id}, parent_id={self.parent_id}, db_statements={self.db_statements}, http_target={self.http_target})"

    def to_json(self):
        return json.dumps({
            'spanId': self.span_id,
            'traceId': self.trace_id,
            'parentId': self.parent_id,
            'db_statements': self.db_statements,
            'http_target': self.http_target
        }, indent=2)
    
    def get_endpoint_name(self):
        endpoint_name = self.http_target

        if endpoint_name != None:
            endpoint =  endpoint_name.split('?')[0]
            endpoint_parts = endpoint.split('/')

            # if the last part is a number (e.g. /customers/count/9), it should get cut - else (e.g. /customers) 
            if is_number(endpoint_parts[-1]):
                endpoint_name = '/'.join(endpoint_parts[:-1]) + '/'
            else: 
                endpoint_name = '/'.join(endpoint_parts) + '/'

            # removes duplicate / and ensures there is exactly one / at the end
            endpoint_name = '/'.join(part for part in endpoint_name.split('/') if part) + '/'
    
        return endpoint_name

    def get_db_statement(self):
        db_statements = self.db_statements

        if len(db_statements) > 0:
            return db_statements
        
        return None

    def get_table_names(self):
        statement = self.get_db_statement()
        
        if statement is not None:
            return extract_table_names(statement[0])
        
        return None

def set_parent_endpoints(logs, service_name):
    # Create a dictionary to store parents
    parents = {}

    # get service parent for each trace id
    for log in logs: 
        endpoint_name = log.get_endpoint_name()
        if endpoint_name != None and service_name in endpoint_name:
            if log.trace_id not in parents.keys():
                parents[log.trace_id] = endpoint_name

    for log in logs:
        endpoint_name = log.get_endpoint_name()
        if endpoint_name != None:
            parent = parents.get(log.trace_id)
            if parent:
                log.parent_endpoint = parent
                
    return logs

def group_logs(logs):
    grouped_logs = {}

    for log in logs: 
        table_names = log.get_table_names()
        if table_names != None and log.parent_endpoint != None:
            endpoint_name = log.parent_endpoint

            if endpoint_name not in grouped_logs:
                grouped_logs[endpoint_name] = []

            for name in table_names:
                if name in grouped_logs[endpoint_name]:
                    continue
                else:
                    grouped_logs[endpoint_name].append(name)


    return grouped_logs


def extract_logs(result, service_name):
    logs = []
 
    for data in result["data"]:
        for log in data["spans"]:
            parent_id = None
            db_statements = []
            http_target = None

            for tag in log["tags"]:
                if "key" in tag:
                    if tag["key"] == "db.statement":
                        db_statements.append(tag["value"])

                    if tag["key"] == "http.target":
                        http_target = tag["value"]
            
            for reference in log["references"]:
                if "span" in reference: 
                    for tag in reference["span"]["tags"]:
                        if tag["key"] == "db.statement":
                            db_statements.append(tag["value"])

                        if tag["key"] == "http.target":
                            http_target = tag["value"]

            if "references" in log: 
                for r in log["references"]:
                    parent_id = r["spanID"]
            
            span_obj = Log(
                span_id=log['spanID'], 
                trace_id=log["traceID"], 
                parent_id = parent_id,
                db_statements = db_statements,
                http_target = http_target
            )

            logs.append(span_obj)

    for log in logs: 
        if log.http_target == None:
            logs.remove(log)

    logs = set_parent_endpoints(logs, service_name)

    return logs

def retrieve_grouped_logs_from_file(jsonfile, service_name):
    logs = extract_logs(jsonfile, service_name)
    return group_logs(logs)