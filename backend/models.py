from pydantic import BaseModel, Field


class User(BaseModel):
    login : str = Field(...)
    password : str = Field(...)
