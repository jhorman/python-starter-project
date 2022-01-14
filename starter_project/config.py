from pydantic import BaseSettings


class CoreSettings(BaseSettings):
    api_keys: set[str] = set()

    class Config:
        env_prefix = ""
