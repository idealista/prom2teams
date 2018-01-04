FROM python:3.5-slim-jessie

LABEL maintainer="labs@idealista.com"

EXPOSE 8089

RUN pip install prom2teams
COPY config.ini /opt/prom2teams/config.ini

ENTRYPOINT ["prom2teams", "--configpath", "/opt/prom2teams/config.ini"]
