from scom.log import Log

def group_logs(logs):
    grouped_logs= {}

    for log in logs:
        operation_name = log.get_operation_name()

        if operation_name == None:
            continue

        if operation_name not in grouped_logs:
            grouped_logs[operation_name] = []

        table_names = log.get_table_names()

        for name in table_names: 
            if name in grouped_logs[operation_name]:
                continue
            else: 
                grouped_logs[operation_name].append(name)

    return grouped_logs


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


def calculate_connection_intensity(api1, api2):
     common_tables = set(api1).intersection(api2)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(api1)), len(set(api2))))


def scom(grouped_logs, number_of_tables):
    n_of_apis = len(grouped_logs)
    if n_of_apis <= 1: return "Too few endpoints"

    total_weighted_connections = 0

    processed_pairs = set()  # Verarbeitete Paare speichern

    for i, api1 in enumerate(grouped_logs):
        for api2 in list(grouped_logs.keys())[i + 1:]:
            pair_key = tuple(sorted((api1, api2)))
            
            if pair_key in processed_pairs:
                continue  # Überspringen, wenn Paar schon verarbeitet wurde
            
            connection_intensity = calculate_connection_intensity(grouped_logs[api1], grouped_logs[api2])
            n_involved_tables = len(set(grouped_logs[api1]).union(set(grouped_logs[api2])))
            weight = n_involved_tables / number_of_tables
            weighted_connection = connection_intensity * weight
            total_weighted_connections += weighted_connection
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)

def calculate_scom(jsonfile, n_tables):
    logs = extract_logs(jsonfile)
    grouped_logs = group_logs(logs)
    return scom(grouped_logs, n_tables)




