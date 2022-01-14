from functools import lru_cache
from urllib.parse import urlparse

from pydantic import BaseSettings
from redis import Redis


class CoreSettings(BaseSettings):
    api_keys: set[str] = set()

    class Config:
        env_prefix = ""


class RedisSettings(BaseSettings):
    url: str = "redis://localhost:6379"

    class Config:
        env_prefix = "REDIS_"


class RedisConfig:
    def __init__(
        self,
        url_string: str = None,
        host: str = None,
        port: int = None,
        password: str = None,
        db: int = None,
        socket_timeout: int = 10,
        socket_connect_timeout: int = 10,
        health_check_interval: int = 30,
        decode_responses: bool = False,
    ):
        if not url_string and not (host and port and password) or url_string and (host or port or password):
            raise ValueError("Must either supply url_string OR host/port/password")

        if url_string:
            parsed_url_string = urlparse(url_string)
            host = parsed_url_string.hostname
            port = parsed_url_string.port
            password = parsed_url_string.password
            db = int(parsed_url_string.path.replace("/", "")) if parsed_url_string.path else 0

        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.socket_timeout = socket_timeout
        self.socket_connect_timeout = socket_connect_timeout
        self.health_check_interval = health_check_interval
        self.decode_responses = decode_responses


REDIS_CONFIG = RedisConfig(RedisSettings().url)


@lru_cache
def get_redis():
    return Redis(
        host=REDIS_CONFIG.host,
        port=REDIS_CONFIG.port,
        password=REDIS_CONFIG.password,
        db=REDIS_CONFIG.db,
        socket_timeout=REDIS_CONFIG.socket_timeout,
        socket_connect_timeout=REDIS_CONFIG.socket_connect_timeout,
        health_check_interval=REDIS_CONFIG.health_check_interval,
        ssl=True if REDIS_CONFIG.password else False,
        decode_responses=REDIS_CONFIG.decode_responses,
    )
