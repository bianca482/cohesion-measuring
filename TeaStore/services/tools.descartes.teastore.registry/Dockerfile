FROM descartesresearch/teastore-base:latest
MAINTAINER Chair of Software Engineering <se2-it@informatik.uni-wuerzburg.de>

COPY target/*.war /usr/local/tomcat/webapps/

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*
    
# Download and install the OpenTelemetry Java Agent
RUN wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.7.2/opentelemetry-javaagent-all.jar -O /opentelemetry-javaagent.jar

# Set the environment variable for the OpenTelemetry Java agent
ENV JAVA_TOOL_OPTIONS "-javaagent:/opentelemetry-javaagent.jar"