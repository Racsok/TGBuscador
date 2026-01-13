#!/usr/bin/env python

from pydantic_settings import BaseSettings, SettingsConfigDict
from utils.logger import config_logger

logger = config_logger(__name__)
class Configuracion(BaseSettings):
    # tipo de variables
    api_id: int
    api_hash: str
    bot_token: str

    # Lee el el archivo .env automaticamente
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8", extra="ignore")

# Se crea una instancia
config = Configuracion()
logger.info(f"{config.api_id}, {config.api_hash}, {config.bot_token}")
