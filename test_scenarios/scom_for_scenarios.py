from cohesion_calculator import cohesion
from cohesion_calculator import trace
import json

files = ["scenario1.json", "scenario2.json", "scenario3.json"]
service_names = ["scenario1", "scenario2", "scenario3"]

for i, f in enumerate(files): 
    file = open(f"./test_data/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_scom(data, service_names[i], True)
    grouped_traces = trace.get_grouped_traces_from_file(data, service_names[i])
    calls = trace.get_number_of_endpoint_calls_from_file(data, service_names[i])

    print(f"Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped traces for {f}: {grouped_traces}")
    print(f"Number of calls for {f}: {calls}")
