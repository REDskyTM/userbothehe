# установленные модули
from googletrans import Translator, LANGUAGES
from pyrogram import Client as app, filters


class Help():
    des = "Переводит текст"
    in_help = ".trans"
    ver = 1.1
    author = "Chaos(@xlllukas), Whoami(@xllwhoami)"
    cmd_list = {
		"trans [изначальный язык] [язык, на который будет переведён ваш текст] [ваш текст]": "Перевод"
	}


@app.on_message(filters.me & filters.command("trans","."), group = 10)
async def bash_command(app, msg):
    tr = Translator()
    try:
        args = msg.text.split(' ', 3)[1:]
        res = tr.translate(args[2], src=LANGUAGES[args[0]], dest=LANGUAGES[args[1]])
        await msg.edit(f"**<| {res.src.upper()} --> {res.dest.upper()} |>**\n\n**{res.src.upper()}**:\n    __{args[2]}__\n**{res.dest.upper()}**:\n    __{res.text}__")
    except IndexError:
     await msg.reply("Вы не ввели язык или текст!\nПример импользования: .trans en(из) ru(на) Hello(текст)")