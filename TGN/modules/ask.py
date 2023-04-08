from TGN import pbot as Mukund
import openai
import time
import os 
from pyrogram import filters

openai.api_key = os.environ.get("OPENAI_TOKEN", "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")

async def gen(prompt):
    #Fixed By Wolf :)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.8,
        max_tokens=1024,
        top_p=0.7,
        frequency_penalty=0,
        presence_penalty=0)

    # Get the response text from the API response
    answer = response.choices[0].text.strip()
    return answer
@Mukund.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["",".", "/", "-", "?", "$"]))
async def chat(bot, message):
    try:
        start_time = time.time()
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`ai Give me a simple flask code?`")
        else:
            a = message.text.split(' ', 1)[1]
            x=await gen(a)
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n FANTASTIC ROBOT ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @FANTASTICFIGHTERBOT")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")
