import datetime, time
import requests
import asyncio
import pytz
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps
import tracemalloc
from pyrogram import Client, filters, types
import textwrap
tracemalloc.start()

class Main:
  author = "Написал Кулич"
  ver = 2.0
  des = "Выводит инфо о юзере в виде карточки"
  cmd_list = {"uinfo": "получить карточку"}

FONT = BytesIO(requests.get("https://github.com/youngtitanium/dexter/blob/master/modules/gen_mac_window/fonts/jet.ttf?raw=true").content)

@Client.on_message(filters.me & filters.command("uinfo", "."))
async def uinfo_card(app, msg: types.Message):
    await msg.edit("**Получаю информацию**")
    path = await app.download_media((await app.get_profile_photos(msg.reply_to_message.from_user.id))[0], file_name="./avatar.png")
    img = Image.new('RGBA', (500, 300), '#232529')
    avatar = Image.open(path).resize((100, 100), Image.ANTIALIAS)
    # Create the circle mask
    mask = Image.new('L', avatar.size)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + avatar.size, fill=255)
    img.paste(avatar, (15, 15, 115, 115), mask)
    file = BytesIO()
    file.name = "some.png"

    idraw = ImageDraw.Draw(img)
    name = msg.reply_to_message.from_user.first_name
    tag = msg.reply_to_message.from_user.username
    ids = msg.reply_to_message.from_user.id
    status = (await app.get_chat(ids)).bio

    a = msg.reply_to_message.from_user.is_bot
    if a is True:
      a = "✓"
    else:
      a = "✗"
      
    scam = msg.reply_to_message.from_user.is_scam
    if scam is True:
      scam = "✓"
    else:
      scam = "✗"
      
    verif = msg.reply_to_message.from_user.is_verified
    if verif is True:
      verif = "✓"
    else:
      verif = "✗"
      
    r = msg.reply_to_message.from_user.is_contact
    if r is True:
      r = "✓"
    else:
      r = "✗"
      
    e = msg.reply_to_message.from_user.status
    g = "recently"
    m = "online"
    if e == g:
      e = "Недавно"
    elif e == m:
      e = " ✓"
    else:
      e = "✗"

    headline = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 20)
    idss = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 17)
    botnet = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 17)
    scummer = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 17)
    verifys = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 17)
    onlinestat = ImageFont.truetype(BytesIO(requests.get("https://github.com/REDskyTM/fontforuserbot/blob/main/DejaVuSans.ttf?raw=true").content), size = 17)
    

    idraw.text((125, 15), f'{name}\n{tag}', font = headline)
    idraw.text((125, 75), f'ID: {ids}', font = idss)
    idraw.text((125, 85), f'Бот: {a}', font = botnet)
    idraw.text((125, 95), f'Скам: {scam}', font = scummer)
    idraw.text((125, 105), f'Верификация: {verif}', font = verifys)
    idraw.text((125, 125), f'Онлайн: {e}', font = onlinestat) 

    img.save('downloads/user_card.png')
    #photo = open('/downloads/photo.png', 'rb')
    await msg.edit("**Информация получена**")
    await app.send_photo(msg.chat.id, "downloads/user_card.png")