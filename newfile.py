import os
import csv
import re
import time
import requests
import random
import json
import datetime
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telebot import TeleBot, types
from telethon.sync import TelegramClient
import asyncio

# إعدادات الاتصال لبوت TeleBot
BOT_TOKEN = '7321238928:AAFljwvUy_x0MQnYX7kAx4K1WfY77_U36_MN'
bot = TeleBot(BOT_TOKEN, parse_mode='HTML')

# إعدادات الاتصال لحساب Telethon
api_id = '28334196'
api_hash = 'dd3c4aa0133fb57ec9eef25252b2f266'
phone_number = '

# ملفات الكاش
cache_file = "bin_cache.json"
PREMIUM_FILE = "premium.txt"
IDs_file = 'IDs.csv'

# إعدادات إضافية
owner_id = '6898845629'
bot_working = True

# تحميل الكاش
if os.path.exists(cache_file):
    with open(cache_file, "r") as file:
        bin_cache = json.load(file)
else:
    bin_cache = {}

# دالة لحفظ الكاش
def save_cache():
    with open(cache_file, "w") as file:
        json.dump(bin_cache, file)

# ======= وظائف بوت TeleBot ======= #

@bot.message_handler(commands=["start"])
def send_welcome(message):
    name = message.from_user.first_name
    welcome_message = (
        f"Welcome, {name}!\n"
        "⌯ Welcome to bot scrap cc\n\n"
        "⇾ You can scrape from your username, ID, invitation link, or user chats\n"
        "⇾ You can scrape from bank name or bin\n"
        "⇾ You can scrape from more than one bank or bin, all you have to do is put ',' between them\n\n"
        "The commands are below 🧸"
    )
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("≈ CC SCRAPPING FROM CHAT ≈", callback_data='scrap_from_chat')
    button2 = types.InlineKeyboardButton("≈ CC SCRAPPING FROM BIN IN ALL USER CHATS ≈", callback_data='scrap_from_bin')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(commands=['scr'])
def send_scrape_messages(message):
    chat_id = message.chat.id
    initial_message = bot.reply_to(message, "Scraping Started...⏳")
    command_parts = message.text.split()

    if len(command_parts) < 3:
        bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="Command format: /scr [username/bin] [limit]")
        return

    input_data = command_parts[1]
    limit = int(command_parts[2])

    if input_data.isdigit() and len(input_data) >= 6:
        # Scrape by BIN
        bin = input_data
        cards = generate_cards(bin, limit)
        with open("Original_Scrap.txt", "w") as file:
            file.write("\n".join(cards))

        bin_info = get_bin_info(bin[:6])
        additional_info = (f'''
            • BIN ~ {bin[:10]}
            • Total Found ~ {limit}
        ''')

        with open("Original_Scrap.txt", "rb") as file:
            bot.send_document(chat_id, file, caption=additional_info)
            bot.delete_message(chat_id=chat_id, message_id=initial_message.message_id)
    else:
        # Scrape by username (using Telethon)
        username = input_data
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        messages_text, channel_name = loop.run_until_complete(get_last_messages(username, limit))

        if channel_name:
            save_to_file(messages_text)
            with open('Original_Scrap.txt', 'rb') as file:
                caption_info = f"• Channel ~ {channel_name}\n• Total Found ~ {len(messages_text.split())}"
                bot.send_document(chat_id, file, caption=caption_info)
                bot.delete_message(chat_id=chat_id, message_id=initial_message.message_id)
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=initial_message.message_id, text="Failed to scrape.")

# دالة لتوليد بطاقات
def generate_cards(bin, count):
    cards = set()
    while len(cards) < count:
        card_number = bin + str(random.randint(0, 10**(16-len(bin)-1) - 1)).zfill(16-len(bin))
        if luhn_check(card_number):
            expiry_date = generate_expiry_date()
            cvv = str(random.randint(0, 999)).zfill(3)
            card = f"{card_number}|{expiry_date['month']}|{expiry_date['year']}|{cvv}"
            cards.add(card)
    return list(cards)

# دالة لحساب Luhn Check
def luhn_check(number):
    digits = [int(d) for d in str(number)]
    checksum = sum(digits[-1::-2]) + sum(sum(divmod(d * 2, 10)) for d in digits[-2::-2])
    return checksum % 10 == 0

# دالة لتوليد تاريخ انتهاء
def generate_expiry_date():
    current_year = datetime.datetime.now().year % 100
    current_month = datetime.datetime.now().month
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(current_year, current_year + 5)).zfill(2)
    return {"month": month, "year": year}

# دالة للحصول على معلومات BIN
def get_bin_info(bin):
    if bin in bin_cache:
        return bin_cache[bin]
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin[:6]}")
        response.raise_for_status()
        data = response.json()
        info = {
            "scheme": data.get("scheme", "").upper(),
            "type": data.get("type", "").upper(),
            "brand": data.get("brand", "").upper(),
            "bank": data.get("bank", {}).get("name", "").upper(),
            "country": data.get("country", {}).get("name", "").upper(),
            "emoji": data.get("country", {}).get("emoji", "")
        }
        bin_cache[bin] = info
        save_cache()
        return info
    except Exception as e:
        print(f"Error fetching BIN info: {e}")
        return {}

# دالة لحفظ البيانات في ملف
def save_to_file(text):
    with open('Original_Scrap.txt', 'w') as file:
        file.write(text)

# ======= تشغيل البوت ======= #
bot.infinity_polling()
