"""Tests for my_package.cli."""

from click.testing import CliRunner

from my_package.cli import main

runner = CliRunner()


class TestCLI:
    def test_version_flag(self):
        result = runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "my-package" in result.output

    def test_hello_default(self):
        result = runner.invoke(main, ["hello"])
        assert result.exit_code == 0
        assert result.output.strip() == "Hello, World!"

    def test_hello_with_name(self):
        result = runner.invoke(main, ["hello", "Alice"])
        assert result.exit_code == 0
        assert result.output.strip() == "Hello, Alice!"
