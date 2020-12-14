from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help

CHAT_ID = None
REPLY_TO = None

@UserBot.on_message(filters.user("QuotLyBot") & filters.sticker)
async def send_result(bot: UserBot, message: Message):
    global CHAT_ID, REPLY_TO
    
    if CHAT_ID != None:
        try:
            if REPLY_TO != None:
                await UserBot.send_sticker(CHAT_ID, message.sticker.file_id, reply_to_message_id=REPLY_TO)
            else:
                await UserBot.send_sticker(CHAT_ID, message.sticker.file_id)
            CHAT_ID, REPLY_TO = None, None
        except:
            pass


@UserBot.on_message(filters.command('quotly', ['.']) & filters.me)
async def send_query(bot: UserBot, message: Message):
    global CHAT_ID, REPLY_TO
    
    try:
        CHAT_ID, REPLY_TO = message.chat.id, message.reply_to_message.message_id if message.reply_to_message else None
        await UserBot.send_message("QuotLyBot", message.text[8:])
        await message.delete()
    except:
        pass

    try:
        await message.delete()
    except:
        pass


add_command_help(
    'quotly', [
        [
            '.quotly',
            'بە وتە کردنی نووسینەکەت'
        ]
    ]
)
