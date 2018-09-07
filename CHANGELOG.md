# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/prom2teams/tree/develop)

## [2.2.0](https://github.com/idealista/prom2teams/tree/2.2.0)
[Full changelog](https://github.com/idealista/prom2teams/compare/2.1.2...2.2.0)
## Added
- *[#80](https://github.com/idealista/prom2teams/pull/79) Add the possibility of group alarms by alertname * @manuhortet

## [2.1.2](https://github.com/idealista/prom2teams/tree/2.1.2)
[Full Changelog](https://github.com/idealista/prom2teams/compare/2.1.1...2.1.2)
### Fixed
- *[#70](https://github.com/idealista/prom2teams/pull/70) Fix condition in teams_client.py * @Gkrlo

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
- *[#26](https://github.com/idealista/prom2teams/issues/26) Able to handle multiple received alarms* @jnogol

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
