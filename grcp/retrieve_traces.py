import grpc
import query_pb2_grpc, query_pb2
from google.protobuf.timestamp_pb2 import Timestamp
import time
import os
import json
from google.protobuf.json_format import MessageToDict


def get_traces_for_service(service_name):
    # Connect to the Jaeger gRPC server
    channel = grpc.insecure_channel('localhost:16685')  # Replace with your Jaeger gRPC endpoint
    client = query_pb2_grpc.QueryServiceStub(channel)

    # Create a request
    #end_time = int(time.time() * 1e6)  # Current time in microseconds
    #start_time = end_time - (60 * 60 * 1e6)  # 1 hour ago in microseconds

    request = query_pb2.FindTracesRequest(
        query=query_pb2.TraceQueryParameters(
            service_name=service_name,
           # start_time_min=Timestamp(seconds=int(start_time // 1e6), nanos=int((start_time % 1e6) * 1e3)),
           # start_time_max=Timestamp(seconds=int(end_time // 1e6), nanos=int((end_time % 1e6) * 1e3))
        )
    )

    # Get the traces
    response = client.FindTraces(request)

    # Convert the response to json
    traces_json = [MessageToDict(trace) for trace in response]

    return traces_json

# Write traces locally to files
def write_traces(directory, traces):
    for i, trace in enumerate(traces):
        for j, span in enumerate(trace["spans"]):
           # traceid = span["traceId"]
            path = os.path.join(directory, f"trace{i}_span{j}.json")
            with open(path, 'w') as fd:
                json.dump(trace, fd, indent=3)

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

if __name__ == "__main__":
    """names = ["auth"]#, "image"], "persistence", "registry", "recommender", "webui"]

    for service in names:
        if not os.path.exists(service):
            os.makedirs(service)

        traces = get_traces_for_service(service)

       # for i, t in enumerate(traces):
       #     print(f"Trace {i}: {t} \n\n")
       #     if i == 2:
       #         break
        write_traces(service, traces)"""
combine_jsons("auth")
