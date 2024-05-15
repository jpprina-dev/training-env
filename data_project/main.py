import logging
import os
from datetime import datetime

import click
from dotenv import load_dotenv

from data_project.helpers import downloaw_asset, generate_url, load_data

load_dotenv()

__version__ = os.getenv("CLI_VERSION")
API_BASE = os.getenv("API_BASE")
BASE_PATH = os.getcwd()
OUTPUT_PATH = os.path.join(BASE_PATH, os.getenv("DATA_PATH"))
LOG_LEVEL = os.getenv("LOG_LEVEL")

logging.basicConfig(format="%(asctime)s - %(message)s", level=LOG_LEVEL)
logger = logging.getLogger("main")


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
@click.argument("coin_id")
def main(date, coin_id):
    logger.info(f"Start processing {coin_id} for {date}")
    # Extract
    url = generate_url(API_BASE, coin_id, date)
    logger.info(f"Quering URL: {url}")
    data = downloaw_asset(url)

    # Load
    dir = os.path.join(OUTPUT_PATH, f"{coin_id}-{date}.json")
    logger.info(f"Saving data to {dir}")
    load_data(dir, data)


if __name__ == "__main__":
    main()
