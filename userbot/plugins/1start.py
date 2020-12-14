import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__

from userbot import UserBot, START_TIME
from userbot.helpers.constants import First
from userbot.plugins.help import add_command_help


@UserBot.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    txt = (
        "**بۆتی بەکارهێنەر لەکاردایە**\n"
        f"-> ماوەی لەکاربوون: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"-> وەشانی پایسۆن: `{python_version()}`\n"
        f"-> وەشانی پایرۆگرام: `{__version__}`"
    )
    await message.edit(txt)


@UserBot.on_message(filters.command("repo", ".") & filters.me)
async def repo(_, message: Message):
    await message.edit(First.REPO)


@UserBot.on_message(filters.command("creator", ".") & filters.me)
async def creator(_, message: Message):
    await message.edit(First.CREATOR)


@UserBot.on_message(filters.command(['uptime', 'up'], ".") & filters.me)
async def uptime(_, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await message.edit(
        "ماوەی لەکاربوون\n"
        f"```{str(current_uptime).split('.')[0]}```"
    )


@UserBot.on_message(filters.command("id", ".") & filters.me)
async def get_id(_, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**ناسنامەی فایل**: `{rep.audio.file_id}`"
            file_id += f"**سەرچاوەی فایل**: `{rep.audio.file_ref}`"
            file_id += "**جۆری فایل**: `audio`"

        elif rep.document:
            file_id = f"**ناسنامەی فایل**: `{rep.document.file_id}`"
            file_id += f"**سەرچاوەی فایل**: `{rep.document.file_ref}`"
            file_id += f"**جۆری فایل**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**ناسنامەی فایل**: `{rep.photo.file_id}`"
            file_id += f"**سەرچاوەی فایل**: `{rep.photo.file_ref}`"
            file_id += "**جۆری فایل**: `photo`"

        elif rep.sticker:
            file_id = f"**ناسنامەی لەزگە**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**کۆمەڵەی لەزگە**: `{rep.sticker.set_name}`\n"
                file_id += f"**ئیمۆجیی لەزگە**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**لەزگەی جووڵاو**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**لەزگەی جووڵاو**: نەخێر\n"
            else:
                file_id += "**کۆمەڵەی لەزگە**: __None__\n"
                file_id += "**ئیمۆجیی لەزگە**: __None__"

        elif rep.video:
            file_id = f"**ناسنامەی فایل**: `{rep.video.file_id}`\n"
            file_id += f"**سەرچاوەی فایل**: `{rep.video.file_ref}`\n"
            file_id += "**جۆری فایل**: `video`"

        elif rep.animation:
            file_id = f"**ناسنامەی فایل**: `{rep.animation.file_id}`\n"
            file_id += f"**سەرچاوەی فایل**: `{rep.animation.file_ref}`\n"
            file_id += "**جۆری فایل**: `GIF`"

        elif rep.voice:
            file_id = f"**ناسنامەی فایل**: `{rep.voice.file_id}`\n"
            file_id += f"**سەرچاوەی فایل**: `{rep.voice.file_ref}`\n"
            file_id += "**جۆری فایل**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**ناسنامەی فایل**: `{rep.animation.file_id}`\n"
            file_id += f"**سەرچاوەی فایل**: `{rep.animation.file_ref}`\n"
            file_id += "**جۆری فایل**: `Video Note`"

        elif rep.location:
            file_id = "**شوێن**:\n"
            file_id += f"**هێڵی درێژی**: `{rep.location.longitude}`\n"
            file_id += f"**هێڵی پانی**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**شوێن**:\n"
            file_id += f"**هێڵی درێژی**: `{rep.venue.location.longitude}`\n"
            file_id += f"**هێڵی پانی**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**ناونیشان**:\n"
            file_id += f"**سەردێڕ**: `{rep.venue.title}`\n"
            file_id += f"**زیاتر**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = f"**گواستراوەتەوە لە**: `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = f"**ناسنامەی بەکارهێنەر**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**ناسنامەی پەیام**: `{message.reply_to_message.message_id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = f"**گواستراوەتەوە لە**: `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = f"**ناسنامەی بەکارهێنەر**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**ناسنامەی پەیام**: `{message.reply_to_message.message_id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**ناسنامەی چات**: `{message.chat.id}`")


@UserBot.on_message(filters.command("restart", '.') & filters.me)
async def restart(_, message: Message):
    await message.edit("دەستپێدەکاتەوە....")
    await UserBot.send_message('me', f'#دەستپێکردنەوە، {message.chat.id}، {message.message_id}')

    if 'u' in message.text in message.text:
        asyncio.get_event_loop().create_task(UserBot.restart(update=True))
    else:
        asyncio.get_event_loop().create_task(UserBot.restart())


# Command help section
add_command_help(
    'start', [
        [
            '.alive',
            'زانینی ئەوەی کە ئایا بۆتەکە لەکاردایە یان نا'
        ],
        [
            '.repo',
            'ڕیپۆی ئەم بۆتە نیشاندەدات'
        ],
        [
            '.creator',
            'دروستکەری ئەم بۆتە نیشاندەدات'
        ],
        [
            '.id', 'ناسنامەی ئەو شتە دەنێرێت کە وەڵامتداوەتەوە'
        ],
        [
            '.up یان .uptime',
            'بینینی ماوەی کارکردنی بۆت'
        ]
    ]
)

add_command_help(
    'restart', [
        [
            '.restart',
            'بۆت دەستپێدەکاتەوە'
        ],
        [
            '.restart u',
            'بۆت نوێدەکاتەوە و دەستپێدەکاتەوە'
        ]
    ]
)
