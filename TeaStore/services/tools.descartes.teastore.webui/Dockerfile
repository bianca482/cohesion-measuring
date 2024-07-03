FROM descartesresearch/teastore-base:latest
MAINTAINER Chair of Software Engineering <se2-it@informatik.uni-wuerzburg.de>

COPY target/*.war /usr/local/tomcat/webapps/
RUN mkdir -p /usr/local/tomcat/webapps/ROOT

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download and install the OpenTelemetry Java Agent
RUN wget https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.7.2/opentelemetry-javaagent-all.jar -O /opentelemetry-javaagent.jar

# Set the environment variable for the OpenTelemetry Java agent
ENV JAVA_TOOL_OPTIONS "-javaagent:/opentelemetry-javaagent.jar"

# Use the CMD instruction to start the Tomcat server with the OpenTelemetry agent
CMD java -jar /usr/local/tomcat/bin/dockermemoryconfigurator.jar ${TOMCAT_HEAP_MEM_PERCENTAGE} && \
    echo '<% response.sendRedirect("/tools.descartes.teastore.webui/"); %>' > /usr/local/tomcat/webapps/ROOT/index.jsp && \
    export JAVA_TOOL_OPTIONS && /usr/local/tomcat/bin/start.sh && /usr/local/tomcat/bin/catalina.sh run