from pydantic import BaseModel


class DayTable(BaseModel):
    title: str
    done: str
    time: str
