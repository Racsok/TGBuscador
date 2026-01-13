from pyrogram.client import Client 
from pyrogram import filters

from utils.logger import config_logger 

logger =config_logger(__name__)

@Client.on_message(filters.command("start") & filters.private)
async def start_privado(client, message):
    logger.info("Respondiendo al comando /start")
    await client.send_message(
            chat_id=message.chat.id,
            text=f"🔍 Este es un motor de búsqueda de recursos de Telegram. Envía palabras clave para encontrar grupos, canales, videos, música, para opciones de o conocer sobre el bot escribe /help"
            )

