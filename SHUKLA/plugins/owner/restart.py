import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from ... import app, SUDO_USER
from ... import *

@app.on_message(cdz(["restart"]) & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**Restarting...**")
    await message.delete()
    await reply.edit_text("Successfully Restarted #_4ST_𝙵𝚄𝙲𝙺𝙸𝙽𝙶_𝙱𝙾𝚃...\n\n💞 𝚆𝙰𝙸𝚃 2 𝙼𝙸𝙽𝚂...𝙿𝙾𝚆𝙴𝚁 𝙸𝚉 𝙾𝙵𝙵..\nLoad plugins...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLA")
  

__NAME__ = "Rᴇsᴛᴀʀᴛ"
__MENU__ = """
`.restart` **heroku bot restart **
`.upload` **Upload the file to telegram from the given system file path**
"""
