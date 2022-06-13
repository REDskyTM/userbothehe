from pyrogram import Client, filters
from pyrogram import types

import asyncio
import time
import random


@Client.on_message(filters.me & filters.command("test","."))
async def testt_cmd(app, message):
	await message.edit_text('ХАХАХАХАХА ЭТО ГОВНО РАБОТАЕТ')