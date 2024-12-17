from pydantic import BaseModel
from datetime import date

class BorrowBase(BaseModel):
    book_id: int
    readers_name: str
    issue_date: date


class BorrowCreate(BorrowBase):
    pass


class BorrowUpdate(BaseModel):
    return_date: date


class BorrowOut(BorrowBase):
    id: int
    return_date: date | None

    class ConfigDict:
        from_attributes = True
