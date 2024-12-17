from datetime import datetime

from pydantic import BaseModel


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class AuthorOut(AuthorBase):
    id: int

    class ConfigDict:
        from_attributes = True
