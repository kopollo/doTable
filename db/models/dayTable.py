import sqlalchemy
from sqlalchemy import Column, Integer

from db.db import base


class DayTableModel(base):
    """SqlAlchemy db model for dish."""

    __tablename__ = 'daytable'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        default=0,
    )
    title = Column(sqlalchemy.String)
    done = Column(sqlalchemy.String)
    time = Column(sqlalchemy.String)
