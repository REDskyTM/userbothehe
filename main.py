from pyrogram import Client, filters
import os

plugins = dict(root="plugins")

id = '3124927'
hash = 'fdb6d907685bd444efabd9bc2697b4cc'

app = Client(
    "my_account",
    api_id=id,
		api_hash=hash,
    plugins = plugins
)

@app.on_message(filters.me & filters.command("add", "."))
def module_adder(app, msg):
	try:
		name = msg.text.split(" ", 1)[1]
		text = msg.reply_to_message.text
		f = open(f"plugins/{name}.py","w+")
		f.write(text)
		app.restart(False)
		msg.edit("**Успешно**")
	except:
		pass

@app.on_message(filters.command("send", prefixes=".") & filters.me)
async def send_cmd(app, msg):
    file_name = msg.text.split(maxsplit=1)[1].replace(' ', '/')
    if os.path.exists(file_name):
        await msg.reply_document(file_name)
        return await msg.delete()
    await msg.edit_text('<i>Нет такого файла</i>')

app.run()
