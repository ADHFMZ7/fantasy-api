import os
from typing import Annotated
from psycopg import AsyncConnection 
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends


load_dotenv()
conn_string = os.getenv("POSTGRES_CONN_STRING")

if not conn_string:
    print("POSTGRES_CONN_STRING env not set")
    exit()

pool = AsyncConnectionPool(conn_string, open=False)

@asynccontextmanager
async def lifespan(instance: FastAPI):
    await pool.open()
    yield
    await pool.close()


async def get_connection() -> AsyncConnection:
    async with pool.connection() as conn:
        yield conn

Connection = Annotated[AsyncConnection, Depends(get_connection)]
