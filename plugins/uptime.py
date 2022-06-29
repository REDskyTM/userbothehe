import os
from pyrogram import Client, filters, types
from m2h import Sec2Hum


class Help:
    des = 'Показывает время работы бота'
    ver = '2.0'
    in_help = "upt"
    author = "Chaos, Koban"
    cmd_list = {
        'upt': 'узнать время работы бота'
    }


@Client.on_message(filters.me & filters.command("upt", "."))
async def uptime_handler(_, msg: types.Message):
    timer = os.popen("cat /proc/uptime").read()
    timer = float(timer.split()[0])
    result = Sec2Hum(timer)
    await msg.edit_text(f"Бот работает: <b><i>{result}</i></b>")
