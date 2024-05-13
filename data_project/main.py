import os
from datetime import datetime

import click
from dotenv import load_dotenv

from data_project.helpers.helpers import *

load_dotenv()

__version__ = os.getenv("VERSION")
API_BASE = os.getenv("API_BASE")
BASE_PATH = os.getcwd()
OUTPUT_PATH = os.path.join(BASE_PATH, os.getenv("DATA_PATH"))


def datetime_valid(ctx, param, value):
    """Date in ISO Format Validation"""
    try:
        # Validation required because --date_end is not a required option
        if value:
            date = datetime.fromisoformat(value)
            return date.strftime("%d-%m-%Y")
        else:
            return None
    except ValueError:
        click.BadParameter("date must be in ISO8601 format")


@click.command()
@click.option(
    "--date",
    required=False,
    type=str,
    callback=datetime_valid,
    help="ISO8601 format date",
)
@click.version_option(__version__)
@click.option("--coin_id", type=str, required=False)
def main(date, coin_id):
    if not (date and coin_id):
        click.echo(f"Hello!")
        click.echo(f"{API_BASE}")

    else:
        # Extract
        url = generate_url(API_BASE, coin_id, date)
        data = downloaw_asset(url)

        dir = os.path.join(OUTPUT_PATH, f"{coin_id}-{date}.json")
        # Load
        load_data(dir, data)


if __name__ == "__main__":
    main()
