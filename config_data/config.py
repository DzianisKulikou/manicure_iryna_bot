from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    channel_id: str       # id канала бьюти Варшава
    channel_id_na: str    # id канала барахолка Lodz
    my_id: str            # id мой
    ira_id: str           # id Иры
    admin_id: list        # id Мой и Иры


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('bot_token'),
                               channel_id=env('CHANNEL_ID'),
                               channel_id_na=env('CHANNEL_ID_NA'),
                               my_id=env('MY_ID'),
                               ira_id=env('IRA_ID'),
                               admin_id=env('ADMIN_ID')))
