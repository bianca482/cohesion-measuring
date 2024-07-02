from cohesion_calculator import cohesion
from cohesion_calculator import trace
import json

files = ["auth.json", "image.json", "persistence.json", "recommender.json", "registry.json", "webui.json"]
service_names = ["tools.descartes.teastore.auth", "tools.descartes.teastore.image", "tools.descartes.teastore.persistence", "tools.descartes.teastore.recommender", "tools.descartes.teastore.registry", "tools.descartes.teastore.webui"]
path = "../grpc/"

for i, f in enumerate(files): 
    file = open(f"{path}/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_scom(data, service_names[i], True)
    grouped_traces = trace.get_grouped_traces_from_file(data, service_names[i])
    #calls_per_table = trace.get_number_of_calls_per_table_from_file(data, service_names[i])
    endpoint_calls = trace.get_number_of_endpoint_calls_from_file(data, service_names[i])

    print(f"Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped traces for {f}: {grouped_traces}")
    #print(f"Number of calls per table: {calls_per_table}")
    print(f"Number of endpoint calls: {endpoint_calls}")
