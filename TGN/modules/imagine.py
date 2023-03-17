import os
import re
import replicate

from pyrogram.types import Message
from pyrogram import Client, filters
from TGN import pbot as app

rp = replicate.Client(api_token=os.getenv("AI_ART_TOKEN", None))

model = rp.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"
)


@app.on_message(filters.command("draw"))
async def imagine(app: Client, message: Message):
    query = message.text.split(" ")
    if len(query) < 1:
        return await message.reply_text("Provide Prompt.")

    prompt = re.sub(r"\b" + "/draw" + r"\b", "", query)
    msg = await message.reply_text("Please wait.")

    image = await version.predict(prompt=prompt)[0]

    await message.reply_photo(image)

    await msg.delete()

    return
