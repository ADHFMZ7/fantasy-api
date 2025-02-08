from fastapi import APIRouter, Depends, HTTPException
from psycopg.rows import class_row
from models import User
from db import Connection 
from psycopg import AsyncConnection
from typing import List

router = APIRouter(
    prefix="/users"
)

@router.get("/")
async def get_users(conn: Connection) -> List[User]:
    cursor = conn.cursor(row_factory=class_row(User))

    users = await cursor.execute("SELECT * from users;")
    return await users.fetchall()
    

@router.post("/")
async def create_user(user_form: User, conn: Connection):

    await conn.execute("INSERT INTO users (id, username, email) VALUES (%s, %s, %s)", 
                       (user_form.id, user_form.username, user_form.email))

    await conn.commit()
    return {"Response": "Successfully created user"} 
    # error checking later

@router.get("/{user_id}")
async def get_user(user_id: str, conn: Connection) -> User:
   
    cursor = conn.cursor(row_factory=class_row(User))

    user = await cursor.execute("SELECT * FROM users WHERE id = %s", (user_id))
    if not (user := await user.fetchone()):
        raise HTTPException(status_code=404, detail="User not found") 
    return user

@router.delete("/{user_id}")
async def delete_user(user_id):
    pass

