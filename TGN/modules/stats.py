@sudo_plus 
def stats(update, context): 
     uptime = datetime.datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S") 
     botuptime = get_readable_time((time.time() - StartTime)) 
     status = "*╒═══「 System statistics 」*\n\n" 
     status += "*➢ System Start time:* " + str(uptime) + "\n" 
     uname = platform.uname() 
     status += "*➢ System:* " + str(uname.system) + "\n" 
     status += "*➢ Node name:* " + escape_markdown(str(uname.node)) + "\n" 
     status += "*➢ Release:* " + escape_markdown(str(uname.release)) + "\n" 
     status += "*➢ Machine:* " + escape_markdown(str(uname.machine)) + "\n" 
     mem = virtual_memory() 
     cpu = cpu_percent() 
     disk = disk_usage("/") 
     status += "*➢ CPU:* " + str(cpu) + " %\n" 
     status += "*➢ RAM:* " + str(mem[2]) + " %\n" 
     status += "*➢ Storage:* " + str(disk[3]) + " %\n\n" 
     status += "*➢ Python Version:* " + python_version() + "\n" 
     status += "*➢ python-Telegram-Bot:* " + str(ptbver) + "\n" 
     status += "*➢ Uptime:* " + str(botuptime) + "\n" 
     try: 
         update.effective_message.reply_photo( 
             NEKO_IMG, 
             status 
             + "\n*Bot statistics*:\n" 
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
