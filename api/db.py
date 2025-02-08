import os
import psycopg
from psycopg import AsyncConnection 
from psycopg_pool import AsyncConnectionPool
from dotenv import load_dotenv

load_dotenv()
conn_string = os.getenv("POSTGRES_CONN_STRING")

if not conn_string:
    print("POSTGRES_CONN_STRING env not set")
    exit()

pool = AsyncConnectionPool(conn_string, open=False)

async def get_connection() -> AsyncConnection:
    async with pool.connection() as conn:
        yield conn

