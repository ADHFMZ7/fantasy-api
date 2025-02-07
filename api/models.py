from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MyTable(BaseModel):
    id: int = Field(..., description="Primary key for the record")
    name: str = Field(..., max_length=255, description="Name (up to 255 characters)")
    created_at: Optional[datetime] = Field(
        None, description="Timestamp when the record was created. Defaults to CURRENT_TIMESTAMP in the DB."
    )

class User(BaseModel):
    ...

class League(BaseModel):
    ...

class Player(BaseModel):
    ...

class Team(BaseModel):
    ...

class Match(BaseModel):
    ...


