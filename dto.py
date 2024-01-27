from pydantic import BaseModel


class DayTableDTO(BaseModel):
    title: str
    done: str
    time: str
    user_id: int
    row: int
    table_number: int
