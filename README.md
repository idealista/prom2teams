![Logo](https://raw.githubusercontent.com/idealista/prom2teams/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/prom2teams.png)](https://travis-ci.org/idealista/prom2teams)

# prom2teams

<img src="assets/example.png" alt="Alert example" style="width: 600px;"/>

**prom2teams** is an HTTP server built with Python that receives alert notifications from a previously configured [Prometheus Alertmanager](https://github.com/prometheus/alertmanager) instance and forwards it to [Microsoft Teams](https://teams.microsoft.com/) using defined connectors.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
  - [Config file](#config-file)
	- [Configuring Prometheus](#configuring-prometheus)
	- [Templating](#templating)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

### Prerequisites

The application has been tested with _Prometheus 1.7.1_, _Python 3.5.0_ and _pip 9.0.1_.

Newer versions of _Prometheus/Python/pip_ should work but could also present issues.

### Installing

prom2teams is present on [PyPI](https://pypi.python.org/pypi/prom2teams), so could be installed using pip3:

```bash
$ pip3 install prom2teams
```

**Note:** Only works since v1.1.1

## Usage

```bash
# To start the server (a config file path must be provided, log file path, log level and Jinja2 template path are optional arguments):
$ prom2teams start --configpath <config file path> [--logfilepath <log file path>] [--loglevel (DEBUG|INFO|WARNING|ERROR|CRITICAL)] [--templatepath <Jinja2 template file path>]

# To show the help message:
$ prom2teams --help
```

**Note:** default log level is INFO. Messages are redirected to stdout if no log file path is provided.

### Config file

The config file is an [INI file](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure) and should have the structure described below:

```
[HTTP Server]
Host: <host ip> # default: 0.0.0.0
Port: <host port> # default: 8089

[Microsoft Teams]
Connector: <webhook url> # required value
```

### Configuring Prometheus

The [webhook receiver](https://prometheus.io/docs/alerting/configuration/#<webhook_config>) in Prometheus allows configuring a prom2teams server.

The url is formed by the host and port defined in the previous step.

```
# The prom2teams endpoint to send HTTP POST requests to.
url: 0.0.0.0:8089
```

### Templating

prom2teams provides a [default template](app/teams/template.j2) built with [Jinja2](http://jinja.pocoo.org/docs/2.9/) to render messages in Microsoft Teams. This template could be overrided using the 'templatepath' argument ('--templatepath <Jinja2 template file path>') during the application start.

## Testing

To run the test suite you should type the following:

```bash
# After cloning prom2 teams :)
$ python3 -m unittest discover tests
```

## Built With
![Python 3.6.2](https://img.shields.io/badge/Python-3.6.2-green.svg)
![pip 9.0.1](https://img.shields.io/badge/pip-9.0.1-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/prom2teams/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/prom2teams/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
