import asyncio

from ... import *
from .buttons import *
from .wrapper import *
from pyrogram.types import *


async def help_menu_logo(answer):
    image = None
    if image:
        thumb_image = image
    else:
        thumb_image = "https://telegra.ph/file/4294541927ae4d497f121.jpg"
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="💫 ʜᴇʟᴘ ᴍᴇɴᴜ  ✨",
            thumb_url=f"{thumb_image}",
            description=f"🥀 Open Help Menu Of @II_4ST_READY_FOR_FUCKING_II ✨...",
            caption=f"""
            **💫 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏᴘ.
@II_4ST_READY_FOR_FUCKING_II ᴜsᴇʀʙᴏᴛ  » {__version__} ✨
 
❤️ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ
ɢᴇᴛ 4ST ᴜsᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ❤️
 
🌹ᴘᴏᴡᴇʀᴇᴅ ʙʏ ♡  [ 😻 #𝙸_𝙼_4𝚂𝚃_𝙵ʏᴛᴇʀ 👻 ](https://t.me/II_4ST_READY_FOR_FUCKING_II) 🌹**""",
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    from ... import __version__
    button = paginate_plugins(0, plugs, "help")
    answer.append(
        InlineQueryResultArticle(
            title="💫 ʜᴇʟᴘ ᴍᴇɴᴜ  ✨",
            input_message_content=InputTextMessageContent(f"""
            **💫 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏᴘ.
#_4ST ᴜsᴇʀʙᴏᴛ  » {__version__} ✨
 
❤️ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ
ɢᴇᴛ ᴜsᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ❤️
 
🌹ᴘᴏᴡᴇʀᴇᴅ ʙʏ ♡  [ 😻 #𝙸_𝙼_4𝚂𝚃_𝙵ʏᴛᴇʀ 👻 ](https://t.me/II_4ST_READY_FOR_FUCKING_II) 🌹**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def run_async_inline():
    @bot.on_inline_query()
    @inline_wrapper
    async def inline_query_handler(bot, query):
        text = query.query
        if text.startswith("help_menu_logo"):
            answer = []
            answer = await help_menu_logo(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        elif text.startswith("help_menu_text"):
            answer = []
            answer = await help_menu_text(answer)
            try:
                await bot.answer_inline_query(
                    query.id, results=answer, cache_time=10
                )
            except Exception as e:
                print(str(e))
                return
        else:
            return
