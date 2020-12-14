from datetime import datetime
from time import sleep

from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message, User
from pyrogram.errors import PeerIdInvalid

from userbot import UserBot
from userbot.helpers.PyroHelpers import ReplyCheck
from userbot.plugins.help import add_command_help

WHOIS = (
    "**بەکارهێنەر \"{full_name}\" کێیە؟**\n"
    "[بەستەر بۆ پرۆفایل](tg://user?id={user_id})\n"
    "════════════════\n"
    "ناسنامە: `{user_id}`\n"
    "ناوی یەکەم: {first_name}\n"
    "ناوی دووەم: {last_name}\n"
    "ناوی بەکارهێنەرێتی: `{username}`\n"
    "کۆتاجار کە لەسەرخەت بووە: `{last_online}`\n"
    "گروپە هاوبەشەکان: {common_groups}\n"
    "════════════════\n"
    "ژیاننامە:\n{bio}"
)

WHOIS_PIC = (
    "**بەکارهێنەر \"{full_name}\" کێیە؟**\n"
    "[بەستەر بۆ پرۆفایل](tg://user?id={user_id})\n"
    "════════════════\n"
    "ناسنامە: `{user_id}`\n"
    "ناوی یەکەم: {first_name}\n"
    "ناوی دووەم: {last_name}\n"
    "ناوی بەکارهێنەرێتی: `{username}`\n"
    "کۆتاجار کە لەسەرخەت بووە: `{last_online}`\n"
    "گروپە هاوبەشەکان: `{common_groups}`\n"
    "════════════════\n"
    "وێنەکانی پرۆفایل: `{profile_pics}`\n"
    "کۆتاجار کە نوێکراوەتەوە: `{profile_pic_update}`\n"
    "════════════════\n"
    "بایۆ:\n{bio}"
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == 'recently':
        return "بەم نزیکانە"
    elif user.status == 'within_week':
        return "هەفتەی پێشوو"
    elif user.status == 'within_month':
        return "مانگی پێشوو"
    elif user.status == 'long_time_ago':
        return "ماوەیەکی درێێێژ لەمەوپێش :("
    elif user.status == 'online':
        return "لە ئێستادا لەسەرخەتە"
    elif user.status == 'offline':
        return datetime.fromtimestamp(user.status.date).strftime("%a, %d %b %Y, %H:%M:%S")


async def GetCommon(get_user):
    common = await UserBot.send(
        functions.messages.GetCommonChats(
            user_id=await UserBot.resolve_peer(get_user),
            max_id=0,
            limit=0))
    return common


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic[0].date).strftime("%d.%m.%Y, %H:%M:%S")


@UserBot.on_message(filters.command('whois', ['.', '']) & filters.me)
async def summon_here(_, message: Message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await UserBot.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("ئەم کەسە ناناسم.")
        sleep(2)
        await message.delete()
        return
    desc = await UserBot.get_chat(get_user)
    desc = desc.description
    user_pic = await UserBot.get_profile_photos(user.id)
    pic_count = await UserBot.get_profile_photos_count(user.id)
    common = await GetCommon(user.id)

    if not user.photo:
        await message.edit(
            WHOIS.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "دانەنراوە",
                username=user.username if user.username else "دانەنراوە",
                last_online=LastOnline(user),
                common_groups=len(common.chats),
                bio=desc if desc else "دانەنراوە"),
            disable_web_page_preview=True)
    elif user.photo:
        await UserBot.send_photo(
            message.chat.id,
            user_pic[0].file_id,
            caption=WHOIS_PIC.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "دانەنراوە",
                username=user.username if user.username else "دانەنراوە",
                last_online=LastOnline(user),
                profile_pics=pic_count,
                common_groups=len(common.chats),
                bio=desc if desc else "دانەنراوە",
                profile_pic_update=ProfilePicUpdate(user_pic)),
            reply_to_message_id=ReplyCheck(message),
            file_ref=user_pic[0].file_ref,
        )
        await message.delete()


add_command_help(
    'whois', [
        [
            '.whois',
            'دەستکەوتنی هەندێک زانیاری ئەو کەسەی وەڵامیدەدەیتەوە'
        ]
    ]
)
