from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help
from time import sleep
from userbot.helpers import fonts as emojify
from emoji import UNICODE_EMOJI


@UserBot.on_message(filters.command("emoji", ".") & filters.me)
async def emoji(bot: UserBot, message: Message):
    args = message.text.split()

    if len(args) == 1:
        m = await message.edit(
            "نووسینێکم پێبدە."
        )
        sleep(2)
        await m.delete()
        return
    try:
        emoji, arg = args[1], "".join(args[2:])
        if emoji not in UNICODE_EMOJI:
            m = await message.edit(
                "ئیمۆجیەکت پێنەداوم."
            )
            sleep(2)
            await m.delete()
            return
    except:
        m = await message.edit(
            "ئیمۆجیەکت پێنەداوم."
        )
        sleep(2)
        await m.delete()
        return
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[
                emojify.kakashitext.index(a)
            ].format(
                cj=emoji
            )
            result += char
        else:
            result += a
    await message.edit(result)

add_command_help(
    'emoji', [
        [
            '.emoji',
            '.emoji <ئیمۆجیەک> SOME TEXT\nنووسینەکە بەو ئیمۆجیە دەنووسێت کە دیاریدەکەیت.'
        ]
    ]
)
