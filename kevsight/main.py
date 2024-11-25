import argparse
import pytz  # type: ignore[import-untyped]
from datetime import date, datetime
from dateutil.relativedelta import relativedelta  # type: ignore[import-untyped]

from cisa_kev.client import Catalog, Client, Query
from pyvulnerabilitylookup import PyVulnerabilityLookup

from kevsight import config


client = Client(path=config.catalog_path)
vuln_lookup = PyVulnerabilityLookup(
    config.vulnerability_lookup_base_url, token=config.vulnerability_auth_token
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="KEVSight",
        description="",
    )
    parser.add_argument(
        "--since",
        default=2,
        help="Specify the number of days from today to include in the query.",
    )

    arguments = parser.parse_args()

    catalog_version = client.get_catalog().version

    date_since = date.today() - relativedelta(days=int(arguments.since))
    query = Query(min_date_added=date_since)

    for vulnerability in client.get_catalog(query):
        # Create the sighting
        datetime_obj = datetime.combine(vulnerability.date_added, datetime.min.time())
        utc_aware_datetime = datetime_obj.replace(tzinfo=pytz.UTC)
        sighting = {
            "source": f"CISA-KEV-Version:{catalog_version}",
            "vulnerability": vulnerability.cve_id,
            "type": config.sighthing_type,
            "creation_timestamp": utc_aware_datetime,
        }

        # Post the JSON to Vulnerability Lookup
        try:
            r = vuln_lookup.create_sighting(sighting=sighting)
            if "message" in r:
                print(r["message"])
        except Exception as e:
            print(
                f"Error when sending POST request to the Vulnerability Lookup server:\n{e}"
            )


if __name__ == "__main__":
    # Point of entry in execution mode.
    main()
