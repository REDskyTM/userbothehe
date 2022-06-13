from pyrogram import Client, filters
from pyrogram import types

import asyncio
import time
import random


@Client.on_message(filters.me & filters.command("love","."))
async def love_cmd(app, message):
	stroka1 = ['❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '❤️‍🔥', '💖']
	stroka2 = ['Ты самое дорогое что у меня есть ❤️', 'Спасибо то что ты со мной ❤️', 'Без тебя моя жизнь слишком скучная ❤️']
	await message.edit_text(random.choice(stroka2))
	time.sleep(2)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️🤍🤍🤍🤍🤍❤️🤍
🤍❤️🤍🤍🤍🤍🤍❤️🤍
🤍🤍❤️🤍🤍🤍❤️🤍🤍
🤍🤍🤍❤️🤍❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍❤️🤍🤍❤️🤍🤍❤️🤍
🤍🤍❤️🤍❤️🤍❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️💜💜❤️💜💜❤️🤍
🤍❤️💜💜❤️💜💜❤️🤍
🤍❤️💜💜❤️💜💜❤️🤍
🤍🤍❤️💜❤️💜❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🧡🤍🧡🧡🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🤍🧡🧡🧡🧡🧡🤍🤍
🤍🤍🤍🧡🧡🧡🤍🤍🤍
🤍🤍🤍🤍🧡🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💛💛🤍🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍🤍💛💛💛💛💛🤍🤍
🤍🤍🤍💛💛💛🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💚💚🤍💚💚🤍🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💚💚💚💚💚🤍🤍
🤍🤍🤍💚💚💚🤍🤍🤍
🤍🤍🤍🤍💚🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💜💜🤍💜💜🤍🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍💛💛💛💛💛💛💛🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍💛💛💛💛💛💛💛🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍💛💛💛💛💛💛💛🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍💛💛💛💛💛💛💛🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💖🤍💚💝🤍🤍
🤍💚💙❤️💓❤️🖤❤️‍🔥🤍
🤍🖤❤️💙🤎💙💛💓🤍
🤍❤️💛💙💗💕💚❤️‍🔥🤍
🤍🤍💜💖🖤💜💛🤍🤍
🤍🤍🤍💙❤️🧡🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💜🤎🤍🖤💛🤍🤍
🤍💓❤️‍🩹💛💓💚💜🧡🤍
🤍💘🖤❤️💗💖💝❤️🤍
🤍❤️‍🩹🤎❤️💞💙💜🖤🤍
🤍🤍💞❤️💛❤️💚🤍🤍
🤍🤍🤍🧡❤️‍🔥💜🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")
	time.sleep(1)
	await message.edit_text(f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍
🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍
🤍🤍🤍{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}🤍🤍🤍
🤍🤍🤍🤍{random.choice(stroka1)}🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍
""")