from pyrogram import *
from pyrogram.types import *

from TGN import pbot as app

from TGN.__main__ import STATS 

@app.on_message(filters.command("bstats"), group=69)
async def botstats(_, message):
    text = "Bot Stats\n"
    await message.reply_text(text + "\n".join([mod.__stats__() for mod in STATS]))

