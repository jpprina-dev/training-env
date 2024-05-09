from click.testing import CliRunner
from data_project import main

def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ['--hello', 'Juan'])
    assert result.exit_code == 0
    assert result.output == 'Hello Juan!\n'
    
    
if __name__ == "__main__":
    test_hello_world()