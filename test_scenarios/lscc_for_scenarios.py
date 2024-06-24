from cohesion_calculator import cohesion
from cohesion_calculator import log
import json

files = ["scenario1.json", "scenario2.json", "scenario3.json"]
service_names = ["scenario1", "scenario2", "scenario3"]

for i, f in enumerate(files): 
    file = open(f"./test_data/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_lscc(data, service_names[i])
    grouped_logs = log.get_grouped_logs_from_file(data, service_names[i])
    calls = log.get_number_of_calls_from_file(data, service_names[i])

    print(f"LSCC Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped logs for {f}: {grouped_logs}")
    print(f"Number of calls for {f}: {calls}")
