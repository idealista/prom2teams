#!/bin/bash

# Alertmanager 0.21.0
# {
#  "receiver": "test",
#  "status": "firing",
#  "alerts": [
#    {
#      "status": "firing",
#      "labels": {
#        "alertname": "NodeExporter",
#        "env": "production",
#        "instance": "node1.summit",
#        "job": "node_exporter",
#        "notify_room": "test",
#        "severity": "critical",
#        "type": "nodeexporter"
#      },
#      "annotations": {
#        "description": "Node exporter down on node1.summit",
#        "summary": "Node exporter down on node1.summit"
#      },
#      "startsAt": "2020-09-16T07:38:01.586706006Z",
#      "endsAt": "0001-01-01T00:00:00Z",
#      "generatorURL": "",
#      "fingerprint": "e4ad109767ee663e"
#    }
#  ],
#  "groupLabels": {
#    "alertname": "NodeExporter"
#  },
#  "commonLabels": {
#    "alertname": "NodeExporter",
#    "job": "node_exporter",
#    "severity": "critical",
#    "type": "nodeexporter"
#  },
#  "commonAnnotations": {},
#  "externalURL": "http://localhost:9093",
#  "version": "4",
#  "groupKey": "{}/{notify_room=~\"^(?:.*test.*)$\"}:{alertname=\"NodeExporter\"}",
#  "truncatedAlerts": 0
#}
#  

# Alertmanager 0.20.0
# {
#  "receiver": "test",
#  "status": "firing",
#  "alerts": [
#    {
#      "status": "firing",
#      "labels": {
#        "alertname": "NodeExporter",
#        "env": "production",
#        "instance": "node2.summit",
#        "job": "node_exporter",
#        "notify_room": "test",
#        "severity": "critical",
#        "type": "nodeexporter"
#      },
#      "annotations": {
#        "description": "Node exporter down on node2.summit",
#        "summary": "Node exporter down on node2.summit"
#      },
#      "startsAt": "2020-09-16T08:09:50.791949454Z",
#      "endsAt": "0001-01-01T00:00:00Z",
#      "generatorURL": "generator",
#      "fingerprint": "96b211b05dc430e8"
#    }
#  ],
#  "groupLabels": {
#    "alertname": "NodeExporter"
#  },
#  "commonLabels": {
#    "alertname": "NodeExporter",
#    "env": "production",
#    "job": "node_exporter",
#    "notify_room": "test",
#    "severity": "critical",
#    "type": "nodeexporter"
#  },
#  "commonAnnotations": {},
#  "externalURL": "http://localhost:9093",
#  "version": "4",
#  "groupKey": "{}/{notify_room=~\"^(?:.*test.*)$\"}:{alertname=\"NodeExporter\"}"
#}

echo "Creating containers..."
docker-compose up --build -d > /dev/null 2>&1

echo "Creating expectations and responses..."
sleep 10
curl -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
  "httpRequest" : {
    "method" : "POST",
    "path" : "/api/test"
  },
  "httpResponse" : {
    "statusCode": 200,
    "body" : "1"
  }
}'


echo "Running tests..."
# Alertmanager 0.21.0 request
test1=$(curl -s -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node1.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node1.summit\", \"summary\": \"Node exporter down on node1.summit\" }, \"startsAt\": \"2020-09-16T07:38:01.586706006Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"e4ad109767ee663e\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"job\": \"node_exporter\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\", \"truncatedAlerts\": 0}")
# Alertmanager 0.20.0 request
test2=$(curl -s -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node2.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node2.summit\", \"summary\": \"Node exporter down on node2.summit\" }, \"startsAt\": \"2020-09-16T08:09:50.791949454Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"96b211b05dc430e8\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\"}")

passing=1
if [[ "$test1" = "\"OK\"" ]]
then
    echo "Test 1: OK"
else
    echo "Test 1: Failed"
    passing=0
fi
if [[ "$test2" = "\"OK\"" ]]
then
    echo "Test 2: OK"
else
    echo "Test 2: Failed"
    passing=0
fi

echo "Destroying containers..."
docker-compose down > /dev/null 2>&1

if [ "$passing" -eq 1 ]
then
    echo "TESTS FINISHED SUCCESSFULLY"
    exit 0
fi
echo "TESTS FAILED"
exit 1
