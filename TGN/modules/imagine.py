"""
DOCUMENTATION:

Dependencies:
    - replicate
    - pyrogram
    
How to get the API TOKEN?
    - You can get the API token from `https://replicate.com/account`. After that add the token in your environment variables as `AI_ART_TOKEN`.

How to use this module?
    - Simply paste this module in your module folder, but first check if there is any import errors.

Can I edit the model?
    - Yeah, totally. BUt first check the documentation.
    
Reference:
    - `https://docs.pyrogram.org`
    - `https://replicate.com/docs`
    
Note: Please check `https://replicate.com/pricing` before using this module.

        ~github.com/SOME-1HING
"""

import os
import re
import replicate

from replicate.exceptions import ModelError
from pyrogram.types import Message
from pyrogram import Client, filters
from TGN import pbot as app

# Initialize the replicate client with the API token
rp = replicate.Client(api_token=os.getenv("AI_ART_TOKEN", None))

# Get the model and version
model = rp.models.get("stability-ai/stable-diffusion")
version = model.versions.get(
    "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"
)


# Define the command handler
@app.on_message(filters.command("draw"))
async def imagine(app: Client, message: Message):
    # Check if the prompt is provided
    if len(message.text.split()) < 2:
        return await message.reply_text("Provide Prompt.")

    # Extract the prompt from the command
    prompt = re.sub(r"\b" + "/draw" + r"\b", "", message.text)

    # Show "Please wait" message
    msg = await message.reply_text("Please wait.")

    # Generate the image from the prompt using the model
    try:
        image = version.predict(prompt=prompt)[0]
    except ModelError:
        return await message.reply_text(
            "NSFW content detected. Try running it again, or try a different prompt."
        )

    # Reply to the message with the generated image
    await message.reply_photo(image)

    # Delete the "Please wait" message
    await msg.delete()

    return
