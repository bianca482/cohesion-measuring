import os
import json
import requests

# Returns list of all traces for a service
def get_traces(service):
    url = "http://localhost:16686/api/traces?service=" + service

    try:
        response = requests.get(url)
    except Exception as e:
        print(e)

    response = response.json()
    traces = response["data"]
    return traces

# Write traces locally to files
def write_traces(directory, traces):

    for i, trace in enumerate(traces):
        path = os.path.join(directory, f"{i}.json")

        with open(path, 'w') as fd:
            json.dump(trace, fd, indent=3)

# Combine all JSON files in a directory into a single JSON file
def combine_jsons(name):
    directory = f"./{name}/"
    combined_traces = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            path = os.path.join(directory, filename)

            with open(path, 'r') as file:
                try:
                    trace = json.load(file)
                    combined_traces.append(trace)
                except json.JSONDecodeError as e:
                    print(f"Error decoding {filename}: {e}")

    combined_data = {"data": combined_traces}
    save_file_path = f"{name}.json"

    with open(save_file_path, "w") as save_file:
        json.dump(combined_data, save_file, indent=3)

service_names = ["auth", "image", "persistence", "registry", "recommender", "webui"]

for service_name in service_names:
    if not os.path.exists(f"traces/{service_name}"):
        os.makedirs(f"traces/{service_name}")

    traces = get_traces(service_name)
    write_traces(service_name, traces)
    combine_jsons(service_name)