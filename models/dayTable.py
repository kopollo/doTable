import sqlalchemy

from src.db import base


class DayTableModel(base):
    """SqlAlchemy db model for dish."""

    __tablename__ = 'daytable'

    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        default=0,
    )
    title = sqlalchemy.Column(sqlalchemy.String)
    done = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.String)
