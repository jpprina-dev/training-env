from datetime import datetime

import click


def datetime_valid(ctx, param, value):
    """Date in ISO Format Validation"""
    try:
        # Validation required because --date_end is not a required option
        if value:
            date = datetime.fromisoformat(value)
            return date
        else:
            return None
    except ValueError:
        click.BadParameter("date must be in ISO8601 format")


@click.command()
@click.option("--hello", prompt=True)
# @click.option(
#     "--date",
#     required=True,
#     type=str,
#     callback=datetime_valid,
#     help="ISO8601 format date",
# )
@click.version_option()
# @click.argument("coin_id")
def main(hello):
    if hello:
        click.echo(f"Hello {hello}!")


if __name__ == "__main__":
    main()
