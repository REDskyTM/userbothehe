import random
import re
import sys
import traceback
from io import StringIO
from html import escape

from pyrogram import Client, filters, types
from meval import meval


class Help:
    des = "Выполнение Python кода"
    ver = "4.1"
    author = "Кобан"
    cmd_list = {
        "e + код": "выполнение"
    }
    in_help = "e"


class MyInput:
    def __init__(self, text=""):
        pass

    def __str__(self):
        return "simulate input"

    def __int__(self):
        return random.randint(0, 1000)


async def slicer(text, step):
    for i in range(0, len(text), step):
        yield text[i:i + step]


class Attrs:
    def __call__(self, obj: object):
        return "\n".join(dir(obj))

    def __lshift__(self, obj: object):
        return self(obj)

    def __gt__(self, obj: object):
        return self(obj)

    @staticmethod
    def search(obj: object, query: str):
        return [a for a in dir(obj) if query in a]


async def get_code(string, msg: types.Message = None):
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


@Client.on_edited_message(
    filters.regex(r"(Код|Выполнено):\n(.+)(Результат|Вывод|Возвращено|Ошибка):", re.S) & filters.me)
@Client.on_message(filters.command("e", ".") & filters.me)
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
    error = output = None

    attrs = await getattrs(app, msg)
    attrs.update(globals())
    try:
        output = await meval(args, globals(), **attrs)
    except:
        error = traceback.format_exc(limit=0)
    result = result.getvalue()

    if len(str(output)) < 3900:
        result_output = f"**Код:**\n```{escape(str(args)).strip()}```"
        result_output += "\n\n**Возвращено:**\n```{}```".format(escape(str(output)).rstrip('\n'))
        result_output += "\n\n**Вывод:**\n```{}```".format(escape(result).rstrip('\n')) if result else ""
        result_output += "\n\n**Ошибка:**\n```{}```".format(escape(error).rstrip('\n')) if error else ""

        await msg.edit(result_output)

    elif 3900 < len(str(output)) < 40000:
        await msg.edit(f"**Код:**```\n{escape(args)}```\n\n"f"**Возвращено:**\n```{str(output)[:3900]}```")
        async for i in slicer(str(output)[3900:], 3900):
            await msg.reply(f"```{i}```")
    else:
        await msg.edit(f"**Код:**```\n{escape(args)}```\n\n"f"**Возвращено:**\n```MESSAGE_TOO_LONG```")
    sys.stdout = old_stdout


async def getattrs(app, msg):
    return {"reply": msg.reply_to_message,
            "msg": msg,
            "app": app,
            "chat": msg.chat,
            "message": msg,
            "client": app,
            "input": MyInput,
            "quoting": msg.reply_to_message,
            "attrs": Attrs()
            }
