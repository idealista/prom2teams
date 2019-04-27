#!/bin/sh
python /opt/prom2teams/replace_config.py
prom2teams --configpath /opt/prom2teams/config.ini --loglevel $PROM2TEAMS_LOGLEVEL
