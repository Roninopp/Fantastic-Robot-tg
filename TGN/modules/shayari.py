import random
import asyncio
from pyrogram import filters
from TGN import pbot as FANTASTICFIGHTERBOT




ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...',
                     'Don't wait for things to happen. Make them happen.', 
                     'Nothing is permanent.
Don't stress yourself too much because no matter how bad the situation is, it will change.', 

                   ]

@FANTASTICFIGHTERBOT.on_message(filters.command("shayari"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)


__mod_name__ = "Sʜᴀʏᴀʀɪ"

help = """

ᴍᴀᴋᴇs ᴀ sʜᴀʏᴀʀɪ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.

❍ /shayari *:* ᴍᴀᴋᴇs sʜᴀʏᴀʀɪ ɪғ ʏᴏᴜ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

 """
