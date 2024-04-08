# app/schemas.py
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    address: dict

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 20,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }

class StudentUpdate(BaseModel):
    name: str = None
    age: int = None
    address: dict = None
