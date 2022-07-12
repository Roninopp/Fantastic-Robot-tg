import random
import asyncio
from pyrogram import filters
from TGN import pbot as WILDROBOT

GAALI_STRINGS = [
                     'ABA CHOOT KA TAPAKTA PANI NANKU MOCHI KI LAWARIS AULAD...',
                     'MADARBHOSDI AAJ TO CHODUGA TERI AMMA TOD KA KHATIYA...',
                     'Saale Phatele Nirodh Ke Natije. Chut Ka Maindak…!...',
                     'Chut Ke Pasine Mein Talay Hue Bhajiye…Chullu Bhar Muth Mein Doob Mar! ...',
                     'Kaali Chut Ke Safed Jhaant…...',
                     'Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain...',
                     'Naa Chut, Naa Choche, Aur Nakhre Noor Jahan Ke!...',
                     'Teri Gaand Mein Kutte Ka Lund...',
                     'Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana...',
                     'Chutiya kitne tikega teri behen ka gand marunga eisa marunga ki teri behen ka doodh pura india peeyega. Eisa marunga ki teri amma meri private randi iiiii   hehehhehahhaha . Areh lawde eisa chodunga ki ane wale 7 janam tak teri behen meri private randi rahegi🤤🤤🤤🤤...',
                     'Ahahahhahahaha beta dekh TV pe teri ammi ka porn bana rha mein😂😂😂...',
                     'Ye teri ammi ke porn pure xxxxx videos pe upload karke paisa kamaunga. Ek kaam kar lawde porn sites pe sabki mummy randi type kar tereko kaise paida kia tha wo wala video bhi a ajyega ehsaan man ki mera lund chooske teri ammi ne tereko paida kia🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤 jaanat de dia tereko😂😂😂...',

                   ]

@FANTASTICFIGHTERBOT.on_message(filters.command("gaali"))
async def lel(bot, message):
    ran = random.choice(GAALI_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)


__mod_name__ = "FULLGALI"

help = """

ᴍᴀᴋᴇs ᴀ ABUSE ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.

❍ /fullabuse *:* ᴍᴀᴋᴇs ABUSE ɪғ ʏᴏᴜ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ NOTE THIS COMMAND ONLY FOR 16+ aGE USERS

 """
