from cohesion_calculator import cohesion
from cohesion_calculator import log
import json

files = ["auth_050624.json", "image_050624.json", "persistence_050624.json", "recommender_050624.json", "registry_050624.json", "webui_050624.json"]

for f in files: 
    file = open(f"../test_data/teastore/{f}")
    data = json.load(file)
    file.close()

    c = cohesion.calculate_scom(data)
    grouped_logs = log.retrieve_grouped_logs_from_file(data)

    print(f"Cohesion for {f}: {c}")
    print(f"Grouped logs for {f}: {grouped_logs}")
