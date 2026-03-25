"""Command-line interface for my_package."""

import click

from my_package import __version__
from my_package.core import greet


@click.group()
@click.version_option(version=__version__, prog_name="my-package")
def main() -> None:
    """My package — a sample CLI application."""


@main.command()
@click.argument("name", default="World")
def hello(name: str) -> None:
    """Greet someone by name."""
    click.echo(greet(name))


if __name__ == "__main__":
    main()
