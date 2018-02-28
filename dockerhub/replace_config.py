#!/usr/bin/env python
import os

with open('/opt/prom2teams/config.ini', 'r') as file:
  filedata = file.read()

filedata = filedata.replace("prom2teamsport", os.environ.get("PROM2TEAMS_PORT"))
filedata = filedata.replace("prom2teamshost", os.environ.get("PROM2TEAMS_HOST"))
filedata = filedata.replace("prom2teamsconnector", os.environ.get("PROM2TEAMS_CONNECTOR"))

with open('/opt/prom2teams/config.ini', 'w') as file:
  file.write(filedata)
