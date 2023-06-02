# import os
# import requests as r
# from telegraph import upload_file
# from pyrogram import filters, enums
# from pyrogram import *
# from pyrogram.types import *
# from pyrogram.enums import *
# from pyrogram.types import InlineKeyboardButton
# from pyrogram.types import InlineKeyboardMarkup , CallbackQuery , ForceReply
# from telegram import Update, ParseMode , bot

# import traceback

# #NAME => YOUR BOTS FILE NAME
# from TGN import pbot

# #ADD ANY BUTTON YOU WANT BELOW YOUR WELCOME IMAGE
# #markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("MODS", url="https://t.me/NovaXMod")]])

# @pbot.on_message(filters.new_chat_members & filters.group, group=69)
# async def welcomepic(_, message):
#     chat = message.chat
#     user = message.from_user
#     for u in message.new_chat_members:
#         MSG = f"""
# **WELCOME TO {message.chat.title}
# ➖➖➖➖➖➖➖➖➖➖➖➖
# NAME: {u.mention}
# ID: {u.id}
# USERNAME: @{u.username}
# COUNT: {await pbot.get_chat_members_count(message.chat.id)}
# ➖➖➖➖➖➖➖➖➖➖➖➖**
# """

#         uid = u.id
#         try:
#             Up = (await pbot.get_chat(uid)).photo
            
#             await pbot.download_media(Up.big_file_id, file_name=f"pfp_{uid}.png")
            
#             a = upload_file(f"./downloads/pfp_{uid}.png")

#             for x in a:
#                 url = "https://graph.org/" + x
#                 resp = r.post("https://nova-apis.up.railway.app/generate", json={'name' : f'{u.first_name}','user_name' : f'@{u.username}','user_id' : f'{u.id}','profile_pic' : f'{url}','group_name' : f'{message.chat.title}' ,"auth_key" : "Yash_Yash__@"}).json()
#                 await message.reply_photo((resp['image_url']), caption=MSG)
#                 os.remove(f"./downloads/pfp_{uid}.png")
#         except AttributeError:
#             resp = r.post("https://nova-apis.up.railway.app/generate", json={'name' : f'{u.first_name}','user_name' : f'@{u.username}','user_id' : f'{u.id}','group_name' : f'{message.chat.title}' ,"auth_key" : "Yash_Yash__@"}).json()
#             await message.reply_photo((resp['image_url']), caption=MSG)
#             os.remove(f"./downloads/pfp_{uid}.png")
            
            
#         if u.id == 2100096282:
#                 try : 
#                     if chat.type == chat.SUPERGROUP:
#                         GROUP_LINK = f"@{chat.username}"
#                     else :
#                         GROUP_LINK = "Private"
#                 except Exception:
#                     GROUP_LINK = "private"
#                     traceback.print_exc()
#                     # print(2)

#                 added_by = user
#                 chet = await pbot.get_chat(chat.id) 
#                 members = chet.members_count
#                 # print(1)
#                 try :
#                     await pbot.send_message(
#                             chat_id =-1001739122591,
#                             text = f"""
# #ADDED #GROUP
# • Name : <code>{chat.title}</code>
# • Link : {GROUP_LINK}
# • ID : <code>{chat.id}</code>
# • Members : <code>{members}</code>
# • Added by : @{added_by.username}
# • User ID : <code>{added_by.id}</code>
# """,
#                             parse_mode=ParseMode.HTML
#                             )
#                 except Exception:
#                     traceback.print_exc()

#                 # print(9)
#                 await pbot.reply_text(
#                     "Hey {}, I'm Fantastic Robot! Thank you for adding me to {}\n"
#                     "Join support and channel update with clicking button below!".format(
#                         user.first_name, chat.title
#                     ),
#                     parse_mode=ParseMode.MARKDOWN,
#                     reply_markup=InlineKeyboardMarkup(
#                         [
#                             [
#                                 InlineKeyboardButton(
#                                     text="Support🚑",
#                                     url=f"https://t.me/fantastic_support",
#                                 ),
#                                 InlineKeyboardButton(
#                                     text="Updates🛰️",
#                                     url="https://t.me/serenityupdates",
#                                 ),
#                             ]
#                         ]
#                     ),
#                 )
#                 continue
