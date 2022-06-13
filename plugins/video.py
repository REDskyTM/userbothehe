from pyrogram import Client, filters
from pyrogram import types

import asyncio
import time
import random
import os


@Client.on_message(filters.me & filters.command("video","."))
async def videoo_cmd(app, message):
	await message.reply_video_note("./downloads/video.mp4")