from pyrogram import Client, filters

import json
import io
import os
import requests



strings = {
    "name": "YandexReverseSearch",
    "search": "⚪⚪⚪\n⚪❓⚪\n⚪⚪⚪",
    "no_reply": "<b>Reply to image or sticker!</b>",
    "result": '<a href="{}"><b>🔴⚪🔴|See</b>\n<b>⚪🔴⚪|Search</b>\n<b>⚪🔴⚪|Results</b></a>',
    "error": '<b>Something went wrong...</b>'
}

if 'get_string' not in globals():
    def get_string(string_id):
        return strings.get(string_id, 'None')



@Client.on_message(filters.me & filters.command('yars', '.'))
async def yarscmd(peluserbot, message):
    """.yars <repy to image>"""
    reply = message.reply_to_message
    data = await check_media(message, reply)
    if not data:
        await message.edit(get_string("no_reply"))
        return
    await message.edit(get_string("search"))

    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', data, 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)

    if response.ok:
        query_string = json.loads(response.content)['blocks'][0]['params']['url']
        link = searchUrl + '?' + query_string
        text = get_string("result").format(link)
        await message.edit(text)
    else:
        await message.edit(get_string("error"))



async def check_media(message, reply):
    if not reply or not reply.media:
        return

    data = reply.photo or reply.sticker
    if not data:
        return


    path = await message._client.download_media(data)
    img = io.BytesIO(open(path, 'rb').read())
    os.remove(path)
    return img
