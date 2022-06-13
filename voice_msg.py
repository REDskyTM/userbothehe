from pyrogram import Client, filters
import os
os.popen("pip install gtts")
from gtts import gTTS

@Client.on_message(filters.me & filters.command('voice', '.'))
async def func(app, msg):
 try:
  await msg.delete()
  text = msg.text.split(maxsplit=1)[1]
  language = 'ru'
  speech = gTTS(text = text, lang = language, slow = False)
  speech.save("downloads/module_voice.mp3")
  await app.send_voice(msg.chat.id, "downloads/module_voice.mp3", caption=f"**Текст голосового сообщения:**\n{text}")
 except IndexError:
    await msg.edit("**Напишите текст голосового сообщения после команды!**")