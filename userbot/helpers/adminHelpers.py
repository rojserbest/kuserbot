from time import sleep, time

from pyrogram.types import Message

from userbot import UserBot
from userbot.helpers.interval import IntervalHelper


async def CheckAdmin(message: Message):
    """Check if we are an admin."""
    admin = 'administrator'
    creator = 'creator'
    ranks = [admin, creator]

    SELF = await UserBot.get_chat_member(
        chat_id=message.chat.id,
        user_id=message.from_user.id)

    if SELF.status not in ranks:
        await message.edit("بەرێوەبەر نیت!")
        sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("مافی سنووردارکردنی خەڵکت نیە")
            sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit(f"دەبێت `?{message.command[0]}` وەڵامی یەکێک بدەیتەوە.")
        sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"ناتوانم خۆم {message.command[0]} بکەم.")
        sleep(2)
        await message.delete()
    else:
        return True


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"ناتوانم ئەم بەکارهێنەرە {message.command} بکەم.")
    sleep(2)
    await message.delete()
