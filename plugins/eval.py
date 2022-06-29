import random
import re
import sys
import traceback
from io import StringIO
import pyrogram
import time, datetime
import os
import requests
import wget

from aiogram.utils.markdown import quote_html
from meval import meval
from pyrogram import Client, filters



class MyInput:
    def __init__(self, text=""):
        pass

    def __str__(self):
        return "simulate input"

    def __int__(self):
        return random.randint(0, 1000)


async def slicer(text, step):
    for i in range(0, len(text), step):
        yield text[i:i+step]


async def get_code(string, msg=False):
	regex = r"(Код|Выполнено):\n(.+)(Результат|Вывод|Возвращено|Ошибка):\n(.+)(Результат|Вывод|Возвращено|Ошибка)"
	result = re.search(regex, string, re.S)
	try:
		return result.group(2)
	except AttributeError:  # если первый шаблон не подходит
		regex = r"(Код|Выполнено):\n(.+)(Результат|Вывод|Возвращено|Ошибка):"
		result = re.search(regex, string, re.S)
		try:
			return result.group(2)
		except AttributeError:
			if msg:
				return msg.reply_to_message.text



@Client.on_message(filters.regex(r"(Код|Выполнено):\n(.+)(Результат|Вывод|Возвращено|Ошибка):", re.S) & filters.me & filters.edited)
@Client.on_message(filters.command("e", prefixes=".") & filters.me)
async def evalcmd(app, msg):
    if msg.command:
        if len(msg.command) > 1:
            args = re.sub(r"^.+e[\s\n]", "", msg.text)
        else:
            args = await get_code(msg.reply_to_message.text, msg)
    else:  # если редактирование
        args = await get_code(msg.text, msg)
    old_stdout = sys.stdout
    result = sys.stdout = StringIO()
    error = None
    output = None
    attrs = await getattrs(app, msg)
    attrs.update(globals())
    try:
        output = await meval(args, globals(), **attrs)
    except:
        error = traceback.format_exc(limit=0)
    result = result.getvalue()

    if len(str(output)) < 3900:
        result_output = f"**Код:**\n```{quote_html(args)}```"
        result_output += "\n\n**Возвращено:**\n```{}```".format(quote_html(output).rstrip('\n') )
        result_output += "\n\n**Вывод:**\n```{}```".format(quote_html(result).rstrip('\n')) if result else ""
        result_output += "\n\n**Ошибка:**\n```{}```".format(quote_html(error).rstrip('\n')) if error else ""

        await msg.edit(result_output)

    elif 3900 < len(str(output)) < 40000:
        await msg.edit(f"**Код:**```\n{quote_html(args)}```\n\n"f"**Возвращено:**\n```{str(output)[:3900]}```")
        async for i in slicer(str(output)[3900:], 3900):
            await msg.reply(f"```{i}```")
    else:
        await msg.edit(f"**Код:**```\n{quote_html(args)}```\n\n"f"**Возвращено:**\n```MESSAGE_TOO_LONG```")
    sys.stdout = old_stdout


async def getattrs(app, msg):
    return {"reply": msg.reply_to_message,
            "msg": msg,
            "app": app,
            "chat": msg.chat,
            "message": msg,
            "client": app,
            "input": MyInput
            }

@Client.on_message(filters.command("w", prefixes=".") & filters.me)
async def whao_cmd(app, msg):
    text = msg.text.split(maxsplit=1)[1]
    wget.download(text)
    await msg.edit('Файл скачался!')

@Client.on_message(filters.command("torrentdown", prefixes=".") & filters.me)
async def torrentdown_cmd(app, msg):
	await msg.reply_to_message.download()

