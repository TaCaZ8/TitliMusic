from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", "5782858671:AAGebiBT_365wcd5kJQdGAxF6gJ0h9efWA4")
BOT_NAME = getenv("BOT_NAME","Titli ᴍᴜsɪᴄ ʙᴏᴛ")
BOT_USERNAME = getenv("BOT_USERNAME", "QueenMusicX_Bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "jaanu_stuff")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Agricultura_Queen")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/89cbc8b8760b6abff430f.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQDA9c1N8Sx_yl-AwEzIiz0efC3vpfCSwP1RE5rAPHxAY8asfOkl-_SGo1gcrVmzyn70EIsl6jr6v1IF2sejERZDb3OGkgwxbNN9RWhYd1m3eTh7n4vd66l6ajAjlQ93a86OOlWJGmbiA6JmzFzAM_yBoAPBMv_xGNHDQtlNRNcCCkqRuXagO2lmmx-WOAAKHjUzZhMKIswU_zjEgHi4UsgixqMOeGlgSl-_JT-KfGofcSXcDaKDZ9aTV1ZEUSTW1rSFv55lNDxoLnSltoGGf4gduIMdb8uxsIUITUs67ezDHWih1zO56Xo6HSMGcANHYNx7q_mJxISFqd23c7TUleAAAAAThX180A. ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5416733128").split()))
