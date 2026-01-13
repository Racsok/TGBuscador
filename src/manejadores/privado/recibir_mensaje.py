# Seccion para recibir el mensjae y enviar la respuesta
from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.logger import config_logger

logger = config_logger(__name__)


# Responder mensaje ignorando los comando start y help
@Client.on_message(filters.text & filters.private & ~filters.command(["start", "help"]))
async def buscar_contenido(client, message):
    palabra_clave = message.text
    
    # Aquí simularemos resultados (después conectarás tu BD)
    resultados = generar_resultados_ejemplo(palabra_clave)
    
    # Crear el texto de respuesta
    texto_respuesta = f"🔍 Resultados para: **{palabra_clave}**\n\n"
    texto_respuesta += "📂 **Recursos encontrados:**\n\n"
    
    for i, resultado in enumerate(resultados, 1):
        emoji = obtener_emoji_tipo(resultado['tipo'])
        texto_respuesta += f"{emoji} **{i}.** [{resultado['titulo']}]({resultado['url']})\n"
        texto_respuesta += f"   📊 {resultado['estadisticas']}\n\n"
    
    # Crear los botones de filtro
    botones = crear_botones_filtro(palabra_clave)
    
    # Enviar mensaje con botones
    logger.info(f"Respondiendo al mensaje con palabra clave: {palabra_clave}")
    await message.reply_text(
        text=texto_respuesta,
        reply_markup=botones,
        disable_web_page_preview=True
    )



# Resultado de ejemplo
def generar_resultados_ejemplo(palabra_clave):
    resultados = [
        {
            'titulo': f'Canal de {palabra_clave} - Contenido Premium',
            'url': 'https://t.me/ejemplo1',
            'tipo': 'canal',
            'estadisticas': '👥 15K miembros | 📝 500 publicaciones'
        },
        {
            'titulo': f'Grupo de {palabra_clave} - Comunidad Activa',
            'url': 'https://t.me/ejemplo2',
            'tipo': 'grupo',
            'estadisticas': '👥 8K miembros | 💬 Muy activo'
        },
        {
            'titulo': f'Videos de {palabra_clave} [HD]',
            'url': 'https://t.me/ejemplo3',
            'tipo': 'video',
            'estadisticas': '🎬 2.5K videos | ⭐ Alta calidad'
        },
        {
            'titulo': f'Música {palabra_clave} - Colección Completa',
            'url': 'https://t.me/ejemplo4',
            'tipo': 'musica',
            'estadisticas': '🎵 1.8K canciones | 320kbps'
        },
        {
            'titulo': f'Documentos y PDFs de {palabra_clave}',
            'url': 'https://t.me/ejemplo5',
            'tipo': 'documento',
            'estadisticas': '📄 500 documentos | PDF/EPUB'
        },
        {
            'titulo': f'Curso de {palabra_clave} - Completo',
            'url': 'https://t.me/ejemplo6',
            'tipo': 'curso',
            'estadisticas': '🎓 25 módulos | Certificado'
        },
        {
            'titulo': f'Software y Apps de {palabra_clave}',
            'url': 'https://t.me/ejemplo7',
            'tipo': 'software',
            'estadisticas': '💾 150 apps | Actualizado'
        },  
        {
            'titulo': f'Stickers y GIFs de {palabra_clave}',
            'url': 'https://t.me/ejemplo8',
            'tipo': 'sticker',
            'estadisticas': '🎨 50 packs | Animados'
        },
        {
            'titulo': f'Noticias de {palabra_clave} - Diarias',
            'url': 'https://t.me/ejemplo9',
            'tipo': 'noticias',
            'estadisticas': '📰 Actualización diaria'
        },
        {
            'titulo': f'{palabra_clave} - Recursos Variados',
            'url': 'https://t.me/ejemplo10',
            'tipo': 'mixto',
            'estadisticas': '📦 Contenido variado | 3K archivos'
        }
    ]
    return resultados

def obtener_emoji_tipo(tipo):
    emojis = {
        'canal': '📢',
        'grupo': '👥',
        'video': '🎬',
        'musica': '🎵',
        'documento': '📄',
        'curso': '🎓',
        'software': '💾',
        'sticker': '🎨',
        'noticias': '📰',
        'mixto': '📦'
    }
    return emojis.get(tipo, '📌')

# Funcion para crera los botones de categorizacion
def crear_botones_filtro(palabra_clave):
    botones = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎬 Videos", callback_data=f"filtro_video_{palabra_clave}"),
            InlineKeyboardButton("🎵 Música", callback_data=f"filtro_musica_{palabra_clave}"),
            InlineKeyboardButton("📄 Docs", callback_data=f"filtro_doc_{palabra_clave}")
        ],
        [
            InlineKeyboardButton("📢 Canales", callback_data=f"filtro_canal_{palabra_clave}"),
            InlineKeyboardButton("👥 Grupos", callback_data=f"filtro_grupo_{palabra_clave}"),
            InlineKeyboardButton("🎓 Cursos", callback_data=f"filtro_curso_{palabra_clave}")
        ],
        [
            InlineKeyboardButton("🔄 Actualizar", callback_data=f"actualizar_{palabra_clave}"),
            InlineKeyboardButton("❌ Limpiar", callback_data="limpiar")
        ],
        [
            InlineKeyboardButton("⬅️ Anterior", callback_data=f"pag_anterior_{palabra_clave}_1"),
            InlineKeyboardButton("1/5", callback_data="pagina_actual"),
            InlineKeyboardButton("Siguiente ➡️", callback_data=f"pag_siguiente_{palabra_clave}_1")
        ]
    ])
    return botones

# Maneja las funcionlidades de los botones de categorizacion
@Client.on_callback_query()
async def manejar_botones(client, callback_query):
    data = callback_query.data
    
    if data.startswith("filtro_"):
        # Extraer tipo de filtro y palabra clave
        partes = data.split("_", 2)
        tipo_filtro = partes[1]
        palabra_clave = partes[2] if len(partes) > 2 else ""
        
        await callback_query.answer(f"🔍 Filtrando por {tipo_filtro}...", show_alert=False)
        
        # Aquí filtrarías los resultados según el tipo
        texto_filtrado = f"🔍 Resultados de **{tipo_filtro}** para: **{palabra_clave}**\n\n"
        texto_filtrado += f"📌 Mostrando solo contenido tipo: {tipo_filtro}\n\n"
        texto_filtrado += "_(En tu implementación real, aquí irían los resultados filtrados de la BD)_"
        
        await callback_query.edit_message_text(
            text=texto_filtrado,
            reply_markup=crear_botones_filtro(palabra_clave)
        )
    
    elif data.startswith("actualizar_"):
        palabra_clave = data.replace("actualizar_", "")
        await callback_query.answer("🔄 Actualizando resultados...", show_alert=False)
        # Recargar resultados
        
    elif data == "limpiar":
        await callback_query.answer("✅ Búsqueda limpiada", show_alert=False)
        await callback_query.edit_message_text(
            "🔍 Búsqueda limpiada. Envía una nueva palabra clave para buscar."
        )
    
    elif data.startswith("pag_"):
        # Manejar navegación de páginas
        await callback_query.answer("📄 Cambiando página...", show_alert=False)
        # Implementar lógica de paginación
    
    elif data == "pagina_actual":
        await callback_query.answer("📍 Estás en esta página", show_alert=False)
