FROM python:3.5-alpine

LABEL maintainer="labs@idealista.com"

EXPOSE 8089

RUN apk add gcc libc-dev linux-headers --update-cache \
    && rm -rf /var/cache/apk/*

WORKDIR /opt/prom2teams

COPY LICENSE \
        MANIFEST.in \
        README.md \
        requirements.txt \
        setup.py \
        ./docker/config.ini \
        ./docker/replace_config.py \
        ./docker/prom2teams_start.sh \
        ./

COPY ./bin bin
COPY ./prom2teams prom2teams

RUN python setup.py install

ENV PROM2TEAMS_PORT="8089"
ENV PROM2TEAMS_HOST="0.0.0.0"
ENV PROM2TEAMS_LOGLEVEL="INFO"
ENV PROM2TEAMS_CONNECTOR=""
ENV PROM2TEAMS_GROUP_ALERTS_BY=""

ENTRYPOINT ["sh", "prom2teams_start.sh"]