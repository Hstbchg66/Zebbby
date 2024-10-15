import re,telebot,random,os
from telethon.sync import TelegramClient

from telebot import types

import asyncio, datetime
from datetime import datetime
bot_token = "7321238928:AAFljwvUy_x0MQnYX7kAx4K1WfY77_U36_M"
admin_id = 6898845629
async def get_last_messages(username, limit, bin):
	api_id = 28334196
	api_hash = "dd3c4aa0133fb57ec9eef25252b2f266"
	phone_number = "+201288817278"

	async with TelegramClient(
		phone_number, 
		api_id, 
		api_hash) as client:
		try:
			username = int(username)
		except Exception:
			pass
		if isinstance(username, int):
			entity = username
			try:
				entity = await client.get_entity(username)
				name = entity.title
			except Exception:
				name = username
		else:
			entity = await client.get_entity(username)
			name = entity.title
		print(bin)
		messages = await client.get_messages(entity, limit=limit)
		
		matching_texts = []
		for message in messages:
			if not isinstance(message.text, (str, bytes)):
				pass
			card_pattern = r'(\d{15,16})[^0-9]+([0-9]{1,2})[^0-9]+([0-9]{2,4})[^0-9]+([0-9]{3,4})'
			try:
				match = re.search(
				card_pattern, message.text)
				if match:
					formatted_text =  f"{match.group(1)}|{match.group(2)}|{match.group(3)}|{match.group(4)}"
					print(formatted_text)
				else:
					formatted_text = None
			except Exception:
				formatted_text = None
			if formatted_text is not None and bin is None:
				matching_texts.append(formatted_text)
			elif formatted_text is not None and bin is not None:
				if formatted_text.startswith(bin):
					matching_texts.append(formatted_text)
		random.shuffle(matching_texts)
	return "\n".join(matching_texts),name
	
def save_to_file(text):
	if os.path.exists('combo.txt'):
		os.remove('combo.txt')
	with open('combo.txt', 'w') as file:
		file.write(text)

bot = telebot.TeleBot(bot_token, parse_mode='html')
print("Started")
bot.send_message(admin_id,"Started")

command_pattern = r'^(?:/|\.|)sc(?:\s+(.*))?$'
@bot.message_handler(regexp=command_pattern)#10
def send_sc_messages(message):
		chat_id = message.chat.id
		language = 'en'
		msg = """Scarping Started...⏳"""
		msg1 = ["Amount","Took","Source"]
		msg2 = """command format. Use /scr [username] [limit]"""
		if language == 'es':
			msg = """Raspado iniciado...⏳"""
			msg1 = ["Cantidad","Tomó","Fuente"]
			msg2 = """formato de comando. Utilice /scr [nombre de usuario] [límite]"""
		initial_message = bot.reply_to(message, msg)
		start_time = datetime.now()
		command_parts = message.text.split()
		if len(command_parts) == 4 and command_parts[0].endswith('sc') or len(command_parts) == 3 and command_parts[0].endswith('sc'):
			
			username = command_parts[1]
			limit = int(command_parts[2])
			try:bin = command_parts[3]
			except:bin = None
			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			
			messages_text = loop.run_until_complete(get_last_messages(username, limit, bin))
			
			save_to_file(messages_text[0])
			
			file_len = len(messages_text[0].split('\n'))
			end_time = datetime.now()
			time_taken_seconds = (end_time - start_time).total_seconds()
			time_taken_formatted = "{:.0f}".format(time_taken_seconds)
			captain_info = f"""
<==============>
• {msg1[2]} -» {messages_text[1]}
• {msg1[0]} -» {file_len}
• {msg1[1]} -» {time_taken_formatted}sec
<==============>"""
			with open('combo.txt', 'rb') as file:
				try:
					markup = types.InlineKeyboardMarkup()
					team_button = telebot.types.InlineKeyboardButton(text="Dev Team", url='https://t.me/telemex')
					dev_button = telebot.types.InlineKeyboardButton(text="Dev", url='https://t.me/E_2_7')
					markup.add(team_button,dev_button)
					bot.send_document(message.chat.id, file,caption=captain_info,parse_mode='none',reply_markup=markup)
					bot.delete_message(message_id=initial_message.message_id,chat_id=chat_id)
				except Exception as e:
					bot.edit_message_text(message_id=initial_message.message_id,chat_id=chat_id,text=f"An error has occurred, May The Channel Has No Cards To Scrap. {e}")
		else:
			bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text=msg2)

bot.infinity_polling()