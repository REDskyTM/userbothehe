from pyrogram import Client, filters
from pyrogram import types

import asyncio
import time
import random


@Client.on_message(filters.me & filters.command("love","."))
async def love_cmd(app, message):
	stroka1 = ['β€οΈ', 'π§‘', 'π', 'π', 'π', 'π', 'π€', 'β€οΈβπ₯', 'π']
	stroka2 = ['Π’Ρ ΡΠ°ΠΌΠΎΠ΅ Π΄ΠΎΡΠΎΠ³ΠΎΠ΅ ΡΡΠΎ Ρ ΠΌΠ΅Π½Ρ Π΅ΡΡΡ β€οΈ', 'Π‘ΠΏΠ°ΡΠΈΠ±ΠΎ ΡΠΎ ΡΡΠΎ ΡΡ ΡΠΎ ΠΌΠ½ΠΎΠΉ β€οΈ', 'ΠΠ΅Π· ΡΠ΅Π±Ρ ΠΌΠΎΡ ΠΆΠΈΠ·Π½Ρ ΡΠ»ΠΈΡΠΊΠΎΠΌ ΡΠΊΡΡΠ½Π°Ρ β€οΈ']
	await message.edit_text(random.choice(stroka2))
	time.sleep(2)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€β€οΈπ€π€β€οΈπ€π€β€οΈπ€
π€β€οΈπ€π€π€π€π€β€οΈπ€
π€β€οΈπ€π€π€π€π€β€οΈπ€
π€π€β€οΈπ€π€π€β€οΈπ€π€
π€π€π€β€οΈπ€β€οΈπ€π€π€
π€π€π€π€β€οΈπ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€β€οΈπ€π€β€οΈπ€π€β€οΈπ€
π€β€οΈπ€π€β€οΈπ€π€β€οΈπ€
π€β€οΈπ€π€β€οΈπ€π€β€οΈπ€
π€π€β€οΈπ€β€οΈπ€β€οΈπ€π€
π€π€π€β€οΈβ€οΈβ€οΈπ€π€π€
π€π€π€π€β€οΈπ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€β€οΈππβ€οΈππβ€οΈπ€
π€β€οΈππβ€οΈππβ€οΈπ€
π€β€οΈππβ€οΈππβ€οΈπ€
π€π€β€οΈπβ€οΈπβ€οΈπ€π€
π€π€π€β€οΈβ€οΈβ€οΈπ€π€π€
π€π€π€π€β€οΈπ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€β€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈπ€
π€β€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈπ€
π€β€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈβ€οΈπ€
π€π€β€οΈβ€οΈβ€οΈβ€οΈβ€οΈπ€π€
π€π€π€β€οΈβ€οΈβ€οΈπ€π€π€
π€π€π€π€β€οΈπ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€π§‘π§‘π€π§‘π§‘π€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€π€π§‘π§‘π§‘π§‘π§‘π€π€
π€π€π€π§‘π§‘π§‘π€π€π€
π€π€π€π€π§‘π€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€πππ€πππ€π€
π€ππππππππ€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€πππ€πππ€π€
π€ππππππππ€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€πππ€πππ€π€
π€ππππππππ€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€πππ€πππ€π€
π€ππππππππ€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€ππππππππ€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€β€οΈβ€οΈπ€β€οΈβ€οΈπ€π€
π€π§‘π§‘π§‘π§‘π§‘π§‘π§‘π€
π€ππππππππ€
π€ππππππππ€
π€π€ππππππ€π€
π€π€π€ππππ€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€πππ€πππ€π€
π€ππβ€οΈπβ€οΈπ€β€οΈβπ₯π€
π€π€β€οΈππ€ππππ€
π€β€οΈπππππβ€οΈβπ₯π€
π€π€πππ€πππ€π€
π€π€π€πβ€οΈπ§‘π€π€π€
π€π€π€π€ππ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text("""π€π€π€π€π€π€π€π€π€
π€π€ππ€π€π€ππ€π€
π€πβ€οΈβπ©Ήπππππ§‘π€
π€ππ€β€οΈπππβ€οΈπ€
π€β€οΈβπ©Ήπ€β€οΈππππ€π€
π€π€πβ€οΈπβ€οΈππ€π€
π€π€π€π§‘β€οΈβπ₯ππ€π€π€
π€π€π€π€β€οΈπ€π€π€π€
π€π€π€π€π€π€π€π€π€""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")
	time.sleep(1)
	await message.edit_text(f"""
π€π€π€π€π€π€π€π€π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}π€{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€
π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€
π€π€π€{random.choice(stroka1)}{random.choice(stroka1)}{random.choice(stroka1)}π€π€π€
π€π€π€π€{random.choice(stroka1)}π€π€π€π€
π€π€π€π€π€π€π€π€π€
""")