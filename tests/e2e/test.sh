#!/bin/bash


create_containers(){
    echo "Creating containers..."
    docker-compose up --build -d 
}

create_expectations_and_responses(){
    echo "Creating expectations and responses in teams mockserver..."
    sleep 10 # To wait for containers to start
    curl -s -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
        "httpRequest": {
            "method": "POST",
            "path": "/api/test",
            "body": {
            "type": "message",
            "attachments": [
                {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {
                    "width": "Full"
                    },
                    "body": [
                    {
                        "type": "ColumnSet",
                        "style": "attention",
                        "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                            {
                                "type": "TextBlock",
                                "text": "Prometheus alert NodeExporter triggered",
                                "weight": "Bolder",
                                "size": "Large"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Node exporter down on node1.summit",
                                "wrap": true
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                        {
                            "title": "Alert",
                            "value": "NodeExporter"
                        },
                        {
                            "title": "In host",
                            "value": "node1.summit"
                        },
                        {
                            "title": "Severity",
                            "value": "critical"
                        },
                        {
                            "title": "Description",
                            "value": "Node exporter down on node1.summit"
                        },
                        {
                            "title": "Status",
                            "value": "firing"
                        },
                        {
                            "title": "job",
                            "value": "node_exporter"
                        },
                        {
                            "title": "notify_room",
                            "value": "test"
                        },
                        {
                            "title": "env",
                            "value": "production"
                        },
                        {
                            "title": "type",
                            "value": "nodeexporter"
                        }
                        ]
                    }
                    ]
                }
                }
            ]
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "body": "1"
        }
        }' > /dev/null 2>&1


    curl -s -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
        "httpRequest": {
            "method": "POST",
            "path": "/api/test",
            "body": {
            "type": "message",
            "attachments": [
                {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {
                    "width": "Full"
                    },
                    "body": [
                    {
                        "type": "ColumnSet",
                        "style": "attention",
                        "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                            {
                                "type": "TextBlock",
                                "text": "Prometheus alert NodeExporter triggered",
                                "weight": "Bolder",
                                "size": "Large"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Node exporter down on node2.summit",
                                "wrap": true
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                        {
                            "title": "Alert",
                            "value": "NodeExporter"
                        },
                        {
                            "title": "In host",
                            "value": "node2.summit"
                        },
                        {
                            "title": "Severity",
                            "value": "critical"
                        },
                        {
                            "title": "Description",
                            "value": "Node exporter down on node2.summit"
                        },
                        {
                            "title": "Status",
                            "value": "firing"
                        },
                        {
                            "title": "job",
                            "value": "node_exporter"
                        },
                        {
                            "title": "notify_room",
                            "value": "test"
                        },
                        {
                            "title": "env",
                            "value": "production"
                        },
                        {
                            "title": "type",
                            "value": "nodeexporter"
                        }
                        ]
                    }
                    ]
                }
                }
            ]
            }
        },
        "httpResponse": {
            "statusCode": 200,
            "body": "1"
        }
        }' > /dev/null 2>&1
    
    curl -s -v -X PUT "http://localhost:1080/mockserver/expectation" -d '{
        "httpRequest": {
            "method": "POST",
            "path": "/api/test",
            "body": {
            "type": "message",
            "attachments": [
                {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {
                    "width": "Full"
                    },
                    "body": [
                    {
                        "type": "ColumnSet",
                        "style": "attention",
                        "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                            {
                                "type": "TextBlock",
                                "text": "Prometheus alert NodeExporter triggered",
                                "weight": "Bolder",
                                "size": "Large"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Node exporter down on node3.summit",
                                "wrap": true
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                        {
                            "title": "Alert",
                            "value": "NodeExporter"
                        },
                        {
                            "title": "In host",
                            "value": "node3.summit"
                        },
                        {
                            "title": "Severity",
                            "value": "critical"
                        },
                        {
                            "title": "Description",
                            "value": "Node exporter down on node3.summit"
                        },
                        {
                            "title": "Status",
                            "value": "firing"
                        },
                        {
                            "title": "job",
                            "value": "node_exporter"
                        },
                        {
                            "title": "notify_room",
                            "value": "test"
                        },
                        {
                            "title": "type",
                            "value": "nodeexporter"
                        },
                        {
                            "title": "env",
                            "value": "production"
                        },
                        ]
                    }
                    ]
                }
                }
            ]
            }
        },
        "httpResponse": {
            "statusCode": 202
        }
        }' > /dev/null 2>&1
}

