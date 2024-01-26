import sqlalchemy
from sqlalchemy import Column, Integer

from db.db import base


class DayTableModel(base):
    """SqlAlchemy db model for dish."""

    __tablename__ = 'daytable'
    # id = Column(Integer, primary_key=True)
    table_number = Column(Integer, default=0, primary_key=True)
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        default=0, primary_key=True
    )
    row = Column(Integer, default=0, primary_key=True)
    title = Column(sqlalchemy.String)
    done = Column(sqlalchemy.String)
    time = Column(sqlalchemy.String)

    # def __repr__(self):
    #     print(self.title, self.user_id)
    #
    # def __str__(self):
    #     print(self.title, self.user_id)
