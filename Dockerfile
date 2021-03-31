FROM python:3.8-alpine AS builder
WORKDIR /prom2teams
COPY LICENSE \
        MANIFEST.in \
        README.md \
        requirements.txt \
        setup.py \
        ./
COPY prom2teams/ prom2teams
COPY bin/ bin
RUN apk add gcc libc-dev yaml-dev linux-headers --no-cache \
        && python setup.py bdist_wheel

FROM python:3.8-alpine
LABEL maintainer="labs@idealista.com"
EXPOSE 8089
WORKDIR /opt/prom2teams
COPY docker/rootfs .
COPY --from=builder /prom2teams/dist .
RUN apk add gcc libc-dev yaml-dev linux-headers --no-cache \
	&& pip install prom2teams*.whl
ENV PROM2TEAMS_PORT="8089" \
        PROM2TEAMS_HOST="0.0.0.0" \
        PROM2TEAMS_LOGLEVEL="INFO" \
        PROM2TEAMS_CONNECTOR="" \
        PROM2TEAMS_GROUP_ALERTS_BY="" \
        APP_CONFIG_FILE="/opt/prom2teams/config.ini" \
        PROM2TEAMS_PROMETHEUS_METRICS="true"
ENTRYPOINT ["sh", "prom2teams_start.sh"]
