# KEVSight

A client to generate sightings for
[Vulnerability-Lookup](https://github.com/cve-search/vulnerability-lookup) from the
[Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
catalog.


## Installation

[pipx](https://github.com/pypa/pipx) is an easy way to install and run Python applications in isolated environments.
It's easy to [install](https://github.com/pypa/pipx?tab=readme-ov-file#on-linux).

```bash
$ pipx install KEVSight
$ export KEVSight_CONFIG=~/.KEVSight/conf.py
$ cisa_kev --download-path /home/cedric/.cisa_kev/known_exploited_vulnerabilities.json  download
```

The configuration for KEVSight should be defined in a Python file (e.g., ``~/.KEVSight/conf.py``).
You must then set an environment variable (``KEVSight_CONFIG``) with the full path to this file.


## Usage

```bash
$ KEVSight --help
usage: KEVSight [-h] [--since SINCE]

options:
  -h, --help     show this help message and exit
  --since SINCE  Specify the number of days from today to include in the query
```



## License

[KEVSight](https://github.com/cedricbonhomme/KEVSight) is licensed under
[GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.html)

~~~
Copyright (c) 2024 Computer Incident Response Center Luxembourg (CIRCL)
Copyright (C) 2024 Cédric Bonhomme - https://github.com/cedricbonhomme
~~~
