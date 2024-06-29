python -m pip install grpcio
python -m pip install grpcio-tools

scenarios\grcp>python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. protos/query.proto protos/ protos/model.proto gogoproto/gogo.proto protos/google/api/annotations.proto protos/google/api/http.proto protos/google/protobuf/descriptor.proto protos/google/protobuf/timestamp.proto protos/google/protobuf/duration.proto
