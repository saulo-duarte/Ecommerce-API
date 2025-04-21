from functools import lru_cache
from typing import Any, AsyncGenerator, Optional, Self

from app.configs.logger import logger
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    database_url: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)


@lru_cache()
def get_settings() -> Settings:
    return Settings()


class Database:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.engine: Optional[AsyncEngine] = None
        self.session_maker: Optional[async_sessionmaker[AsyncSession]] = None

    def setup(self) -> Self:
        if not self.engine:
            database_url = str(self.settings.database_url)
            self.engine = create_async_engine(
                database_url,
                echo=False,
                future=True,
                pool_pre_ping=True,
                pool_size=5,
                max_overflow=10,
            )
            self.session_maker = async_sessionmaker(
                bind=self.engine, expire_on_commit=False, autoflush=False
            )
            logger.info("✅ Engine do banco de dados configurado com sucesso.")
        return self


db = Database().setup()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    if not db.session_maker:
        raise RuntimeError("❌ Database não foi configurado corretamente.")

    async with db.session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error(f"❗ Erro na sessão do banco de dados: {e}")
            raise
        finally:
            await session.close()


Base = declarative_base()
