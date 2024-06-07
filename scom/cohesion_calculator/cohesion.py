from cohesion_calculator.log import group_logs, extract_logs

def filter_empty_apis(apis):
    return {k: v for k, v in apis.items() if v}

def calculate_connection_intensity(i, j):
     common_tables = set(i).intersection(j)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(i)), len(set(j))))

def scom(grouped_logs):
    apis = filter_empty_apis(grouped_logs)

    n_of_apis = len(apis)
    if n_of_apis <= 1:
        return "Too few endpoints"

    total_weighted_connections = 0 
    processed_pairs = set() # Verarbeitete Paare speichern

    for i, api1 in enumerate(apis):
        for api2 in list(apis.keys())[i + 1:]:
            pair_key = tuple(sorted((api1, api2)))
            
            if pair_key in processed_pairs:
                continue  # Überspringen, wenn Paar schon verarbeitet wurde
                              
            tables1 = set(apis[api1])
            tables2 = set(apis[api2])

            connection_intensity = calculate_connection_intensity(tables1, tables2)
            total_weighted_connections += connection_intensity
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)

def calculate_scom(jsonfile, service_name):
    logs = extract_logs(jsonfile, service_name)
    grouped_logs = group_logs(logs)
    return scom(grouped_logs)





