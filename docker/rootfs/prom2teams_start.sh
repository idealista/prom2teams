#!/bin/sh
python /opt/prom2teams/replace_config.py
prom2teams --loglevel $PROM2TEAMS_LOGLEVEL
