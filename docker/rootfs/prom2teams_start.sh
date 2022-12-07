#!/bin/sh
python /opt/prom2teams/replace_config.py

if [ ! -f "/opt/prom2teams/config.ini" ]; then
    mv /opt/prom2teams/config.ini.tmp /opt/prom2teams/config.ini
fi

if [[ ! -f "/opt/prom2teams/uwsgi.ini" ]]; then
    mv /opt/prom2teams/uwsgi.ini.tmp /opt/prom2teams/uwsgi.ini
fi

uwsgi /opt/prom2teams/uwsgi.ini
