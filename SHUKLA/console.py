import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", "6762113050"))
OWNER_USERNAME = getenv("OWNER_USERNAME", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6919199044").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/4d72d398197a56fbf4a73.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴡɪᴛʜ ᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴠᴇʀꜱɪᴏɴ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ 𝙾𝙵 #4𝚂𝚃. \n\n❤️ 𝙿𝙻𝚉 𝚆𝙰𝙸𝚃 𝙵𝙾𝚁 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁. 𝙷𝙴 𝚆𝙸𝙻𝙻 𝙰𝙻𝙻𝙾𝚆 𝚄 𝙵𝙾𝚁 𝙳𝙼.\n\n🍂 ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ, ʙᴇᴄᴀᴜꜱᴇ ꜱᴘᴀᴍᴍɪɴɢ ᴡɪʟʟ ꜰᴏʀᴄᴇ ᴍᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ ɪᴅ 👍🏻 \n\n💗 𝚅𝙸𝚂𝙸𝚃 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾 :-» @II_4ST_READY_FOR_FUCKING_II*")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULTMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/4d72d398197a56fbf4a73.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