run_tests(){
    echo "Running tests..."
    # Alertmanager 0.21.0 request    
    test1=$(curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node1.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node1.summit\", \"summary\": \"Node exporter down on node1.summit\" }, \"startsAt\": \"2020-09-16T07:38:01.586706006Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"e4ad109767ee663e\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"job\": \"node_exporter\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\", \"truncatedAlerts\": 0}")
    # Alertmanager 0.20.0 request
    test2=$(curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node2.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node2.summit\", \"summary\": \"Node exporter down on node2.summit\" }, \"startsAt\": \"2020-09-16T08:09:50.791949454Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"96b211b05dc430e8\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\"}")
    # Alertmanager Teams workflow
    test3=$(curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://localhost:8089/v2/connector" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"receiver\": \"test\", \"status\": \"firing\", \"alerts\": [ { \"status\": \"firing\", \"labels\": { \"alertname\": \"NodeExporter\", \"env\": \"production\", \"instance\": \"node3.summit\", \"job\": \"node_exporter\", \"notify_room\": \"test\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"annotations\": { \"description\": \"Node exporter down on node3.summit\", \"summary\": \"Node exporter down on node3.summit\" }, \"startsAt\": \"2020-09-16T07:38:01.586706006Z\", \"endsAt\": \"0001-01-01T00:00:00Z\", \"generatorURL\": \"\", \"fingerprint\": \"e4ad109767ee663e\" } ], \"groupLabels\": { \"alertname\": \"NodeExporter\" }, \"commonLabels\": { \"alertname\": \"NodeExporter\", \"job\": \"node_exporter\", \"severity\": \"critical\", \"type\": \"nodeexporter\" }, \"commonAnnotations\": {}, \"externalURL\": \"http://localhost:9093\", \"version\": \"4\", \"groupKey\": \"{}/{notify_room=~\\\"^(?:.*test.*)$\\\"}:{alertname=\\\"NodeExporter\\\"}\", \"truncatedAlerts\": 0}")


    test1verify=$(curl -s -w "%{http_code}\n" -X PUT "http://localhost:1080/mockserver/verify" -d '{
        "httpRequest": {
            "method": "POST",
            "path": "/api/test",
            "body": {
                "type": "message",
                "attachments": [
                    {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.4",
                        "msteams": {
                        "width": "Full"
                        },
                        "body": [
                        {
                            "type": "ColumnSet",
                            "style": "attention",
                            "columns": [
                            {
                                "type": "Column",
                                "width": "stretch",
                                "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "Prometheus alert NodeExporter triggered",
                                    "weight": "Bolder",
                                    "size": "Large"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": "Node exporter down on node1.summit",
                                    "wrap": true
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "FactSet",
                            "facts": [
                            {
                                "title": "Alert",
                                "value": "NodeExporter"
                            },
                            {
                                "title": "In host",
                                "value": "node1.summit"
                            },
                            {
                                "title": "Severity",
                                "value": "critical"
                            },
                            {
                                "title": "Description",
                                "value": "Node exporter down on node1.summit"
                            },
                            {
                                "title": "Status",
                                "value": "firing"
                            },
                            {
                                "title": "job",
                                "value": "node_exporter"
                            },
                            {
                                "title": "env",
                                "value": "production"
                            },
                            {
                                "title": "notify_room",
                                "value": "test"
                            },
                            {
                                "title": "type",
                                "value": "nodeexporter"
                            }

                            ]
                        }
                        ]
                    }
                    }
                ]
                }
        }
        },
      },
        "times": {
            "atLeast": 1,
            "atMost": 1
        }
    }')

    test2verify=$(curl -s -w "%{http_code}\n" -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "method": "POST",
        "path": "/api/test",
        "body": {
            "type": "message",
            "attachments": [
                {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {
                    "width": "Full"
                    },
                    "body": [
                    {
                        "type": "ColumnSet",
                        "style": "attention",
                        "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                            {
                                "type": "TextBlock",
                                "text": "Prometheus alert NodeExporter triggered",
                                "weight": "Bolder",
                                "size": "Large"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Node exporter down on node2.summit",
                                "wrap": true
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                        {
                            "title": "Alert",
                            "value": "NodeExporter"
                        },
                        {
                            "title": "In host",
                            "value": "node2.summit"
                        },
                        {
                            "title": "Severity",
                            "value": "critical"
                        },
                        {
                            "title": "Description",
                            "value": "Node exporter down on node2.summit"
                        },
                        {
                            "title": "Status",
                            "value": "firing"
                        },
                        {
                            "title": "job",
                            "value": "node_exporter"
                        },
                        {
                            "title": "notify_room",
                            "value": "test"
                        },
                        {
                            "title": "env",
                            "value": "production"
                        },
                        {
                            "title": "type",
                            "value": "nodeexporter"
                        }
                        ]
                    }
                    ]
                }
                }
            ]
            }
    }
      },
        "times": {
            "atLeast": 1,
            "atMost": 1
        }
    }')

    test3verify=$(curl -s -w "%{http_code}\n" -X PUT "http://localhost:1080/mockserver/verify" -d '{
    "httpRequest": {
        "method": "POST",
        "path": "/api/test",
        "body": {
            "type": "message",
            "attachments": [
                {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "msteams": {
                    "width": "Full"
                    },
                    "body": [
                    {
                        "type": "ColumnSet",
                        "style": "attention",
                        "columns": [
                        {
                            "type": "Column",
                            "width": "stretch",
                            "items": [
                            {
                                "type": "TextBlock",
                                "text": "Prometheus alert NodeExporter triggered",
                                "weight": "Bolder",
                                "size": "Large"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Node exporter down on node3.summit",
                                "wrap": true
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                        {
                            "title": "Alert",
                            "value": "NodeExporter"
                        },
                        {
                            "title": "In host",
                            "value": "node3.summit"
                        },
                        {
                            "title": "Severity",
                            "value": "critical"
                        },
                        {
                            "title": "Description",
                            "value": "Node exporter down on node3.summit"
                        },
                        {
                            "title": "Status",
                            "value": "firing"
                        },
                        {
                            "title": "job",
                            "value": "node_exporter"
                        },
                        {
                            "title": "notify_room",
                            "value": "test"
                        },
                        {
                            "title": "env",
                            "value": "production"
                        },
                        {
                            "title": "type",
                            "value": "nodeexporter"
                        }
                        ]
                    }
                    ]
                }
                }
            ]
            }
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
    if [[ "$test3" -eq 201 && "$test3verify" -eq 202 ]]
    then
        echo "Test 3: OK"
    else
        echo "Test 3: Failed"
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
