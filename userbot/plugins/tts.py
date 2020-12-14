from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help
from gtts import gTTS, lang
import os

LANGS = lang.tts_langs()


@UserBot.on_message(filters.command('tts', ['.']) & filters.me)
async def send_query(bot: UserBot, message: Message):
    global LANGS
    try:
        i = message.text[5:]
        gTTS(i, lang="en-GB").save("tts.mp3")
        reply = message.reply_to_message.message_id if message.reply_to_message else None
        await message.delete()
        await UserBot.send_voice(message.chat.id, "tts.mp3", reply_to_message_id=reply)
    except:
        pass

add_command_help(
    'tts', [
        [
            '.gtts',
            'بە دەنگ کردنی نووسینەکەت'
        ]
    ]
)
