import click
from flask import Blueprint

from db import create_db, drop_db

cli_bp = Blueprint("commands", __name__)


@cli_bp.cli.commands("init_db")
@click.option("-name", default="noname")
def init_db(name):
    # занести в переменные окружения навзщания name
    drop_db()
    create_db()
