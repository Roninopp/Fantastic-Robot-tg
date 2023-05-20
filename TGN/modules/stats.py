import html

import requests

from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update, MessageEntity, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import CallbackContext

from telegram.error import BadRequest

from telegram.utils.helpers import escape_markdown, mention_html

from TGN import dispatcher 

from TGN.modules.helper_funcs.chat_status import sudo_plus

NEKO_IMG = ""

@sudo_plus 
def stats(update, context): 
     status = "*Bot statistics*:\n"
     try: 
         update.effective_message.reply_photo( 
             NEKO_IMG, 
             status
             + "\n".join([mod.stats() for mod in STATS]) 
             + f"\n\n✦ Support | ✦ Updates\n\n" 
             + "\n╘══「 by Programmer • Network 」\n", 
             parse_mode=ParseMode.MARKDOWN, 
             reply_markup=InlineKeyboardMarkup( 
                 [ 
                     [ 
                         InlineKeyboardButton( 
                             text="SAMURAI", url="https://t.me/DushmanXronin" 
                         ) 
                     ] 
                 ] 
             ), 
         ) 
     except BaseException: 
         update.effective_message.reply_text( 
             ( 
                 ( 
                     ( 
                         "\n*Bot statistics*:\n" 
                         + "\n".join(mod.stats() for mod in STATS) 
                     ) 
                     + f"\n\n✦ Support | ✦ Updates\n\n" 
                 ) 
                 + "╘══「 by Programmer • Network 」\n" 
             ), 
             parse_mode=ParseMode.MARKDOWN, 
             reply_markup=InlineKeyboardMarkup( 
                 [ 
                     [ 
                         InlineKeyboardButton( 
                             text="RONIN", url="https://t.me/Dushmanxronin" 
                         ) 
                     ] 
                 ] 
             ), 
         )
     
     
     STATS_HANDLER = CommandHandler("stats", stats, run_async=True)
     
     dispatcher.add_handler(STATS_HANDLER)
     
     __mod_name__ = "Stats"
     __handlers__ = [STATS_HANDLER]
