# Usage of Jaeger gRPC/Protobuf endpoint

This project contains all information needed to retrieve traces from the Jaeger gRPC/Protobuf endpoint. Note that the entire procedure mentioned below is based on the usage of python.

## Setup

The client code has already been generated and is being provided in this repository. If you want to reproduce this, following steps are neccessary before you can get traces from this endpoint.

1.  Install neccessary dependencies:

    - `python -m pip install grpcio`
    - `python -m pip install grpcio-tools`

2.  Generate client code according to the proto definitions
    - `python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. protos/query.proto protos/model.proto`
    - `python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. protos/gogoproto/gogo.proto protos/google/api/annotations.proto protos/google/api/http.proto protos/google/protobuf/descriptor.proto protos/google/protobuf/timestamp.proto protos/google/protobuf/duration.proto`

## Get traces

The file `retrieve_traces.py` retrieves those traces in the Protobuf format and converts them to JSON format. All traces are then saved in a folder named the same as the service name for which the traces are retrieved. Make sure to adjust the service names and endpoint according to your needs. All files from one folder are then combined into a single JSON-file which can be used as an input for the cohesion calculator.
