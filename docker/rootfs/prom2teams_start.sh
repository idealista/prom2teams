#!/bin/sh
python /opt/prom2teams/replace_config.py
uwsgi /opt/prom2teams/uwsgi.ini