import datetime, time
import asyncio
import pytz
from pyrogram import Client, filters
from PIL import Image, ImageDraw, ImageFont

class Main:
	author = "Написал Кобан, идею взял у Пельменя"
	ver = 1.2
	des = "Настоящее время будет выводиться на аве (UTC+3)"
	cmd_list = {"phtime": "запустить часы",
	"ph": "включить/выключить часы"}

IS_ENABLE = True


async def delete_photo(app):
	my_photo = await app.get_profile_photos("me")
	last_photo = my_photo[1]
	last_photo_date = last_photo.date
	photo_file_id = last_photo.file_id
	now_time = time.time()
	if now_time - last_photo_date < 80:
		await app.delete_profile_photos(photo_file_id)


async def get_photo(now_time: str):
	font = ImageFont.truetype("downloads/NixieOne-Regular.ttf", 300)
	W,H = 1024,1024
	img = Image.new("RGB", (W,H), "black")
	drawer = ImageDraw.Draw(img)
	w,h = font.getsize(now_time)
	drawer.text(((W-w)/2, (H-h)/2), now_time, font = font,fill = "#f7b14b")
	img.save("downloads/phototime.png")
	return "downloads/phototime.png"

@Client.on_message(filters.me & filters.command("ph", Client.prefix))
async def start_stop_photo(app, msg):
	global IS_ENABLE
	if IS_ENABLE:
		IS_ENABLE = False
		await msg.edit("**Часы выключены**")
	else:
		IS_ENABLE = False
		await msg.edit("**Часы включены**")

@Client.on_message(filters.me & filters.command("phtime", Client.prefix))
async def photo_time(app, msg):
	global IS_ENABLE
	await msg.delete()	
	old_time = 0
	while IS_ENABLE:
		if not IS_ENABLE:
			break
		tz = pytz.timezone("Europe/Moscow")
		now = datetime.datetime.now(tz)
		now_time = str(now.strftime("%H:%M"))
		if now_time != old_time:
			photo = await get_photo(now_time)
			await app.set_profile_photo(photo = photo)
			await delete_photo(app)
			old_time = now_time

		await asyncio.sleep(3)