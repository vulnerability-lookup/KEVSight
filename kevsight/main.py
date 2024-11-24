from datetime import date
from dateutil.relativedelta import relativedelta  # type: ignore[import-untyped]

from cisa_kev.client import Client, Query
from pyvulnerabilitylookup import PyVulnerabilityLookup

from kevsight import config


client = Client()


def push_sighting_to_vulnerability_lookup(source, vulnerability, creation_date):
    """Create a sighting from an incoming status and push it to the Vulnerability Lookup instance."""
    print("Pushing sighting to Vulnerability Lookup...")
    vuln_lookup = PyVulnerabilityLookup(
        config.vulnerability_lookup_base_url, token=config.vulnerability_auth_token
    )

    # Create the sighting
    sighting = {
        "type": config.sighthing_type,
        "source": f"source",
        "vulnerability": vulnerability,
        "creation_timestamp": creation_date,
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


def main():
    date_since = date.today() - relativedelta(days=3)
    query = Query(min_date_added=date_since)
    ct = client.get_catalog(query)
    for vulnerability in ct.vulnerabilities:
        print(vulnerability)


if __name__ == "__main__":
    main()
