from .models.dayTable import DayTableModel
from .mappers import DayTableMapper
from dto import DayTableDTO
from db.db import db_session


class DayTableRepository:
    @staticmethod
    def add(table: DayTableDTO) -> None:
        db_session.merge(DayTableMapper.to_sqlalchemy(table))
        db_session.commit()

    @staticmethod
    def get_all_records(user_id: int) -> list[DayTableDTO]:
        data: list[DayTableModel] = db_session.query(DayTableModel).filter(DayTableModel.user_id == user_id)
        return list(map(DayTableMapper.to_dto, data))
