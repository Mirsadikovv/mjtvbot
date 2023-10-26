# from data import config

from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool


from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

DB_USER = env.str("DP_USER")
DB_PASS = env.str("DP_PASS")
DB_NAME = env.str("DP_NAME")
DB_HOST = env.str("DP_HOST")



class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        reg_time timestamp NOT NULL,
        phone VARCHAR(255) NULL,
        status VARCHAR(255) NULL,
        subscription_date timestamp NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id, reg_time) VALUES($1, $2, $3, CURRENT_TIMESTAMP) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    
    async def select_current_time(self):
        sql = "SELECT CURRENT_TIMESTAMP"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_user_status(self, **kwargs):
        sql = "SELECT status FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_user_phone(self, **kwargs):
        sql = "SELECT phone FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)
    
    async def select_user_status_endtime(self, **kwargs):
        sql = "SELECT subscription_date + INTERVAL '1 month' FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)
    
    async def update_user_phone(self, phone, telegram_id):
        sql = "UPDATE Users SET phone=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone, telegram_id, execute=True)
    
    async def update_user_status(self,status, telegram_id):
        sql = "UPDATE Users SET status=$1 WHERE telegram_id=$2"
        return await self.execute(sql, status, telegram_id, execute=True)
    
    async def update_user_endtime(self, telegram_id):
        sql = "UPDATE Users SET subscription_date=None WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, execute=True)
    
    async def update_user_status_date(self, telegram_id):
        sql = "UPDATE Users SET subscription_date=CURRENT_TIMESTAMP WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    # async def drop_users(self):
    #         await self.execute("DROP TABLE Users", execute=True)
            