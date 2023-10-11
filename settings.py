from envparse import Env
from loguru import logger


env = Env()
env.read_envfile(".env")

DB_USER = env.str("DB_USER", default="postgres")
DB_PASS = env.str("DB_PASS", default="postgres")
DB_NAME = env.str("DB_NAME", default="postgres")
DB_HOST = env.str("DB_HOST", default="localhost")
APP_PORT = env.int("APP_PORT", default=8000)
APP_HOST = env.str("APP_HOST", default="0.0.0.0")
APP_RELOAD = env.bool("APP_RELOAD", default=True)


REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)


LOGER = logger
LOGER.add(
    "logs/logs.log",
    rotation="10 KB",
    format="{time} {level} {message}",
    level="ERROR"
)

