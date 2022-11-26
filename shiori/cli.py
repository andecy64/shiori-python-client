"""Console script for shiori."""
import sys
import os
from pathlib import PosixPath
import json

import click
from .shiori import ShioriClient
from .models import ShioriConfig


def get_default_shiori_config_dir():
    home_dir = os.getenv("HOME")
    path = PosixPath(home_dir) / ".config/shiori"
    return path


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option("--config-dir", "-c", default=get_default_shiori_config_dir())
@click.pass_context
def cli(ctx, debug, config_dir,):
    with open(config_dir / "config.json", "r") as config_file:
        config = ShioriConfig(**json.loads(config_file.read()))

    client = ShioriClient(
            base_url=config.base_url,
            username=config.username,
            password=config.password)

    ctx.ensure_object(dict)
    ctx.obj["CLIENT"] = client


@cli.command()
@click.pass_context
def get_bookmarks(ctx):
    click.echo(ctx.obj["CLIENT"].get_bookmarks().json(indent=2))
    return 0


def main():
    cli(auto_envvar_prefix="SHIORI")


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
