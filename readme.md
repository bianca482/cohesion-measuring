# Cohesion Measurement

This is the repository for the master thesis "Investigation of microservice applications with
with regard to possible problematic architectural boundaries. Identification of indicators of potentially problematic
architectural boundaries in microservice-based applications and development of an automatic tool to recognise them."

This repository contains the following:

- **cohesion**: Contains the actual implementation for calculating SCOM (Sensitive Cohesion Class Metric).
- **examples**: Contains the sample application used for testing the cohesion measurement as well as scripts for analyzing the TeaStore application in regards of cohesion.
- **grpc**: Contains all neccessary protos and scripts to retrieve Jaeger traces using their gRPC/Protobuf endpoint.
- **TeaStore**: Contains a copy of the [TeaStore-Project](https://github.com/DescartesResearch/TeaStore) with the proposed changes for setting up OpenTelemetry and Jaeger to instrument the application. Following has been changed:

  - `TeaStore\examples\docker\cohesion_measuring` has been added. In this folder you can find the adjusted `docker-compose.yaml`-File.
  - The subfolder `locust` contains the exact same `locustfile.py` as already provided by the original authors, but with the host already defined.
  - `script.bat` has been added to remove all docker container and volumes for testing.

  To run the TeaStore application with OpenTelemetry instrumentation run `docker-compose -f ./TeaStore/examples/docker/cohesion_measuring/docker-compose.yaml up -d --build`

  The locust file can be run by executing `locust -f locustfile.py` from the `TeaStore\examples\docker\cohesion_measuring\locust` location. Make sure that locust is installed. Open http://localhost:8089/ and start simulating the application. After this, use the `grpc\retrieve_traces.py` script to obtain the traces.
