from pydantic import BaseModel

class ResultCreate(BaseModel):
    user: str
    value: str

class ResultOut(ResultCreate):
    id: int

    class Config:
        orm_mode = True
