import asyncio
from datetime import datetime

import humanize
from pyrogram import filters
from pyrogram.types import Message

from userbot import UserBot
from userbot.helpers.PyroHelpers import GetChatID
from userbot.plugins.help import add_command_help

AFK = False
AFK_REASON = ''
AFK_TIME = ''
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    """Get humanized time"""
    subtracted = str(humanize.naturaltime(start - end))
    subtracted = subtracted.replace("seconds", "second")
    subtracted = subtracted.replace("minutes", "minute")
    subtracted = subtracted.replace("hours", "hour")
    subtracted = subtracted.replace("days", "day")
    subtracted = subtracted.replace("weeks", "week")
    subtracted = subtracted.replace("months", "month")
    subtracted = subtracted.replace("ago", "لەمەوپێش")
    subtracted = subtracted.replace("second", "چرکە")
    subtracted = subtracted.replace("minute", "خولەک")
    subtracted = subtracted.replace("hour", "کاتژمێر")
    subtracted = subtracted.replace("day", "رۆژ")
    subtracted = subtracted.replace("week", "هەفتە")
    subtracted = subtracted.replace("month", "مانگ")
    subtracted = subtracted.replace("a ", "یەک ")
    subtracted = subtracted.replace(" a ", " یەک ")
    subtracted = subtracted.replace(" a", " یەک")
    return subtracted


@UserBot.on_message(((filters.group & filters.mentioned) | filters.private) & ~filters.me, group=3)
async def collect_afk_messages(_, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in [
            'supergroup', 'group'] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            res = f"هۆکار: {AFK_REASON}" if len(AFK_REASON) != 0 else ""
            text = (
                f"سڵاو، ئەم نامەیە بۆتەکەم ناردوویەتی.\n"
                f"ئێستا لەسەرخەت نیم.\n"
                f"کۆتاجار کە لەسەرخەت بووم: {last_seen}\n"
                f"{res}"
            )
            await UserBot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=message.message_id
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 50:
                text = (
                    "سڵاو، ئەم نامەیە بۆتەکەم ناردوویەتی.\n"
                    "من ئێستا لەسەرخەت نیم.\n"
                    f"کۆتاجار کە لەسەرخەت بووم: {last_seen}\n"
                    "ئەمە دەیەمجارە پێت دەڵێم کە لەسەرخەت نیم.\n"
                )
                await UserBot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=message.message_id
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                res = f"هۆکار: {AFK_REASON}\n" if len(AFK_REASON) != 0 else ""
                text = (
                    "هەتا ئێستاش لەسەرخەت نیم.\n"
                    f"کۆتاجار کە لەسەرخەت بووم: {last_seen}\n"
                    f"{res}دواتر پەیامم بۆ بنێرە."
                )
                await UserBot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=message.message_id
                )

        CHAT_TYPE[GetChatID(message)] += 1


@UserBot.on_message(filters.command("afk", ".") & filters.me, group=3)
async def afk_set(_, message: Message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ''

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@UserBot.on_message(filters.me, group=3)
async def auto_afk_unset(_, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(
            datetime.now(), AFK_TIME
        ).replace('لەمەوپێش', '').strip()
        await message.reply(
            f"کە تۆ لەسەرخەت نەبوویت (بۆ ماوەی {last_seen}):\n"
            f"لە {sum(USERS.values())} کەس و {sum(GROUPS.values())} گروپەوە "
            f"{len(USERS) + len(GROUPS)} پەیامت بۆ هاتبوو."
        )
        AFK = False
        AFK_TIME = ''
        AFK_REASON = ''
        USERS = {}
        GROUPS = {}


add_command_help(
    'afk', [
        ['.afk', 'کە لەسەرخەت نامێنیت، بە ئەوانی دیکە دەڵێت کە لەسەرخەت نیت\nبەکارهێنان: ```.afk <هۆکار>```'],
    ]
)
