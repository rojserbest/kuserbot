import asyncio
from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.plugins.help import add_command_help
from collections import deque


@UserBot.on_message(filters.command("lmao", ".") & filters.me)
async def lmao(bot: UserBot, message: Message):
    await message.edit("پێکەنین")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("think", ".") & filters.me)
async def think(bot: UserBot, message: Message):
    await message.edit("بیرکردنەوە")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("nhappy", ".") & filters.me)
async def nhappy(bot: UserBot, message: Message):
    await message.edit("دڵناخۆش")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("clock", ".") & filters.me)
async def clock(bot: UserBot, message: Message):
    await message.edit("کات")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("muah", ".") & filters.me)
async def muah(bot: UserBot, message: Message):
    await message.edit("مواح")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("heart", ".") & filters.me)
async def heart(bot: UserBot, message: Message):
    await message.edit("دڵ")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("gym", ".") & filters.me)
async def gym(bot: UserBot, message: Message):
    await message.edit("جیم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("earth", ".") & filters.me)
async def earth(bot: UserBot, message: Message):
    await message.edit("زەوی")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)


@UserBot.on_message(filters.command("moon", ".") & filters.me)
async def moon(bot: UserBot, message: Message):
    await message.edit("مانگ")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit("".join(deq))
        deq.rotate(1)

add_command_help(
    'animation1', [
        [
            '.lmao',
            'پێکەنین'
        ],
        [
            '.think',
            'بیرکردنەوە'
        ],
        [
            '.clock',
            'کات'
        ],
        [
            '.muah',
            'مواح'
        ],
        [
            '.heart',
            'دڵ'
        ],
        [
            '.gym',
            'جیم'
        ],
        [
            '.earth',
            'زەوی'
        ],
        [
            '.moon',
            'مانگ'
        ]
    ]
)
