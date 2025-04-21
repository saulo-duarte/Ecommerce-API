from logging.config import fileConfig
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool
from alembic import context
from app.configs.database import get_settings, Base
from app.models import *

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata
database_url = str(get_settings().database_url)

def run_migrations_offline():
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = async_engine_from_config(
        {"sqlalchemy.url": database_url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    async with connectable.connect() as connection:
        await connection.run_sync(
            lambda conn: context.configure(
                connection=conn,
                target_metadata=target_metadata,
                compare_type=True,
            )
        )
        async with connection.begin():
            await connection.run_sync(lambda conn: context.run_migrations())

def run():
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        import asyncio
        asyncio.run(run_migrations_online())

run()
