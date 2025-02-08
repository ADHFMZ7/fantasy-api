from pydantic import BaseModel, EmailStr, Field, UUID4
from typing import List, Optional
from datetime import datetime
from uuid import uuid4

class MyTable(BaseModel):
    id: int = Field(..., description="Primary key for the record")
    name: str = Field(..., max_length=255, description="Name (up to 255 characters)")
    created_at: Optional[datetime] = Field(
        None, description="Timestamp when the record was created. Defaults to CURRENT_TIMESTAMP in the DB."
    )


class League(BaseModel):
    ...


class User(BaseModel):
    id: UUID4 = Field(default_factory=uuid4, description="Primary key for the user")
    email: EmailStr
    username: str = Field(..., max_length=64, description="Name (up to 64 characters)")
    # leagues: List[League] = Field()
    created_at: Optional[datetime] = Field (
        None, description="Teimstamp when the user was craeted. Defaults to CURRENT_TIMESTAMP in the DB"
    )
    

class Player(BaseModel):
    ...

class Team(BaseModel):
    ...

class Match(BaseModel):
    ...


