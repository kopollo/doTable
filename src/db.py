from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base

from src.config import DB_URL


engine = create_engine(DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
base: DeclarativeMeta = declarative_base()
base.query = db_session.query_property()  # whast is it?


def create_db():
    # from models import
    base.metadata.create_all(bind=engine)


def drop_db():
    base.metadata.drop_all(bind=engine)


def add(data: dict):
    from models.dayTable import DayTableModel
    t = DayTableModel(**data)
    db_session.merge(t)
    db_session.commit()

