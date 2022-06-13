from pyrogram import Client as app, filters

@app.on_message(filters.me & filters.command("user", "."), group = 8)
def us(app, msg):
	a = msg.reply_to_message.from_user.is_bot
	if a is True:
		a = "✅"
	else:
		a = "❌"
		
	scam = msg.reply_to_message.from_user.is_scam
	if scam is True:
		scam = "✅"
	else:
		scam = "❌"
		
	verif = msg.reply_to_message.from_user.is_verified
	if verif is True:
		verif = "✅"
	else:
		verif = "❌"
		
	r = msg.reply_to_message.from_user.is_contact
	if r is True:
		r = " ✅"
	else:
		r = "❌"
		
	e = msg.reply_to_message.from_user.status
	g = "recently"
	m = "online"
	if e == g:
		e = "**Недавно**"
	elif e == m:
		e = " ✅"
	else:
		e = "❌"
	msg.edit("**Узнаю информацию...**")
	msg.edit("**Отправляю информацию...**")
	app.send_photo(msg.chat.id, "downloads/test.png", caption=f"""
**В контактах:** {r}
**Имя:** {msg.reply_to_message.from_user.first_name}
**Фамилия:** {msg.reply_to_message.from_user.last_name}
**Тег:** @{msg.reply_to_message.from_user.username}
**ID:** {msg.reply_to_message.from_user.id}
**Бот:** {a}
**Скам:** {scam}
**Верифицированный:** {verif}
**В сети: **{e}""")
	msg.delete()
	
@app.on_message(filters.me & filters.command("perm","."), group = 10)
async def check_permissions(app,msg):
	permis = msg.chat.permissions
	send_msg = "✅" if permis.can_send_messages else "❌"
	send_media = "✅" if permis.can_send_media_messages else "❌"
	send_stickers = "✅" if permis.can_send_stickers else "❌"
	send_gif = "✅" if permis.can_send_animations else "❌"
	send_games = "✅" if permis.can_send_games else "❌"
	send_polls = "✅" if permis.can_send_polls else "❌"
	change_info = "✅" if permis.can_change_info else "❌"
	invite = "✅" if permis.can_invite_users else "❌"
	pin = "✅" if permis.can_pin_messages else "❌"
	await msg.edit(f"""
**Можно отправлять сообщения**: {send_msg}
**Можно отправлять медиа**: {send_media}
**Можно отправлять стикеры**: {send_stickers}
**Можно отправлять гиф**: {send_gif}
**Можно отправлять игры**: {send_games}
**Можно отправлять опросы**: {send_polls}
**Можно изменять информацию**: {change_info}
**Можно приглашать пользователей**: {invite}
**Можно закреплять сообщения**: {pin}""")
