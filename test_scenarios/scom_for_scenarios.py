from cohesion_calculator import cohesion
from cohesion_calculator import span
import json

files = ["scenario1.json", "scenario2.json", "scenario3.json"]
service_names = ["scenario1", "scenario2", "scenario3"]

for i, f in enumerate(files): 
    file = open(f"./test_data/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_scom(data, service_names[i], True, "json")
    grouped_spans = span.get_grouped_spans_from_file(data, service_names[i], "json")
    calls = span.get_number_of_endpoint_calls_from_file(data, service_names[i], "json")

    print(f"Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped spans for {f}: {grouped_spans}")
    print(f"Number of calls for {f}: {calls}")
