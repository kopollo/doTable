import click
from flask import Blueprint

from db.db import create_db

cli_bp = Blueprint("commands", __name__)


@cli_bp.cli.command("init_db")
@click.option("-name", default="noname")
def init_db(name):
    # занести в переменные окружения навзщания name
    create_db()


@cli_bp.cli.command("hello")
@click.option("--name", default="World")
def hello_command(name):
    click.echo(f"Hello, {name}!")
