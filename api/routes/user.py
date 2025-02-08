from fastapi import APIRouter, Depends, HTTPException
from psycopg.rows import class_row
from models import User
from db import get_connection
from psycopg import AsyncConnection

router = APIRouter(
    prefix="/users"
)

@router.post("/")
async def create_user(user_form: User, conn: AsyncConnection = Depends(get_connection)):

    await conn.execute("INSERT INTO users (id, username, email) VALUES (%s, %s, %s)", 
                       (user_form.id, user_form.username, user_form.email))

    await conn.commit()
    return {"Response": "Successfully created user"} 
    # error checking later

@router.get("/{user_id}")
async def get_user(user_id: str, conn: AsyncConnection = Depends(get_connection)) -> User:
   
    cursor = conn.cursor(row_factory=class_row(User))

    user = await cursor.execute("SELECT * FROM users WHERE id = %s", (user_id))
    if not (user := await user.fetchone()):
        raise HTTPException(status_code=404, detail="User not found") 
    return user

@router.delete("/{user_id}")
async def delete_user(user_id):
    pass

