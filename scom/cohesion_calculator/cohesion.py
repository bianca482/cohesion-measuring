from cohesion_calculator.log import Log, group_logs, extract_logs
from collections import Counter

def filter_empty_apis(apis):
    return {k: v for k, v in apis.items() if v}

def calculate_connection_intensity(api1, api2):
     common_tables = set(api1).intersection(api2)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(api1)), len(set(api2))))

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

            tables_api1 = Counter(apis[api1]).keys()
            tables_api2 = Counter(apis[api2]).keys()

            connection_intensity = calculate_connection_intensity(tables_api1, tables_api2)
            total_weighted_connections += connection_intensity
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)

def calculate_scom(jsonfile):
    logs = extract_logs(jsonfile)
    grouped_logs = group_logs(logs)
    return scom(grouped_logs)





