import time

from pyrogram import filters
from pyrogram.types import Message, ChatPermissions

from pyrogram.errors import UserAdminInvalid

from userbot import UserBot
from userbot.helpers.PyroHelpers import GetUserMentionable
from userbot.helpers.adminHelpers import (
    CheckAdmin, CheckReplyAdmin, RestrictFailed
)
from userbot.plugins.help import add_command_help


@UserBot.on_message(filters.command("ban", '.') & filters.me)
async def ban_hammer(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            if message.command == ['ban', '24']:
                await UserBot.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    until_date=int(time.time() + 86400)
                )
                await message.edit(f"بەکارهێنەر {mention} بۆ 24 کاتژمێر قەدەغەکرا.")
            else:
                await UserBot.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                )
                await message.edit(f"بەکارهێنەر {mention} قەدەغەکرا.")
        except UserAdminInvalid:
            await RestrictFailed(message)


@UserBot.on_message(filters.command("unban", '.') & filters.me)
async def unban(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await UserBot.unban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )
            await message.edit(f"قەدەغەی بەکارهێنەر {mention} لابرا.")
        except UserAdminInvalid:
            await message.edit("ناتوانم قەدەغەی ئەم بەکارهێنەرە لابەم.")


# Mute Permissions
mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_stickers=False,
    can_send_animations=False,
    can_send_games=False,
    can_use_inline_bots=False,
    can_add_web_page_previews=False,
    can_send_polls=False,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False
)


@UserBot.on_message(filters.command("mute", '.') & filters.me)
async def mute_hammer(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            if int(message.command[1]):
                await UserBot.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    permissions=mute_permission,
                    until_date=int(
                        time.time() + 3600 *
                        int(message.command[1])
                    )
                )
                await message.edit(f"بەکارهێنەر {mention} بۆ {message.command[1]} کاتژمێر بێدەنگکرا.")
            else:
                await UserBot.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    permissions=mute_permission
                )
                await message.edit(f"بەکارهێنەر {mention} بێدەنگکرا")
        except UserAdminInvalid:
            await RestrictFailed(message)


# Unmute permissions
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False
)


@UserBot.on_message(filters.command("unmute", '.') & filters.me)
async def unmute(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await UserBot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=unmute_permissions
            )
            await message.edit(f"بەکارهێنەر {mention} ئێستا دەتوانێت لێرە پەیام بنێرێت.")
        except UserAdminInvalid:
            await RestrictFailed(message)


@UserBot.on_message(filters.command("kick", '.') & filters.me)
async def kick_user(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await UserBot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )
            await message.edit(f"بای {mention}، دەرکرایت.")
        except UserAdminInvalid:
            await RestrictFailed(message)


add_command_help(
    'ban', [
        ['.ban', 'بەکارهێنەر قەدەغەدەکات'],
        ['.ban 24', 'بەکارهێنەر بۆ 24 کاتژمێر قەدەغەدەکات\nلە شوێنی 24 دەتوانیت ژمارەی دیکە بنووسیت'],
        ['.unban', 'قەدەغەی بەکارهێنەر ناهێڵێت'],
        ['.mute', 'بەکارهێنەر بێدەنگدەکات'],
        ['.mute 24', 'بەکارهێنەر بۆ 24 کاتژمێر بێدەنگدەکات'],
        ['.unmute', 'ڕێ بە بەکارهێنەر دەدات قسەبکاتەوە'],
        ['.kick', 'بەکارهێنەر دەردەکات'],
    ]
)
