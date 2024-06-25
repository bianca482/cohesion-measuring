from cohesion_calculator.log import group_logs, extract_logs, get_number_of_endpoint_calls, set_parent_endpoints, get_number_of_calls_per_table

def filter_empty_apis(apis):
    return {k: v for k, v in apis.items() if v}

def calculate_connection_intensity(i, j):
     common_tables = set(i).intersection(j)
     if len(common_tables) == 0: return 0

     return len(common_tables) / (min(len(set(i)), len(set(j))))

def normalize_calls(endpoint_calls):
    total_calls = sum(endpoint_calls.values())
    return {endpoint: count / total_calls for endpoint, count in endpoint_calls.items()}

def calculate_weighted_connection_intensity(tables1, tables2, weight1, weight2):
    connection_intensity = calculate_connection_intensity(tables1, tables2)
    return connection_intensity * weight1 * weight2

def scom(grouped_logs, endpoint_calls, weight_n_calls = True):
    apis = filter_empty_apis(grouped_logs)

    n_of_apis = len(apis)
    if n_of_apis <= 1:
        return "Undefined (There are too few endpoints to calculate SCOM)"

    total_calls = sum(endpoint_calls.values())

    #total_calls_per_endpoint = {endpoint: sum(calls.values()) for endpoint, calls in endpoint_calls.items()}
    #total_calls = sum(total_calls_per_endpoint.values())

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
                #print(f"{api1} und {api2}")
                #n_involved_calls = total_calls_per_endpoint[api1] + total_calls_per_endpoint[api2]
                n_involved_calls = endpoint_calls[api1] + endpoint_calls[api2]
                #print(n_involved_calls)
                #print(total_calls)
                weight = n_involved_calls / total_calls
                #print(weight)

            connection_intensity = calculate_connection_intensity(tables1, tables2)
            total_weighted_connections += connection_intensity * weight
            processed_pairs.add(pair_key)  # Paar als verarbeitet markieren

    return total_weighted_connections / (n_of_apis*(n_of_apis-1) / 2)


def calculate_scom(jsonfile, service_name, weight_n_calls = True):
    logs = extract_logs(jsonfile, service_name)
    grouped_logs = group_logs(logs)
    endpoint_calls = get_number_of_endpoint_calls(logs)
    #endpoint_calls = get_number_of_calls_per_table(logs)
    return scom(grouped_logs, endpoint_calls, weight_n_calls)

import json

# l = Anzahl an Attributen (Datenbanktabellen)
# k = Anzahl an Methoden (APIs)
# xi = Anzahl an Methoden (APIs), welche Attribut (Datenbanktabelle) i referenzieren


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
    logs = extract_logs(jsonfile, service_name)
    grouped_logs = group_logs(logs)
    return lscc(grouped_logs)

"""def main():
    name = "tools.descartes.teastore.persistence"
    file = open(f"../../teastore/test_data/persistence_090624.json")
    data = json.load(file)
    file.close()

    logs = extract_logs(data, name)
    grouped_logs = group_logs(logs)
    print(lscc(grouped_logs))

    #print(calculate_scom(data, name))
    #set_parent_endpoints(logs, name)
    #new_logs = { 'tools.descartes.teastore.auth/rest/useractions/login/': ['PERSISTENCEUSER'], 
    #        'tools.descartes.teastore.persistence/rest/users/name/': ['PERSISTENCEUSER'],
    #        'tools.descartes.teastore.webui/loginAction/': ['PERSISTENCEUSER']}

    #new_calls = {'tools.descartes.teastore.auth/rest/useractions/login/': 486, 
    #         'tools.descartes.teastore.persistence/rest/users/name/': 576,
    #         'tools.descartes.teastore.webui/loginAction/': 516
    #         }

    #print(f"New service without weights: {scom(new_logs, new_calls, False)}")
    #print(f"New service with weights: {scom(new_logs, new_calls, True)}")

if __name__ == '__main__':
    main()
"""


