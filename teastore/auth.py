from cohesion_calculator import cohesion
import json

file = open("../test_data/teastore/auth_020624.json")
result = json.load(file)
file.close()

cohesion = cohesion.calculate_scom(result)

print(cohesion)
