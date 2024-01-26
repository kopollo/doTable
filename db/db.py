from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base

from config import DB_URL

engine = create_engine(DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
base: DeclarativeMeta = declarative_base()
base.query = db_session.query_property()  # whast is it?
from .models.dayTable import DayTableModel


def create_db():
    from .models import dayTable
    base.metadata.drop_all(bind=engine)
    base.metadata.create_all(bind=engine)
    db_session.commit()


def add_table(data: dict):
    from .models.dayTable import DayTableModel
    t = DayTableModel(**data)
    db_session.merge(t)
    db_session.commit()


def get_user_table(user_id: int) -> list[DayTableModel]:
    data: list[DayTableModel] = db_session.query(DayTableModel).filter(DayTableModel.user_id == user_id)
    # for i in data:
    #     print(i.user_id)
    # for table in result.scalars():
    #     print(f"{table.title} xxxxxx")
    # # data = result.scalars().all()
    # print(result.scalars())
    return data
