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
EXPOSE 9090
WORKDIR /opt/prom2teams
COPY docker/rootfs .
COPY --from=builder /prom2teams/dist .
COPY bin/wsgi.py ./wsgi.py
RUN apk add gcc libc-dev yaml-dev linux-headers pcre pcre-dev --no-cache \
	&& pip install prom2teams*.whl
RUN addgroup -g "101" -S prom2teams && \
        adduser -S prom2teams -G prom2teams -u "101" && \
        mkdir -p /var/log/prom2teams && \
        mkdir -p /opt/prom2teams/metrics && \
        chown -R prom2teams:prom2teams /var/log/prom2teams && \
        chown -R prom2teams:prom2teams /opt/prom2teams
USER prom2teams
ENV PROM2TEAMS_PORT="8089" \
        PROM2TEAMS_HOST="localhost" \
        PROM2TEAMS_LOGLEVEL="INFO" \
        PROM2TEAMS_CONNECTOR="" \
        PROM2TEAMS_GROUP_ALERTS_BY="" \
        APP_CONFIG_FILE="/opt/prom2teams/config.ini" \
        PROM2TEAMS_PROMETHEUS_METRICS="true" \
        UWSGI_PROCESSES="1" \
        UWSGI_THREADS="1" \
        UWSGI_PORT="8089" \
        UWSGI_HOST="0.0.0.0" \
        UWSGI_PROTOCOL="http" \
        PROMETHEUS_MULTIPROC_PORT="9090" \
        PROMETHEUS_MULTIPROC_DIR="/opt/prom2teams/metrics" \
        prometheus_multiproc_dir="/opt/prom2teams/metrics"
ENTRYPOINT ["sh", "prom2teams_start.sh"]
