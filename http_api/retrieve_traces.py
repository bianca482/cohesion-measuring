import os
import json
import requests

# Returns list of all traces for a service
def get_traces_for_service(service):
    url = "http://localhost:16686/api/traces?service=" + service

    try:
        response = requests.get(url)
    except Exception as e:
        print(e)

    response = response.json()
    traces = response["data"]
    return traces

# Write traces locally to files
def write_traces(service_name, traces):
    for i, trace in enumerate(traces):
        file_path = os.path.join(service_name, f"trace{i}.json")
        with open(file_path, 'w') as file:
            json.dump(trace, file, indent=3)

# Combine all JSON files in a directory into a single JSON file
def combine_jsons(service_name):
    combined_traces = []

    for filename in os.listdir(service_name):
        if filename.endswith('.json'):
            path = os.path.join(service_name, filename)

            with open(path, 'r') as file:
                try:
                    trace = json.load(file)
                    combined_traces.append(trace)
                except json.JSONDecodeError as e:
                    print(f"Error decoding {filename}: {e}")

    combined_data = {"data": combined_traces}
    save_file_path = f"{service_name}.json"

    with open(save_file_path, "w") as save_file:
        json.dump(combined_data, save_file, indent=3)

if __name__ == "__main__":
    service_names = ["auth", "image", "persistence", "registry", "recommender", "webui"]

    for service_name in service_names:
        if not os.path.exists(service_name):
            os.makedirs(service_name)

        traces = get_traces_for_service(service_name)
        write_traces(service_name, traces)
        combine_jsons(service_name)
