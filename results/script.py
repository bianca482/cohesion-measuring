#!/usr/bin/env python

# https://github.com/Ashmita152/jaeger-datasets/blob/master/bookinfo/extract.py

import os
import json
import requests

# Returns list of all traces for a service
def get_traces(service):
    url = "http://localhost:16686/api/traces?limit=5000&service=" + service

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise err

    response = response.json()
    traces = response["data"]
    return traces

# Write traces locally to files
def write_traces(directory, traces):
    for trace in traces:
        traceid = trace["traceID"]
        path = os.path.join(directory, f"{traceid}.json")
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

names = ["auth", "image"]#, "persistence", "registry", "recommender", "webui"]

for service in names:
    if not os.path.exists(service):
        os.makedirs(service)

    traces = get_traces(service)
    write_traces(service, traces)
    combine_jsons(service)
