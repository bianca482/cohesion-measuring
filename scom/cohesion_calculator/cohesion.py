from cohesion_calculator.log import Log

def group_logs(logs):
    grouped_logs= {}

    for log in logs:
        endpoint_name = log.get_endpoint_name()

        if endpoint_name == None:
            continue

        if endpoint_name not in grouped_logs:
            grouped_logs[endpoint_name] = []

        table_names = log.get_table_names()

        if table_names is not None:
            for name in table_names: 
                if name in grouped_logs[endpoint_name]:
                    continue
                else: 
                    grouped_logs[endpoint_name].append(name)

    return grouped_logs


def extract_logs(result):
    logs = []

    for data in result["data"]:
        for log in data["spans"]:
            span_id = log['spanID']
            tags = log['tags']
            for reference in log["references"]:
                if "span" in reference: 
                    span_obj = Log(span_id=span_id, reference_tags=reference["span"]["tags"], tags=tags)
                    logs.append(span_obj)
          
    return logs


def calculate_connection_intensity(api1, api2):
     common_tables = set(api1).intersection(api2)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(api1)), len(set(api2))))


def scom(apis):
    n_of_apis = len(apis)
    if n_of_apis <= 1: return "Too few endpoints"

    total_weighted_connections = 0

    processed_pairs = set()  # Verarbeitete Paare speichern

    for i, api1 in enumerate(apis):
        for api2 in list(apis.keys())[i + 1:]:
            pair_key = tuple(sorted((api1, api2)))
            
            if pair_key in processed_pairs:
                continue  # Überspringen, wenn Paar schon verarbeitet wurde
            
            connection_intensity = calculate_connection_intensity(apis[api1], apis[api2])
            # Weglassen, da Tabellen, die nur sehr selten aufgerufen werden, nicht berücksichtigt werden sollen
            #n_involved_tables = len(set(apis[api1]).union(set(apis[api2])))
            #weight = n_involved_tables / number_of_tables
            #weighted_connection = connection_intensity * weight
            #weighted_connection = connection_intensity * n_involved_tables
            #total_weighted_connections += weighted_connection
            total_weighted_connections += connection_intensity
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)

def calculate_scom(jsonfile):
    logs = extract_logs(jsonfile)
    grouped_logs = group_logs(logs)
    print(grouped_logs)
    return scom(grouped_logs)




