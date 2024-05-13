import os

from click.testing import CliRunner
from dotenv import load_dotenv

from data_project.main import main

load_dotenv()

CLI_VERSION = os.getenv("CLI_VERSION")


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"main, version {CLI_VERSION}\n"


if __name__ == "__main__":
    test_version()
