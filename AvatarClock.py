import datetime, time
import requests
import asyncio
import pytz
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from pyrogram import Client, filters, types

class Main:
	author = "Написал Кобан, идею взял у Пельменя, помог Аладин."
	ver = 2.0
	des = "Настоящее время будет выводиться на аве (UTC+3)"
	cmd_list = {"clock-start": "запустить часы",
	"clock-off": "выключить часы"}

IS_ENABLE = True

FONT = BytesIO(requests.get("https://github.com/youngtitanium/dexter/blob/master/modules/gen_mac_window/fonts/jet.ttf?raw=true").content)

async def delete_photo(app):
	my_photos = await app.get_profile_photos("me")
	if len(my_photos) < 1:
		return
	last_photo = my_photos[0]
	last_photo_date = last_photo.date
	photo_file_id = last_photo.file_id
	now_time = time.time()
	if now_time - last_photo_date < 80:
		await app.delete_profile_photos(photo_file_id)


def gen_photo(now_time: str):
	global FONT
	font = ImageFont.truetype(FONT, 300)
	FONT.seek(0)
	W,H = 1024,1024
	img = Image.new("RGB", (W,H), "black")
	drawer = ImageDraw.Draw(img)
	w,h = font.getsize(now_time)
	drawer.text(((W-w)//2, (H-h)//2), now_time, font = font,fill = "#f7b14b")
	avatar = BytesIO()
	avatar.name = "avatar-time.png"
	img.save(avatar)
	return avatar

@Client.on_message(filters.me & filters.command("clock-off", "."))
async def toggle_clock(_, msg: types.Message):
	global IS_ENABLE
	if IS_ENABLE:
		IS_ENABLE = False
		await msg.edit("**Часы выключены**")
	else:
		await msg.edit("**Часы уже выключены**")

@Client.on_message(filters.me & filters.command("clock-start", "."))
async def photo_time(app, msg: types.Message):
	await msg.delete()	
	old_time = 0
	global IS_ENABLE
	IS_ENABLE = True
	tz = pytz.timezone("Europe/Kiev")
	while IS_ENABLE:
		now = datetime.datetime.now(tz)
		now_time = str(now.strftime("%H:%M"))
		if now_time != old_time:
			await delete_photo(app)
			await app.set_profile_photo(photo=gen_photo(now_time))
			old_time = now_time
import datetime, time
import requests
import asyncio
import pytz
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from pyrogram import Client, filters, types

class Main:
	author = "Написал Кобан, идею взял у Пельменя, помог Аладин."
	ver = 2.0
	des = "Настоящее время будет выводиться на аве (UTC+3)"
	cmd_list = {"clock-start": "запустить часы",
	"clock-off": "выключить часы"}

IS_ENABLE = True

FONT = BytesIO(requests.get("https://github.com/youngtitanium/dexter/blob/master/modules/gen_mac_window/fonts/jet.ttf?raw=true").content)

async def delete_photo(app):
	my_photos = await app.get_profile_photos("me")
	if len(my_photos) < 1:
		return
	last_photo = my_photos[0]
	last_photo_date = last_photo.date
	photo_file_id = last_photo.file_id
	now_time = time.time()
	if now_time - last_photo_date < 80:
		await app.delete_profile_photos(photo_file_id)


def gen_photo(now_time: str):
	global FONT
	font = ImageFont.truetype(FONT, 300)
	FONT.seek(0)
	W,H = 1024,1024
	img = Image.new("RGB", (W,H), "black")
	drawer = ImageDraw.Draw(img)
	w,h = font.getsize(now_time)
	drawer.text(((W-w)//2, (H-h)//2), now_time, font = font,fill = "#f7b14b")
	avatar = BytesIO()
	avatar.name = "avatar-time.png"
	img.save(avatar)
	return avatar

@Client.on_message(filters.me & filters.command("clock-off", "."))
async def toggle_clock(_, msg: types.Message):
	global IS_ENABLE
	if IS_ENABLE:
		IS_ENABLE = False
		await msg.edit("**Часы выключены**")
	else:
		await msg.edit("**Часы уже выключены**")

@Client.on_message(filters.me & filters.command("clock-start", "."))
async def photo_time(app, msg: types.Message):
	await msg.delete()	
	old_time = 0
	global IS_ENABLE
	IS_ENABLE = True
	tz = pytz.timezone("Europe/Kiev")
	while IS_ENABLE:
		now = datetime.datetime.now(tz)
		now_time = str(now.strftime("%H:%M"))
		if now_time != old_time:
			await delete_photo(app)
			await app.set_profile_photo(photo=gen_photo(now_time))
			old_time = now_time

		await asyncio.sleep(3)
		await asyncio.sleep(3)