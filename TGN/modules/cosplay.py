import requests
from telethon import events
from TGN import telethn as lol

@lol.on(events.NewMessage(pattern="^/cosplay"))
async def waifu(event):
  r = requests.get("https://waifu-api.vercel.app").json() #api credit- @DUSHMANXRONIN on telegram
  await event.reply(file=r)
  

mod_name = "Cosplay"
