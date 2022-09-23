#!/usr/bin/env python
import os

with open('/opt/prom2teams/config.ini', 'r') as file:
  filedata = file.read()

filedata = filedata.replace("prom2teamsport", os.environ.get("PROM2TEAMS_PORT"))
filedata = filedata.replace("prom2teamshost", os.environ.get("PROM2TEAMS_HOST"))
filedata = filedata.replace("prom2teamsconnector", os.environ.get("PROM2TEAMS_CONNECTOR"))
filedata = filedata.replace("prom2teamsgroupalertsby", os.environ.get("PROM2TEAMS_GROUP_ALERTS_BY"))
filedata = filedata.replace("prom2teamslogslevel", os.environ.get("PROM2TEAMS_LOGLEVEL"))
filedata = filedata.replace("prom2teamstemplatepath", os.environ.get("PROM2TEAMS_TEMPLATEPATH"))

with open('/opt/prom2teams/config.ini', 'w') as file:
  file.write(filedata)

with open('/opt/prom2teams/uwsgi.ini', 'r') as file:
  uwsgi_filedata = file.read()

uwsgi_filedata = uwsgi_filedata.replace("uwsgiprocesses", os.environ.get("UWSGI_PROCESSES"))
uwsgi_filedata = uwsgi_filedata.replace("uwsgithreads", os.environ.get("UWSGI_THREADS"))
uwsgi_filedata = uwsgi_filedata.replace("uwsgiport", os.environ.get("UWSGI_PORT"))
uwsgi_filedata = uwsgi_filedata.replace("uwsgihost", os.environ.get("UWSGI_HOST"))
uwsgi_filedata = uwsgi_filedata.replace("uwsgiprotocol", os.environ.get("UWSGI_PROTOCOL"))


with open('/opt/prom2teams/uwsgi.ini', 'w') as file:
  file.write(uwsgi_filedata)
