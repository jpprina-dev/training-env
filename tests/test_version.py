from click.testing import CliRunner

from data_project import main


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert result.output == "main, version 0.1.0\n"


if __name__ == "__main__":
    test_version()
