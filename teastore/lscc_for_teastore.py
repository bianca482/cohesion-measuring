from cohesion_calculator import cohesion
from cohesion_calculator import log
import json

files = ["auth_090624.json", "image_090624.json", "persistence_090624.json", "recommender_090624.json", "registry_090624.json", "webui_090624.json"]
service_names = ["tools.descartes.teastore.auth", "tools.descartes.teastore.image", "tools.descartes.teastore.persistence", "tools.descartes.teastore.recommender", "tools.descartes.teastore.registry", "tools.descartes.teastore.webui"]

for i, f in enumerate(files): 
    file = open(f"./test_data/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_lscc(data, service_names[i])
    grouped_logs = log.get_grouped_logs_from_file(data, service_names[i])
    calls_per_table = log.get_number_of_calls_from_file(data, service_names[i])
    endpoint_calls = log.get_number_of_endpoint_calls_from_file(data, service_names[i])

    print(f"LSCC Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped logs for {f}: {grouped_logs}")
    print(f"Number of calls per table: {calls_per_table}")
    print(f"Number of endpoint calls: {endpoint_calls}")
