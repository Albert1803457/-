import telebot
import hashlib

# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('7931810181:AAGOMuRzs-h4HHJkq4fChb71hVkuQ5pxLgA')

# Команда /start: відправляє привітання
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот, для початку натисни /help щоб ознайомитись з командами😉")

# Команда /help: відправляє підказки
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "В мене є список команд: /start, /help, /length <текст>, /encrypt <текст>")

# Команда /encrypt: хешує повідомлення
@bot.message_handler(commands=['encrypt'])
def send_encrypt(message):
    text = message.text[9:]  # Вилучаємо "/encrypt " з команди
    if not text:
        bot.reply_to(message, "Будь ласка, введи текст для хешування. Наприклад: /encrypt hello")
        return

    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    bot.reply_to(message, f"SHA-256 хеш: {hex_dig}")

# Команда /length: визначає довжину тексту
@bot.message_handler(commands=['length'])
def get_length(message):
    text = message.text[8:]  # Вилучаємо "/length " з команди
    if not text:
        bot.reply_to(message, "Будь ласка, введи текст для визначення довжини. Наприклад: /length hello world")
        return

    length = len(text)
    bot.reply_to(message, f"Довжина введеного тексту: {length} символів")

# Запуск бота
bot.polling()