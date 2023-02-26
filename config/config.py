import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

# ADMIN DETAILS (Your ID) 
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "").split())
)
OWNER_NAME = getenv("OWNER_NAME") 

# BOT TOKEN CONFIG VARS (get all vars detail from @botfather) 
BOT_TOKEN = getenv("BOT_TOKEN", None) 
BOT_TOKEN2 = getenv("BOT_TOKEN2", None) 
BOT_TOKEN3 = getenv("BOT_TOKEN3", None) 
BOT_TOKEN4 = getenv("BOT_TOKEN4", None) 
BOT_TOKEN5 = getenv("BOT_TOKEN5", None) 
BOT_TOKEN6 = getenv("BOT_TOKEN6", None) 
BOT_TOKEN7 = getenv("BOT_TOKEN7", None) 
BOT_TOKEN8 = getenv("BOT_TOKEN8", None) 
BOT_TOKEN9 = getenv("BOT_TOKEN9", None) 
BOT_TOKEN10 = getenv("BOT_TOKEN10", None) 


# EXTRA VARS
ALIVE_PIC = getenv("ALIVE_PIC") 
CMD_HNDLR = getenv("CMD_HNDLR") 