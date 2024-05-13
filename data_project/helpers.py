import json

import requests


def generate_url(api_base: str, identifier: str, date_str: str) -> str:
    """Generate URL for the request"""
    url = api_base + f"/coins/{identifier}/history?date={date_str}"
    return url


def downloaw_asset(url: str) -> json:
    """Download coin asset"""
    with requests.get(url) as response:
        # Rise Error if failed
        response.raise_for_status()
        # Get response content as json
        return response.json()


def load_data(dir: str, data: json) -> None:
    # Save as json file
    with open(dir, "w") as f:
        json.dump(data, f, indent=4)
