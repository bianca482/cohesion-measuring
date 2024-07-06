import grpc
import query_pb2_grpc, query_pb2
import os
import json
from google.protobuf.json_format import MessageToDict

# Get traces from Jaeger gRPC server
def get_traces_for_service(service_name, channel):
    client = query_pb2_grpc.QueryServiceStub(channel)

    request = query_pb2.FindTracesRequest(
        query=query_pb2.TraceQueryParameters(
            service_name=service_name,
        )
    )

    response = client.FindTraces(request)
    traces_json = [MessageToDict(trace) for trace in response]

    return traces_json

# Write traces locally to files
def write_traces(service_name, traces):
    for i, trace in enumerate(traces):
        file_path = os.path.join(service_name, f"trace{i}.json")
        with open(file_path, 'w') as file:
            json.dump(trace, file, indent=3)

# Combine all traces to a single json file
def combine_jsons(service_name):
    combined_traces = []

    for filename in os.listdir(service_name):
        if filename.endswith('.json'):
            file_path = os.path.join(service_name, filename)

            with open(file_path, 'r') as file:
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
    service_names = ["auth", "image", "persistence", "registry", "recommender", "webui"] # adjust if neccessary
    channel = grpc.insecure_channel('localhost:16685') # adjust if neccessary

    for service_name in service_names:
        if not os.path.exists(service_name):
            os.makedirs(service_name)

        traces = get_traces_for_service(service_name, channel)
        write_traces(service_name, traces)
    
    for service_name in service_names:
        combine_jsons(service_name)
