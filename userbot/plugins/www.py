import asyncio
import time

import speedtest
from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message

from userbot import UserBot
from userbot.helpers.PyroHelpers import SpeedConvert
from userbot.helpers.constants import WWW
from userbot.plugins.help import add_command_help


@UserBot.on_message(filters.command(["speed", 'speedtest'], ".") & filters.me)
async def speed_test(_, message: Message):
    new_msg = await message.edit(
        "تاقیکردنەوەی خێرایی دەکرێت . . .")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "خێراترین ڕاژەکار هەڵدەبژێردرێت بە پێی پینگ . . .")
    spd.get_best_server()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "تاقیکردنەوەی خێرایی داگرتن دەکرێت . . .")
    spd.download()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n"
        "تاقیکردنەوەی خێرایی بەرزکردنەوە دەکرێت . . .")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n"
        "ئەنجامەکان نیشاندەدرێت . . .")
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results['timestamp'],
            ping=results['ping'],
            download=SpeedConvert(results['download']),
            upload=SpeedConvert(results['upload']),
            isp=results['client']['isp']
        ))


@UserBot.on_message(filters.command("dc", ".") & filters.me)
async def nearest_dc(_, message: Message):
    dc = await UserBot.send(
        functions.help.GetNearestDc())
    await message.edit(
        WWW.NearestDC.format(
            dc.country,
            dc.nearest_dc,
            dc.this_dc))


@UserBot.on_message(filters.command("ping", ".") & filters.me)
async def ping_me(_, message: Message):
    """Ping the assistant"""
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**پۆنگ!**\n{delta_ping * 1000:.3f} مچ")


add_command_help(
    'www', [
        [
            '.ping',
            'خێرایی نێوان شوێنی بۆتەکە و تەلەگرامت پێدەڵێت'
        ],
        [
            '.dc',
            'نزیکترین داتاسەنتەری تەلەگرامت پێدەڵێت'
        ],
        [
            '.speedtest یان .speed',
            'خێرایی هێڵی ئینتەرنێتی هۆستی بۆتەکەت پێدەڵێت'
        ]
    ]
)
