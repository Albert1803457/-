import telebot
from telebot import types
import random
import string

TOKEN = '7611417175:AAF9IDQ-5vJ_SxARcJ7Reofhm5ulN9GcxBY'

bot = telebot.TeleBot(TOKEN)

saved_data = {}

def generate_code():
    return ''.join(random.choices(string.digits, k=4))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    save_button = types.KeyboardButton('Зберегти інформацію') 
    help_button = types.KeyboardButton('/help') 
    markup.add(save_button, help_button)
    bot.send_message(message.chat.id, 'Ласкаво просимо! Ви можете зберегти інформацію та ввести код для її отримання. Повідомлення, яке ви зберегли, можна видалити, щоб приховати ваш текст і код від зайвих очей🤫', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'Цей бот дозволяє зберігати інформацію і отримувати до неї доступ за унікальним кодом. Код треба вводити вручну')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id

    if message.text == 'Зберегти інформацію':
        bot.send_message(chat_id, 'Напишіть текст, який ви хочете зберегти.')
        bot.register_next_step_handler(message, save_information)
    elif message.text in saved_data:

        bot.send_message(chat_id, f'Інформація за вашим кодом: {saved_data[message.text]}')
    else:
        bot.send_message(chat_id, 'Код не розпізнано. Спробуйте ще раз або збережіть нову інформацію.')

def save_information(message):
    chat_id = message.chat.id
    text_to_save = message.text
    access_code = generate_code()
    saved_data[access_code] = text_to_save
    bot.send_message(chat_id, f'Інформація збережена! Ваш код доступу: {access_code}')

bot.polling()
