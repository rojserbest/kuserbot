import asyncio
import io
import os
import sys
import traceback

from pyrogram import filters
from pyrogram.types import Message

from userbot import UserBot


@UserBot.on_message(filters.command("eval", ".") & filters.me & ~filters.forwarded)
async def evaluation_func(bot: UserBot, message: Message):
    status_message = await message.reply_text("...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        reply = message.reply_to_message or None
        await aexec(cmd, bot, message, reply, database)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>پێدراو</b>:\n<code>{}</code>\n\n<b>ئەنجام</b>:\n<code>{}</code>\n".format(
        cmd,
        evaluation.strip()
    )

    if len(final_output) > 4096:
        with open("eval.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document="eval.txt",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("eval.text")
        await status_message.delete()
    else:
        await status_message.edit(final_output)


async def aexec(code, b, m, r, d):
    sys.tracebacklimit = 0
    exec(
        'async def __aexec(b, m, r, d): ' +
        ''.join(f'\n {line}' for line in code.split('\n'))
    )
    return await locals()['__aexec'](b, m, r, d)


@UserBot.on_message(filters.command("exec", ".") & filters.me & ~filters.forwarded)
async def execution(_, message: Message):
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "بێئەنجام"
    o = stdout.decode()
    if not o:
        o = "بێهەڵە"

    OUTPUT = ""
    OUTPUT += f"<b>فەرمان:</b>\n<code>{cmd}</code>\n\n"
    OUTPUT += f"<b>ئەنجام</b>:\n<code>{o}</code>\n"
    OUTPUT += f"<b>هەڵەکان</b>:\n<code>{e}</code>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id
        )
        os.remove("exec.text")
    else:
        await message.reply_text(OUTPUT)
