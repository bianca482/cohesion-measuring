from cohesion_calculator import cohesion
import json

files = ["auth_020624.json", "image_020624.json", "persistence_020624.json", "recommender_020624.json", "registry_020624.json", "webui_020624.json"]

for f in files: 
    file = open(f"../test_data/teastore/{f}")
    result = json.load(file)
    file.close()

    c = cohesion.calculate_scom(result)

    print(f"Cohesion for {f}: {c}")
