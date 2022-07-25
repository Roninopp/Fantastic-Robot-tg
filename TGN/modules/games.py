from pyrogram import filters
from pyrogram.types import Message

from TGN import pbot as app




@app.on_message(filters.command("dice"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("dart"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("basket"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command("bowling"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎳")

@app.on_message(filters.command("football"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "⚽")

@app.on_message(filters.command("slot"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎰")
