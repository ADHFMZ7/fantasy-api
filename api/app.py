from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends 
from psycopg import AsyncConnection
from psycopg.rows import class_row
from db import pool, get_connection
from routes import user, league

from models import MyTable

@asynccontextmanager
async def lifespan(instance: FastAPI):
    await pool.open()
    yield
    await pool.close()


app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
# app.include_router(league.router)

@app.get("/")
async def root(conn: AsyncConnection = Depends(get_connection)):

    # cursor = conn.cursor(row_factory=class_row(MyTable))
    # a = await cursor.execute("select * from my_table;")
    # user = await a.fetchone()
    # print(type(user))

    return {"message": "Hello!"}
