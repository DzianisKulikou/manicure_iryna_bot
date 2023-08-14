from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    channel_id: str       # id канала бьюти
    channel_id_na: str    # id канала наша

@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('bot_token'),
                               channel_id=env('CHANNEL_ID'),
                               channel_id_na=env('CHANNEL_ID_NA')))
