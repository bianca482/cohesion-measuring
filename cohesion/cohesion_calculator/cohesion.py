from cohesion_calculator import log

def filter_empty_apis(apis):
    return {k: v for k, v in apis.items() if v}

def calculate_connection_intensity(i, j):
     common_tables = set(i).intersection(j)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(i)), len(set(j))))

def calculate_weighted_connection_intensity(tables1, tables2, weight1, weight2):
    connection_intensity = calculate_connection_intensity(tables1, tables2)
    return connection_intensity * weight1 * weight2

def scom(grouped_logs, endpoint_calls, weight_n_calls = True):
    apis = filter_empty_apis(grouped_logs)

    n_of_apis = len(apis)
    if n_of_apis <= 1:
        return "Undefined (There are too few endpoints to calculate SCOM)"

    total_calls = sum(endpoint_calls.values())
    total_weighted_connections = 0 

    processed_pairs = set() # Verarbeitete Paare speichern

    for i, api1 in enumerate(apis):
        for api2 in list(apis.keys())[i + 1:]:
            pair_key = tuple(sorted((api1, api2)))
            
            if pair_key in processed_pairs:
                continue  # Überspringen, wenn Paar schon verarbeitet wurde
                              
            tables1 = set(apis[api1])
            tables2 = set(apis[api2])            

            weight = 1

            if weight_n_calls and tables1 != tables2:
                n_involved_calls = endpoint_calls[api1] + endpoint_calls[api2]
                weight = n_involved_calls / total_calls

            connection_intensity = calculate_connection_intensity(tables1, tables2)
            total_weighted_connections += connection_intensity * weight
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)


def calculate_scom(jsonfile, service_name, weight_n_calls = True):
    logs = log.extract_logs(jsonfile, service_name)
    grouped_logs = log.group_logs(logs)
    endpoint_calls = log.get_number_of_endpoint_calls(logs)

    return scom(grouped_logs, endpoint_calls, weight_n_calls)

def lscc(grouped_logs):  
    apis = filter_empty_apis(grouped_logs)
    n_of_apis = len(apis)

    all_tables = []

    for url, tables in grouped_logs.items(): 
        all_tables += tables
    
    n_tables = len(set(all_tables))

    if n_tables == 0 and n_of_apis > 1: return 0
    if n_tables > 0 and n_of_apis == 0: return 1
    if n_of_apis == 1: return 1
    if n_tables == 0 and n_of_apis == 0: return "Undefined (There are no tables and no endpoints)"

    result = 0

    for t in set(all_tables): 
        apis_with_table = 0
        for g in grouped_logs.values():
            if t in g:
                apis_with_table += 1

        result += apis_with_table * (apis_with_table - 1)

    return result / (n_tables*n_of_apis * (n_of_apis-1))

def calculate_lscc(jsonfile, service_name):
    logs = log.extract_logs(jsonfile, service_name)
    grouped_logs = log.group_logs(logs)
    
    return lscc(grouped_logs)

