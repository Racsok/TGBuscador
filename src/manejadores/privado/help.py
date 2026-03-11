from pyrogram.client import Client 
from pyrogram import filters

from utils.logger import config_logger 

logger = config_logger(__name__)

@Client.on_message(filters.command("help") & filters.private)
async def start_privado(client, message):
    logger.info("Respondiendo al comando /start")
    await client.send_message(
            chat_id=message.chat.id,
            text=f"Escribe una palabra y enviala, si quieres aportar en el desarrollo te dejo el link del repositorio de GitHub: [TGBuscador](https://github.com/Racsok/TGBuscador)"
            )
