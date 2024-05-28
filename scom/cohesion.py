from scom.log import Log

def group_logs(logs):
    grouped_logs= {}

    for log in logs:
        operationName = log.get_operation_name()

        if operationName == None:
            continue

        if operationName not in grouped_logs:
            grouped_logs[operationName] = []

        table_name = log.get_table_names()

        if table_name in grouped_logs[operationName]: 
            continue
        
        for name in log.get_table_names():
            grouped_logs[operationName].append(name)


def extract_logs(jsonfile):
    logs = []
    for data in jsonfile["data"]:
        for log in data["spans"]:
            span_id = log['spanID']
            spans = []
            for r in log['references']: 
                spans.append(r["span"])

            tags = log['tags']
            span_obj = Log(span_id=span_id, spans=spans, tags=tags)
            logs.append(span_obj)

    return logs


def calculateConnectionIntensity(api1, api2):
     common_attributes = set(api1).intersection(api2)
     if len(common_attributes) == 0: return 0

     return len(common_attributes) / (min(len(set(api1)), len(set(api2))))


def scom(apis, number_of_tables):
    n_of_apis = len(apis)
    if n_of_apis <= 1: return "Too few endpoints"

    total_weighted_connections = 0

    processed_pairs = set()  # Verarbeitete Paare speichern

    for i, api1 in enumerate(apis):
        for api2 in list(apis.keys())[i + 1:]:
            pair_key = tuple(sorted((api1, api2)))
            
            if pair_key in processed_pairs:
                continue  # Überspringen, wenn Paar schon verarbeitet wurde
            
            connection_intensity = calculateConnectionIntensity(apis[api1], apis[api2])
            n_involved_tables = len(set(apis[api1]).union(set(apis[api2])))
            weight = n_involved_tables / number_of_tables
            weighted_connection = connection_intensity * weight
            total_weighted_connections += weighted_connection
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)

def calculate_scom(jsonfile, n_tables):
    logs = extract_logs(jsonfile)
    grouped_logs = group_logs(logs)
    return scom(grouped_logs, n_tables)




