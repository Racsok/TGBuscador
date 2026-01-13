#!/usr/bin/env python3
from configuracion import config
from utils.logger import config_logger 
from pyrogram.client import Client
from pyrogram import filters

logger = config_logger(__name__)


class TGBuscador:
    def __init__(self) -> None:
        plugins = dict(root="manejadores")
        # self.user = Client("TGBuscador", api_id=config.api_id, api_hash=config.api_hash)
        self.bot = Client("TGBuscador", api_id=config.api_id, api_hash=config.api_hash, bot_token=config.bot_token, plugins=plugins)

    def run(self):
        logger.info("Aplicación iniciando")
        self.bot.run()
        # self.user.run()


    # def prueba(self):
    #     @Client.on_message(filters.command("start") & filters.private)
    #     async def start_privado(client, message):
    #         await message.send_message(f"Hola {message.from_user.first_name}, este es un chat privado.")

if __name__ == "__main__":
    bot = TGBuscador()
    logger.info("Aplicación iniciada")
    bot.run()

