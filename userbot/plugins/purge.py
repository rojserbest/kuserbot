from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from userbot import UserBot
from userbot.plugins.help import add_command_help
from time import sleep


@UserBot.on_message(filters.command('del', ['.']) & filters.me)
async def dele(bot: UserBot, message: Message):
    try:
        await message.reply_to_message.delete()
    except:
        pass

    try:
        await message.delete()
    except:
        pass

# Thanks to TeamDerUntergang/Telegram-SedenUserBot for their idea.


@UserBot.on_message(filters.command('purge', ['.']) & filters.me)
async def purge(bot: UserBot, message: Message):
    msg = message.reply_to_message
    if msg:
        itermsg = [
            i async for i in UserBot.iter_history(
                message.chat.id,
                offset_id=msg.message_id,
                reverse=True
            )
        ]
    else:
        return

    count = 0

    for message in itermsg:
        try:
            count = count + 1
            await UserBot.delete_messages(message.chat.id, message.message_id)
        except FloodWait as e:
            sleep(e.x)
        except Exception as e:
            return

    done = await UserBot.send_message(
        message.chat.id,
        f"خاوێنکردنەوەی خێرا تەواوبوو!\n{count} پەیام سڕانەوە."
    )
    sleep(2)
    await done.delete()

add_command_help(
    'purge', [
        [
            '.del',
            'سڕینەوەی ئەو پەیامەی وەڵامیدەدەیتەوە'],
        [
            '.purge',
            'دەستکردن بە خاوێنکردنەوەی خێرا لەو شوێنەوەی وەڵامی دەدەیتەوە'
        ]
    ]
)
