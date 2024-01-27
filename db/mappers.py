from sqlalchemy import inspect
from .models.dayTable import DayTableModel
from dto import DayTableDTO


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


class DayTableMapper:
    @staticmethod
    def to_sqlalchemy(table: DayTableDTO) -> DayTableModel:
        return DayTableModel(**table.model_dump())

    @staticmethod
    def to_dto(model: DayTableModel) -> DayTableDTO:
        if model is None:
            return None
        return DayTableDTO.model_validate(object_as_dict(model))
