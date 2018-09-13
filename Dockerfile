FROM python:3.6-slim-stretch

LABEL maintainer="labs@idealista.com"

EXPOSE 8089

RUN apt-get update && apt-get install -y build-essential

ADD LICENSE /opt/prom2teams/LICENSE
ADD MANIFEST.in /opt/prom2teams/MANIFEST.in
ADD README.md /opt/prom2teams/README.md
ADD requirements.txt /opt/prom2teams/requirements.txt
ADD setup.py /opt/prom2teams/setup.py

ADD ./bin /opt/prom2teams/bin
ADD ./prom2teams /opt/prom2teams/prom2teams

ADD ./dockerhub/config.ini /opt/prom2teams/config.ini
ADD ./dockerhub/replace_config.py /opt/prom2teams/replace_config.py
ADD ./dockerhub/prom2teams_start.sh /opt/prom2teams/prom2teams_start.sh

WORKDIR /opt/prom2teams
RUN python setup.py install

ENV PROM2TEAMS_PORT="8089"
ENV PROM2TEAMS_HOST="0.0.0.0"
ENV PROM2TEAMS_LOGLEVEL="INFO"
ENV PROM2TEAMS_CONNECTOR=""
ENV PROM2TEAMS_GROUP_ALERTS_BY=""

ENTRYPOINT ["bash", "/opt/prom2teams/prom2teams_start.sh"]