from TGN import pbot as Mukund
import openai
import time
from pyrogram import filters

openai.api_key = "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"
@Mukund.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["",".", "/", "-", "?", "$"]))
async def chat(bot, message):
    try:
        start_time = time.time()
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`ai Give me a simple flask code?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],temperature=0.2,)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n FANTASTIC ROBOT ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @FANTASTICFIGHTERBOT")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")
