# (c) @AbirHasan2005 | @PredatorHackerzZ

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merger_Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
Hello!.👋 This Is A Video Merger Pro Bot.....!
You Can Use Me To Merge Multiple Videos in One with the Given Video Formats.

Check /about to Know More About Me.

Made With ❤ By @TheTeleRoid.
"""
    CAPTION = "Video Merged By @{}\n\nMade With ❤ By @TheTeleRoid"
    PROGRESS = """
➠ Percentage : {0}%

➠ Done : {1}

➠ Total : {2}

➠ Speed: {3}/s

➠ ETA : {4}
"""
    ABOUT_TEXT = """
<b>Mʏ ɴᴀᴍᴇ : <a href='http://t.me/TeleRoid_VideoMerge_Bot'>ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ</a></b>

<b>Cʜᴀɴɴᴇʟ : <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a></b>

<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/TeleRoid14'>@TeleRoid14</a></b>

<b>Vᴇʀꜱɪᴏɴ : <a href='https://t.me/joinchat/t1ko_FOJxhFiOThl'>2.0 ʙᴇᴛᴀ</a></b>

<b>Sᴏᴜʀᴄᴇ : <a href='https://github.com/PredatorHackerzZ'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>

<b>Sᴇʀᴠᴇʀ : <a href='https://heroku.com/'>ʜᴇʀᴏᴋᴜ</a></b>

<b>Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>Pʏᴛʜᴏɴ 3.10.2</a></b>

<b>Fʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢᴀᴍ 1.3.6</a></b>

<b>Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/MoviesFlixers_DL'>Pʀᴇᴅᴀᴛᴏʀ</a></b>

<b>Mᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/TheTeleRoid'>@TʜᴇTᴇʟᴇRᴏɪᴅ</a></b>

"""
