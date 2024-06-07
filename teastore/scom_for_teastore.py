from cohesion_calculator import cohesion
from cohesion_calculator import log
import json

files = ["auth_050624.json", "image_050624.json", "persistence_050624.json", "recommender_050624.json", "registry_050624.json", "webui_050624.json"]
service_names = ["auth", "image", "persistence", "recommender", "registry", "webui"]

for i, f in enumerate(files): 
    file = open(f"./test_data/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_scom(data, service_names[i])
    grouped_logs = log.retrieve_grouped_logs_from_file(data, service_names[i])

    print(f"Cohesion for Service {service_names[i]}: {c}")
    print(f"Grouped logs for {f}: {grouped_logs}")
