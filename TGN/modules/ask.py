from TGN import pbot as Mukund
import openai
import time
import os 
from pyrogram import filters

openai.api_key = os.environ.get("OPENAI_API_KEY")


async def generate_response(prompt):

    completions = openai.Completion.create(

        engine="text-davinci-002",

        prompt=prompt,

        max_tokens=1024,

        n=1,

        stop=None,

        temperature=.5,

    )

    message = completions.choices[0].text

    return message.strip()

@Mukund.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["",".", "/", "-", "?", "$"]))
async def chat(bot, message):
    try:
        start_time = time.time()
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`ai Give me a simple flask code?`")
        else:
            ok= await message.reply_text("`Processing... PLEASE WAIT FOR FEW SECONDS`")
            a = message.text.split(None, 1)[1]
            x=await generate_response(a)
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await ok.edit(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n FANTASTIC ROBOT ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @TEAMSAMURAII")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")

__help__ = """
**HERE IS ASK MODULE YOU CAN ALSO LEARN PYTHON BASICS BY USING THIS COMMAND**
  ➢ /ask *:* What is java
 
"""

__mod_name__ = "『ASK GPT』⁪⁬⁮⁮⁮⁮"
