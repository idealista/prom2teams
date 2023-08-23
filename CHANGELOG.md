# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/prom2teams/tree/develop)
## [4.2.2](https://github.com/idealista/prom2teams/tree/4.2.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/4.2.1...4.2.2)
### Added
- *[#325](https://github.com/idealista/prom2teams/pull/325) add metrics port configuration in Helm* @santi-eidu
## [4.2.1](https://github.com/idealista/prom2teams/tree/4.2.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/4.2.0...4.2.1)
### Fixed
- *[#307](https://github.com/idealista/prom2teams/pull/307) Update prom2teams replace_config with tmp config files* @santi-eidu
## [4.2.0](https://github.com/idealista/prom2teams/tree/4.2.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/4.1.0...4.2.0)
### Added
- *[#312](https://github.com/idealista/prom2teams/pull/312) Improve error handler to distinguish between different kind of exceptions* @smartinsempere
## [4.1.0](https://github.com/idealista/prom2teams/tree/4.1.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/4.0.0...4.1.0)
### Fixed
- *[#309](https://github.com/idealista/prom2teams/pull/309) Update prom2teams to use flask exporter with uWSGI for metrics when using uWSGI mode* @santi-eidu
## [4.0.0](https://github.com/idealista/prom2teams/tree/4.0.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.3.0...4.0.0)
### Fixed
- *[#301](https://github.com/idealista/prom2teams/pull/301) Update image to use uWSGI* @santi-eidu
### Added
- *[#297](https://github.com/idealista/prom2teams/issues/297) Add travis job to upload docker image to Dockerhub* @santi-eidu
- *[#296](https://github.com/idealista/prom2teams/issues/296) Release 3.3.0 missing on Docker Hub* @santi-eidu

## [3.3.0](https://github.com/idealista/prom2teams/tree/3.3.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.2.3...3.3.0)
### Fixed
- *[#290](https://github.com/idealista/prom2teams/pull/290) Fixed .travis.yml config file and added to requirements.txt some missing dependencies.* @ommarmol
- *[#279](https://github.com/idealista/prom2teams/pull/279) Fixed issue with MS Teams exception handling* @nryabkov
### Added
- *[#281](https://github.com/idealista/prom2teams/pull/281) Allow to add arbitrary envvars to deployment* @dkobras
- *[#292](https://github.com/idealista/prom2teams/issues/292) Configurable timeout for the request* @blalop

## [3.2.3](https://github.com/idealista/prom2teams/tree/3.2.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.2.2...3.2.3)
### Fixed
- *[#271](https://github.com/idealista/prom2teams/pull/271) Sending a message with double quotes in TeamsAlert fields breaks MS Teams communication* @earthquakesan
- *[#275](https://github.com/idealista/prom2teams/pull/275) Fix error handling when exception thrown, to return HTTP 500 @srl295

## [3.2.2](https://github.com/idealista/prom2teams/tree/3.2.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.2.1...3.2.2)
### Changed
- Bump jinja2 and pyYAML versions @blalop

## [3.2.1](https://github.com/idealista/prom2teams/tree/3.2.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.2.0...3.2.1)
### Fixed
- *[#225](https://github.com/idealista/prom2teams/issues/250) Fix error when fingerprint is missing @jperera
### Changed
- *[#244](https://github.com/idealista/prom2teams/issues/244) Change travis-ci.org by travis-ci.com in README @Crozzers
## [3.2.0](https://github.com/idealista/prom2teams/tree/3.2.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.1.0...3.2.0)
### Added
- *[#225](https://github.com/idealista/prom2teams/pull/225) Add /alive and /ready endpoints* @vicsufer
- *[#241](https://github.com/idealista/prom2teams/issues/241) Add action on runbook_url annotation* @jperera

## Changed
- *[#155](https://github.com/idealista/prom2teams/issues/155) Using Alert instead of Alarm in the entire code base* @dortegau

## [3.1.0](https://github.com/idealista/prom2teams/tree/3.1.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/3.0.0...3.1.0)
### Fixed
- *[#219](https://github.com/idealista/prom2teams/pull/219) Add timeouts to webhook request to prevent hanging tcp connections in case of network errors* @DanSipola
### Added
- *[#222](https://github.com/idealista/prom2teams/pull/222) Add restrictive security context since the workload doesn't need more permissions to work.* @azman0101
- *[#226](https://github.com/idealista/prom2teams/pull/226) Retrying policy* @blalop

## [3.0.0](https://github.com/idealista/prom2teams/tree/3.0.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.7.0...3.0.0)
### Breaking changes
Now connector field is mandatory in helm chart is mantatory.

### Added
- *[#175](https://github.com/idealista/prom2teams/issues/175) Building docker image using multi-stage build feature* @dortegau
- *[#172](https://github.com/idealista/prom2teams/pull/172) Add fingerprint field to template data* @mdelagrange
- *[#170](https://github.com/idealista/prom2teams/issues/170) Allow specifying multiple connectors* @krmichel

## [2.7.0](https://github.com/idealista/prom2teams/tree/2.7.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.6.0...2.7.0)
### Added
* *[#213](https://github.com/idealista/prom2teams/issues/213) Add end to end tests* @pablogcaldito

## [2.6.0](https://github.com/idealista/prom2teams/tree/2.6.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.8...2.6.0)
### Fixed
* *[#210](https://github.com/idealista/prom2teams/issues/210) Fix bug introduced in 2.5.6 version and add support for alertmanager 0.21.0* @pablogcaldito

## [2.5.8](https://github.com/idealista/prom2teams/tree/2.5.8)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.7...2.5.8)
### Fixed
* *[#201](https://github.com/idealista/prom2teams/issues/201) /metrics server not working* @vicsufer

## [2.5.7](https://github.com/idealista/prom2teams/tree/2.5.7)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.6...2.5.7)
## Fixed
- *[#189](https://github.com/idealista/prom2teams/issues/189) Fixed handling alerts with truncated fields* @dgalcantara
- *[#190](https://github.com/idealista/prom2teams/pull/190) Fixed handling of additional json properties of alertmanager 0.21.0* @lazyBisa
- *[#202](https://github.com/idealista/prom2teams/issues/202) Fix error publishing 2.5.7 release* @pablogcaldito
- *[#189](https://github.com/idealista/prom2teams/issues/189) Fixed handling alerts with truncated fields* @dgalcantara

## [2.5.6](https://github.com/idealista/prom2teams/tree/2.5.6)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.5...2.5.6)
## Fixed
- *[#190](https://github.com/idealista/prom2teams/pull/190) Fixed handling of additional json properties of alertmanager 0.21.0* @lazyBisa

## [2.5.5](https://github.com/idealista/prom2teams/tree/2.5.5)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.4...2.5.5)
## Changed
- *[#175](https://github.com/idealista/prom2teams/issues/175) Building docker image using multi-stage build feature* @dortegau

## Fixed
- *[#158](https://github.com/idealista/prom2teams/issues/158) Fixing Travis Badge (pointing to master branch) and reordering TOC* @dortegau
- *[#177](https://github.com/idealista/prom2teams/issues/177) Fixing unit tests when using Python <= 3.6* @dortegau
- *[#182](https://github.com/idealista/prom2teams/issues/182) Fix dependances versions; yaml-dev in docker container; updated pyyaml package* @ftsao

## [2.5.4](https://github.com/idealista/prom2teams/tree/2.5.4)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.3...2.5.4)
## Fixed
- *[#162](https://github.com/idealista/prom2teams/issues/162) Fix werkzeug version to 0.16.1 (1.0.0 breaks current prom2teams version)* @frantsao

## [2.5.3](https://github.com/idealista/prom2teams/tree/2.5.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.2...2.5.3)
## Fixed
- *[#138](https://github.com/idealista/prom2teams/issues/138) Add ExtraAnnotations field extraction* @Aaron-ML

## [2.5.2](https://github.com/idealista/prom2teams/tree/2.5.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.1...2.5.2)
## Fixed
- *[#151](https://github.com/idealista/prom2teams/issues/151) Favicon not included in source distribution* @miguel-chacon
## Added
- *Log full message on error* @miguel-chacon

## [2.5.1](https://github.com/idealista/prom2teams/tree/2.5.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.5.0...2.5.1)
## Added
- *[#148](https://github.com/idealista/prom2teams/issues/148) Adapt template changes in Alertmanager 0.19* @miguel-chacon
## Fixed
- *[#146](https://github.com/idealista/prom2teams/issues/146) Missing 'job' label* @miguel-chacon
- *[#144](https://github.com/idealista/prom2teams/issues/144) Fix PyPI deploy* @miguel-chacon

## [2.5.0](https://github.com/idealista/prom2teams/tree/2.5.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.4.0...2.5.0)
## Added
- *[#109](https://github.com/idealista/prom2teams/issues/109) Add Helm chart* @Aaron-ML
## Fixed
- *[#139](https://github.com/idealista/prom2teams/issues/139) Add route for favicon* @miguel-chacon
- *Missing internal errors in flask exporter metrics* @miguel-chacon
## Changed
- *Minor improve Dockerfile* @miguel-chacon

## [2.4.0](https://github.com/idealista/prom2teams/tree/2.4.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.3.3...2.4.0)
## Added
- *[#104](https://github.com/idealista/prom2teams/issues/104) Add ability to reload config without restarting* @jnogol @miguel-chacon
- *[#129](https://github.com/idealista/prom2teams/issues/129) Add prometheus_flask_exporter* @jnogol
## Changed
- *[#128](https://github.com/idealista/prom2teams/pull/128) Allow overriding the config file location in Docker by setting the APP_CONFIG_FILE environment variable* @nvx

## [2.3.3](https://github.com/idealista/prom2teams/tree/2.3.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.3.2...2.3.3)
## Fixed
- *[#125](https://github.com/idealista/prom2teams/issues/125) Wrong type in labels_excluded* @miguel-chacon

## [2.3.2](https://github.com/idealista/prom2teams/tree/2.3.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.3.1...2.3.2)
## Fixed
- *[#122](https://github.com/idealista/prom2teams/issues/122) Date parsing exception* @miguel-chacon

## [2.3.1](https://github.com/idealista/prom2teams/tree/2.3.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.3.0...2.3.1)
## Changed
- *[#112](https://github.com/idealista/prom2teams/issues/112) Allow custom labels in jinja template* @miguel-chacon
- *[#110](https://github.com/idealista/prom2teams/pull/110) Using Alpine Linux instead of Debian Slim in Docker Image* @dortegau
- *Update flask-restplus version to v0.12.1* @miguel-chacon
- *Update marshmallow version to v3.0.0rc6* @miguel-chacon
## Fixed
- *Pypi package deployment* @miguel-chacon

## [2.3.0](https://github.com/idealista/prom2teams/tree/2.3.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.2.3...2.3.0)
## Changed
- *[#102](https://github.com/idealista/prom2teams/pull/102) Requests update* @manuhortet
## Fixed
- *[#105](https://github.com/idealista/prom2teams/issues/105) marshmallow.exceptions.ValidationError* @gjermy

## [2.2.3](https://github.com/idealista/prom2teams/tree/2.2.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.2.2...2.2.3)
## Changed
- *[#99](https://github.com/idealista/prom2teams/pull/99) Marshmallow update* @manuhortet

## [2.2.2](https://github.com/idealista/prom2teams/tree/2.2.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.2.1...2.2.2)
## Added
- *[#94](https://github.com/idealista/prom2teams/pull/94) Always group by status* @manuhortet

## [2.2.1](https://github.com/idealista/prom2teams/tree/2.2.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.1.2...2.2.1)
## Added
- *[#80](https://github.com/idealista/prom2teams/pull/79) Add the possibility of group alerts by alertname* @manuhortet
- *[#84](https://github.com/idealista/prom2teams/issues/84) View received message when debugging* @jnogol
- *Update Flask version to v1.0.2* @manuhortet @jnogol

## Changed
- *[#92](https://github.com/idealista/prom2teams/pull/92) Docker image now install from sources* @jnogol

## [2.1.2](https://github.com/idealista/prom2teams/tree/2.1.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.1.1...2.1.2)
### Fixed
- *[#70](https://github.com/idealista/prom2teams/pull/70) Fix condition in teams_client.py* @Gkrlo

## [2.1.1](https://github.com/idealista/prom2teams/tree/2.1.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.0.4...2.1.1)
### Added
- *[#70](https://github.com/idealista/prom2teams/pull/70) Check the Teams's response "text" attribute ='1' for validating a message was sent correctly* @Gkrlo
- *[#69](https://github.com/idealista/prom2teams/issues/69) Add resolved to notifications* @jnogol

## [2.0.4](https://github.com/idealista/prom2teams/tree/2.0.4)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.0.3...2.0.4)
### Fixed
- *[#65](https://github.com/idealista/prom2teams/pull/65) Delete pip usage in setup.py due to pip 10 incompatibilities* @jnogol

## [2.0.3](https://github.com/idealista/prom2teams/tree/2.0.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.0.2...2.0.3)
### Fixed
- *[#61](https://github.com/idealista/prom2teams/pull/63) Fix getting 404 errors - SERVER_NAME removed from flask app* @Gkrlo

## [2.0.2](https://github.com/idealista/prom2teams/tree/2.0.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.0.1...2.0.2)
### Fixed
- *[#57](https://github.com/idealista/prom2teams/pull/57) added conversion to int for PORT* @a-zen

## [2.0.1](https://github.com/idealista/prom2teams/tree/2.0.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.0.0...2.0.1)
### Fixed
- *[#53](https://github.com/idealista/prom2teams/issues/53) Fix prom2teams uwsgi bin startup* @jmonterrubio

## [2.0.0](https://github.com/idealista/prom2teams/tree/2.0.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.3.0...2.0.0)
### Added
- *[#49](https://github.com/idealista/prom2teams/issues/49) Update service startup for production environment* @jmonterrubio
- *[#22](https://github.com/idealista/prom2teams/issues/22) Allow to configure multiple connectors* @manuhortet @Gkrlo

## [1.3.0](https://github.com/idealista/prom2teams/tree/1.3.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.2.0...1.3.0)
### Added
- *[#32](https://github.com/idealista/prom2teams/issues/32) Support alerts with missing mandatory attributes* @lindhor
- *[#38](https://github.com/idealista/prom2teams/issues/38) Dockerfile* @jnogol

## [1.2.0](https://github.com/idealista/prom2teams/tree/1.2.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.1.3...1.2.0)
### Added
- *[#32](https://github.com/idealista/prom2teams/issues/32) Set default value for "instance" in alerts* @maglo

### Fixed
- *[#26](https://github.com/idealista/prom2teams/issues/26) Able to handle multiple received alerts* @jnogol

## [1.1.3](https://github.com/idealista/prom2teams/tree/1.1.3)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.1.2...1.1.3)
### Fixed
- *[#21](https://github.com/idealista/prom2teams/issues/21) Made some JSON fields optional, avoiding later crashes* @jnogol
- *[#23](https://github.com/idealista/prom2teams/issues/23) Deleted redundant log message* @jnogol
- *[#27](https://github.com/idealista/prom2teams/issues/27) Automatic deploy to PyPi via Travis* @jnogol

## [1.1.2](https://github.com/idealista/prom2teams/tree/1.1.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.1.1...1.1.2)
### Fixed
- *[#15](https://github.com/idealista/prom2teams/issues/18) Allow to be installed under Python 3.5.x* @dortegau

## [1.1.1](https://github.com/idealista/prom2teams/tree/1.1.1)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.1.0...1.1.1)
### Fixed
- *[#15](https://github.com/idealista/prom2teams/issues/15) Fixing setuptools config and packaging (broken in versions 1.1.0 and 1.0.0)* @dortegau

## [1.1.0](https://github.com/idealista/prom2teams/tree/1.1.0)
[Full Changelog](https://github.com/idealista/prom2teams/compare/1.0.0...1.1.0)
### Added
- *[#5](https://github.com/idealista/prom2teams/issues/5) Allow to provide log file path and log level as arguments* @dortegau

### Fixed
- *[#6](https://github.com/idealista/prom2teams/issues/6) Allow to define previously declared default values as blank values in provided config* @dortegau
- *[#8](https://github.com/idealista/prom2teams/issues/8) Closing all file descriptors and adding some unit tests* @dortegau
- *[#10](https://github.com/idealista/prom2teams/issues/10) Capturing Keyboard Interrupt and logging server stop event* @dortegau

## [1.0.0](https://github.com/idealista/prom2teams/tree/1.0.0)
### Added
- *First release* @jnogol @jmonterrubio @dortegau @juanriaza
