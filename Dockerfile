FROM python:3.5-alpine

LABEL maintainer="labs@idealista.com"

EXPOSE 8089

RUN apk add gcc libc-dev linux-headers --no-cache

WORKDIR /opt/prom2teams

COPY ./docker/ \
        LICENSE \
        MANIFEST.in \
        README.md \
        requirements.txt \
        setup.py \
        ./

COPY ./bin bin
COPY ./prom2teams prom2teams

RUN python setup.py install

ENV PROM2TEAMS_PORT="8089" \
        PROM2TEAMS_HOST="0.0.0.0" \
        PROM2TEAMS_LOGLEVEL="INFO" \
        PROM2TEAMS_CONNECTOR="" \
        PROM2TEAMS_GROUP_ALERTS_BY="" \
        APP_CONFIG_FILE="/opt/prom2teams/config.ini" \
        PROM2TEAMS_PROMETHEUS_METRICS="true"

ENTRYPOINT ["sh", "prom2teams_start.sh"]
