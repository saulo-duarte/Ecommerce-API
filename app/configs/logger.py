import os
import sys
from importlib.util import find_spec
from typing import Any

from loguru import logger


def _use_rich() -> bool:
    return find_spec("rich") is not None


def _use_json() -> bool:
    return find_spec("pythonjsonlogger") is not None


def _json_formatter(record: dict[str, Any]) -> str:
    import json

    return json.dumps(
        {
            "time": record["time"].strftime("%Y-%m-%dT%H:%M:%S"),
            "level": record["level"].name,
            "module": record["module"],
            "message": record["message"],
        }
    )


def setup_logger() -> None:
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_format = os.getenv("LOG_FORMAT", "rich" if _use_rich() else "default").lower()

    logger.remove()

    if log_format == "json" and _use_json():
        logger.add(sys.stdout, level=log_level, format=_json_formatter)

    elif log_format == "rich" and _use_rich():
        import logging
        from rich.logging import RichHandler

        class InterceptHandler(logging.Handler):
            def emit(self, record: logging.LogRecord) -> None:
                logger_opt = logger.opt(depth=6, exception=record.exc_info)
                logger_opt.log(record.levelname, record.getMessage())

        logging.basicConfig(handlers=[RichHandler()], level=log_level, force=True)
        logging.getLogger().addHandler(InterceptHandler())

    else:
        logger.add(
            sys.stdout,
            level=log_level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
                   "<level>{level}</level> | "
                   "<cyan>{name}</cyan>: <level>{message}</level>",
        )


setup_logger()