import psycopg
from psycopg import AsyncConnection 
from psycopg_pool import AsyncConnectionPool

conn_string = "postgresql://ahmad:ahmad@localhost:5432/ahmad"
pool = AsyncConnectionPool(conn_string, open=False)

async def get_connection() -> AsyncConnection:
    async with pool.connection() as conn:
        yield conn

