import datetime, time
import requests
import asyncio
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from pyrogram import Client, filters, types

class Main:
    author = "Написал Кобан, идею взял у Пельменя, помог Аладин."
    ver = 2.0
    des = "Настоящее время будет выводиться на аве"
    cmd_list = {
        "clock-start[ offset]": "запустить часы. offset — смещение по utc",
        "clock-off": "выключить часы"
    }

IS_ENABLE = True

#FONT = BytesIO(requests.get("https://github.com/youngtitanium/dexter/blob/master/modules/gen_mac_window/fonts/jet.ttf?raw=true").content)

FONT = BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/fontti.TTF?raw=true").content)

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


def gen_photo(now: datetime.datetime):
    global FONT
    # Вывод текущего времени
    font = ImageFont.truetype(FONT,370)
    FONT.seek(0)
    W,H = 1024,1024
    img = Image.new("RGB", (W,H), "black")
    drawer = ImageDraw.Draw(img)
    w,h = font.getsize(now.strftime("%H:%M"))
    drawer.text(((W-w)//2, (H-h)//2), now.strftime("%H:%M"), font=font, fill="#f7b14b")

    # Вывод текущей даты
    date_font = ImageFont.truetype(FONT, size = 200)
    FONT.seek(0)
    date = now.strftime("%d.%m.%Y")
    w, _ = drawer.textsize(date, font=date_font)
    centerW, centerH = (W - w)//2, H//2 - 4 - h
    drawer.text((centerW, centerH), date, font=date_font)

    # Возврат файла
    avatar = BytesIO()
    avatar.name = "avatar-time.png"
    img.save(avatar)
    return avatar

@Client.on_message(filters.me & filters.command("clock-off", "."))
async def toggle_clock(app, msg: types.Message):
    global IS_ENABLE
    if IS_ENABLE:
        IS_ENABLE = False
        await delete_photo(app)
        await msg.edit("**Часы выключены**")
    else:
        await msg.edit("**Часы уже выключены**")

@Client.on_message(filters.me & filters.command("clock-start", "."))
async def photo_time(app, msg: types.Message):
    await msg.edit("Запуск систем...")
    offset = 6
    if len(msg.text.split()) > 1:
        try:
            offset = int(msg.text.split()[1])
        except:
            await msg.edit(
                "Смещение должно быть числом. "
                "Установлено стандартное значение — 2 (Украина)"
            )
    old_time = 0
    global IS_ENABLE
    IS_ENABLE = True
    await msg.edit("Часы запущены!")
    while IS_ENABLE:
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=offset)
        now_time = now.strftime("%H:%M")
        if now_time != old_time:
            await delete_photo(app)
            await app.set_profile_photo(photo=gen_photo(now))
            old_time = now_time

        await asyncio.sleep(3)