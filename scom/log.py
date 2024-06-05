import json
import re

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
class Log:
    def __init__(self, span_id, reference_tags, tags):
        self.span_id = span_id
        self.reference_tags = reference_tags
        self.tags = tags

    def __repr__(self):
        return f"Log(span_id={self.span_id}, reference_tags={self.reference_tags}, tags={self.tags})"

    def to_json(self):
        return json.dumps({
            'spanId': self.span_id,
            'reference_tags': self.reference_tags,
            'tags': self.tags
        }, indent=2)
    
    def get_endpoint_name(self):
        result = None

        for tag in self.reference_tags:
            if tag["key"] == "http.target":     
                result = tag["value"]
                break
        
        return result
    
    def get_db_statement(self):
        result = []
        for s in self.tags:
            if s["key"] == "db.statement":
                result.append(s["value"])

        if len(result) > 0:
            return result
        
        return None
    
    def get_table_names(self):
        statement = self.get_db_statement()
        
        if statement is not None:
            return extract_table_names(statement[0])
        
        return None