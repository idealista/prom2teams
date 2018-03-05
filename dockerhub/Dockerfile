FROM python:3.6-slim-stretch

LABEL maintainer="labs@idealista.com"

EXPOSE 8089

RUN apt-get update && apt-get install -y build-essential
RUN pip install prom2teams
COPY config.ini /opt/prom2teams/config.ini
COPY prom2teams_start.sh /opt/prom2teams/prom2teams_start.sh
COPY replace_config.py /opt/prom2teams/replace_config.py

ENV PROM2TEAMS_PORT="8089"
ENV PROM2TEAMS_HOST="0.0.0.0"
ENV PROM2TEAMS_LOGLEVEL="INFO"
ENV PROM2TEAMS_CONNECTOR=""

ENTRYPOINT ["bash", "/opt/prom2teams/prom2teams_start.sh"]
