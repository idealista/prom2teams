#!/bin/bash

if ! command -v docker-compose &> /dev/null
then
    echo "The 'docker-compose' command could not be found!"
    echo "See https://docs.docker.com/compose/install/ for installation instructions."
    exit 1
fi

create_containers(){
    echo "Creating containers..."
    docker-compose up --build -d > /dev/null 2>&1
}

create_expectations_and_responses(){
    echo "Creating expectations and responses in teams mockserver..."
    sleep 10 # To wait for containers to start
    curl -s -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
      "httpRequest" : {
        "method" : "POST",
        "path" : "/api/test",
        "body": {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": " 8C1A1A ",
        "summary": "Node exporter down on node1.summit",
        "title": "Prometheus alert ",
        "sections": [{
            "activityTitle": "Node exporter down on node1.summit",
            "facts": [{
                "name": "Alert",
                "value": "NodeExporter"
            },{
                "name": "In host",
                "value": "node1.summit"
            },{
                "name": "Severity",
                "value": "critical"
            },{
                "name": "Description",
                "value": "Node exporter down on node1.summit"
            },{
                "name": "Status",
                "value": "firing"
            },{
                "name": "job",
                "value": "node_exporter"
            },{
                "name": "env",
                "value": "production"
            },{
                "name": "notify_room",
                "value": "test"
            },{
                "name": "type",
                "value": "nodeexporter"
            }        ],
              "markdown": true
        }]
    }
      },
      "httpResponse" : {
        "statusCode": 200,
        "body" : "1"
      }
    }' > /dev/null 2>&1


    curl -s -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
      "httpRequest" : {
        "method" : "POST",
        "path" : "/api/test",
        "body": {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": " 8C1A1A ",
        "summary": "Node exporter down on node2.summit",
        "title": "Prometheus alert ",
        "sections": [{
            "activityTitle": "Node exporter down on node2.summit",
            "facts": [{
                "name": "Alert",
                "value": "NodeExporter"
            },{
                "name": "In host",
                "value": "node2.summit"
            },{
                "name": "Severity",
                "value": "critical"
            },{
                "name": "Description",
                "value": "Node exporter down on node2.summit"
            },{
                "name": "Status",
                "value": "firing"
            },{
                "name": "job",
                "value": "node_exporter"
            },{
                "name": "env",
                "value": "production"
            },{
                "name": "notify_room",
                "value": "test"
            },{
                "name": "type",
                "value": "nodeexporter"
            }        ],
              "markdown": true
        }]
    }
      },
      "httpResponse" : {
        "statusCode": 200,
        "body" : "1"
      }
    }' > /dev/null 2>&1
}

run_tests(){
    echo "Running tests..."
    # Alertmanager 0.21.0 request
    test1=$(curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node1.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node1.summit\", \"summary\": \"Node exporter down on node1.summit\" }, \"startsAt\": \"2020-09-16T07:38:01.586706006Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"e4ad109767ee663e\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"job\": \"node_exporter\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\", \"truncatedAlerts\": 0}")
    # Alertmanager 0.20.0 request
    test2=$(curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node2.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node2.summit\", \"summary\": \"Node exporter down on node2.summit\" }, \"startsAt\": \"2020-09-16T08:09:50.791949454Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"96b211b05dc430e8\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\"}")

    test1verify=$(curl -s -w "%{http_code}\n" -X PUT "http://localhost:1080/mockserver/verify" -d '{
        "httpRequest" : {
        "method" : "POST",
        "path" : "/api/test",
        "body": {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": " 8C1A1A ",
        "summary": "Node exporter down on node1.summit",
        "title": "Prometheus alert ",
        "sections": [{
            "activityTitle": "Node exporter down on node1.summit",
            "facts": [{
                "name": "Alert",
                "value": "NodeExporter"
            },{
                "name": "In host",
                "value": "node1.summit"
            },{
                "name": "Severity",
                "value": "critical"
            },{
                "name": "Description",
                "value": "Node exporter down on node1.summit"
            },{
                "name": "Status",
                "value": "firing"
            },{
                "name": "job",
                "value": "node_exporter"
            },{
                "name": "env",
                "value": "production"
            },{
                "name": "notify_room",
                "value": "test"
            },{
                "name": "type",
                "value": "nodeexporter"
            }        ],
              "markdown": true
        }]
    }
      },
        "times": {
            "atLeast": 1,
            "atMost": 1
        }
    }')

    test2verify=$(curl -s -w "%{http_code}\n" -X PUT "http://localhost:1080/mockserver/verify" -d '{
        "httpRequest" : {
        "method" : "POST",
        "path" : "/api/test",
        "body": {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": " 8C1A1A ",
        "summary": "Node exporter down on node2.summit",
        "title": "Prometheus alert ",
        "sections": [{
            "activityTitle": "Node exporter down on node2.summit",
            "facts": [{
                "name": "Alert",
                "value": "NodeExporter"
            },{
                "name": "In host",
                "value": "node2.summit"
            },{
                "name": "Severity",
                "value": "critical"
            },{
                "name": "Description",
                "value": "Node exporter down on node2.summit"
            },{
                "name": "Status",
                "value": "firing"
            },{
                "name": "job",
                "value": "node_exporter"
            },{
                "name": "env",
                "value": "production"
            },{
                "name": "notify_room",
                "value": "test"
            },{
                "name": "type",
                "value": "nodeexporter"
            }        ],
              "markdown": true
        }]
    }
      },
        "times": {
            "atLeast": 1,
            "atMost": 1
        }
    }')

    passing=1
    if [[ "$test1" -eq 201 && "$test1verify" -eq 202 ]]
    then
        echo "Test 1: OK"
    else
        echo "Test 1: Failed"
        passing=0
    fi
    if [[ "$test2" -eq 201 && "$test2verify" -eq 202 ]]
    then
        echo "Test 2: OK"
    else
        echo "Test 2: Failed"
        passing=0
    fi
}

destroy_containers(){
    echo "Destroying containers..."
    docker-compose down > /dev/null 2>&1
}

display_results_and_exit(){
    if [ "$passing" -eq 1 ]
    then
        echo "TESTS FINISHED SUCCESSFULLY"
        exit 0
    fi
    echo "TESTS FAILED"
    exit 1
}

main(){
    create_containers
    create_expectations_and_responses
    run_tests
    destroy_containers
    display_results_and_exit
}

main
