import telebot
from telebot import types
import schedule
import time
import threading
import random
import os

TOKEN = "8096569593:AAHx_7ONfgQgsOOtOiC1HMzcb9boQemZZ-A"
bot = telebot.TeleBot(TOKEN)

user_schedules = {}
reminder_messages = {
    'daily': "⏰ Час зробити важливу справу!",
    'custom': "Нагадування від вашого бота!"
}

def send_scheduled_message(chat_id, message_text):
    try:
        bot.send_message(chat_id, message_text)
    except Exception as e:
        print(f"Помилка відправки повідомлення нагадування для {chat_id}: {e}")

@bot.message_handler(func=lambda message: message.text == "Щоденні нагадування")
def call_set_daily_reminder(message):
    set_daily_reminder(message)

@bot.message_handler(func=lambda message: message.text == "Нагадування за інтервалом")
def call_set_interval_reminder(message):
    set_interval_reminder(message)

@bot.message_handler(func=lambda message: message.text == "Скасувати всі нагадування")
def call_cancel_all_reminders(message):
    cancel_all_reminders(message)

@bot.message_handler(commands=['remind_daily'])
def set_daily_reminder(message):
    chat_id = message.chat.id
    try:
        bot.send_message(chat_id, "Введіть час для щоденних нагадувань у форматі ГГ:ХХ (наприклад, 09:00, 18:00). Розділяйте кілька часів комами.")
        bot.register_next_step_handler(message, process_daily_reminder_times)
    except Exception as e:
        bot.send_message(chat_id, f"Виникла помилка: {e}")

def process_daily_reminder_times(message):
    chat_id = message.chat.id
    times_str = message.text.strip()
    times = [t.strip() for t in times_str.split(',')]

    if chat_id not in user_schedules:
        user_schedules[chat_id] = {}

    for job_id, job in list(user_schedules[chat_id].items()):
        if job.tags and 'daily_reminder' in job.tags:
            schedule.cancel_job(job)
            del user_schedules[chat_id][job_id]

    valid_times = []
    for t_str in times:
        try:
            if len(t_str) == 5 and t_str[2] == ':' and t_str[:2].isdigit() and t_str[3:].isdigit():
                valid_times.append(t_str)
            else:
                bot.send_message(chat_id, f"Неправильний формат часу: {t_str}. Використовуйте ГГ:ХХ.")
        except ValueError:
            bot.send_message(chat_id, f"Неправильний час: {t_str}. Будь ласка, введіть дійсний час.")

    if not valid_times:
        bot.send_message(chat_id, "Не вдалося встановити щоденні нагадування. Перевірте формат часу.")
        return

    for t in valid_times:
        job = schedule.every().day.at(t).do(send_scheduled_message, chat_id, reminder_messages['daily'])
        job.tag('daily_reminder')
        user_schedules[chat_id][job.job_id] = job
        bot.send_message(chat_id, f"Щоденне нагадування встановлено на {t}.")
    bot.send_message(chat_id, "Ваші щоденні нагадування оновлено!")

@bot.message_handler(commands=['remind_interval'])
def set_interval_reminder(message):
    chat_id = message.chat.id
    try:
        bot.send_message(chat_id, "Введіть інтервал для нагадувань у секундах (наприклад, 3600 для щогодини).")
        bot.register_next_step_handler(message, process_interval_reminder_time)
    except Exception as e:
        bot.send_message(chat_id, f"Виникла помилка: {e}")

def process_interval_reminder_time(message):
    chat_id = message.chat.id
    try:
        interval = float(message.text.strip())
        if interval <= 0:
            raise ValueError("Інтервал повинен бути позитивним числом.")

        if chat_id not in user_schedules:
            user_schedules[chat_id] = {}

        for job_id, job in list(user_schedules[chat_id].items()):
            if job.tags and 'interval_reminder' in job.tags:
                schedule.cancel_job(job)
                del user_schedules[chat_id][job_id]

        job = schedule.every(interval).seconds.do(send_scheduled_message, chat_id, reminder_messages['custom'])
        job.tag('interval_reminder')
        user_schedules[chat_id][job.job_id] = job
        bot.send_message(chat_id, f"Нагадування встановлено кожні {interval} секунд.")
    except ValueError:
        bot.send_message(chat_id, "Будь ласка, введіть дійсне число для інтервалу.")
    except Exception as e:
        bot.send_message(chat_id, f"Виникла помилка при встановленні інтервалу: {e}")

@bot.message_handler(commands=['cancel_reminders'])
def cancel_all_reminders(message):
    chat_id = message.chat.id
    if chat_id in user_schedules:
        for job_id, job in list(user_schedules[chat_id].items()):
            schedule.cancel_job(job)
            del user_schedules[chat_id][job_id]
        bot.send_message(chat_id, "Усі ваші нагадування скасовано.")
    else:
        bot.send_message(chat_id, "У вас немає активних нагадувань.")

def run_scheduler():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print(f"Помилка в планувальнику: {e}")
            time.sleep(5)

UPLOAD_FOLDER = "memes/"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

memes = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

@bot.message_handler(content_types=['photo'])
def receive_meme(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        file_extension = file_info.file_path.split('.')[-1]
        file_name = f"meme_{int(time.time())}_{random.randint(100, 999)}.{file_extension}"

        with open(os.path.join(UPLOAD_FOLDER, file_name), 'wb') as new_file:
            new_file.write(downloaded_file)
        memes.append(file_name)
        bot.reply_to(message, "Мем збережено!")
    except Exception as e:
        bot.reply_to(message, f"Виникла помилка при збереженні мему: {e}")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):
    if memes:
        meme_file = random.choice(memes)
        try:
            with open(os.path.join(UPLOAD_FOLDER, meme_file), 'rb') as photo:
                bot.send_photo(message.chat.id, photo)
        except FileNotFoundError:
            bot.reply_to(message, "Вибачте, цей мем не знайдено.")
            memes.remove(meme_file)
        except Exception as e:
            bot.reply_to(message, f"Виникла помилка при відправці мему: {e}")
    else:
        bot.reply_to(message, "Мемів поки немає. Надішліть мені кілька, щоб почати!")

CORRECT_CODE = '395'
SUCCESS_MESSAGE = 'Молодець, ти це зробив!'
VIDEO_PATH = 'C:\\Users\\user\\Desktop\\video1.mp4'
if not os.path.exists(VIDEO_PATH):
    print(f"ПОПЕРЕДЖЕННЯ: Відеофайл за шляхом {VIDEO_PATH} не знайдено. Функція гри 'Вгадай код' може не працювати.")

@bot.message_handler(commands=['guess_code'])
def start_guess_code_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Скасувати"))
    bot.send_message(message.chat.id, 'Введи тризначний код:', reply_markup=markup)
    bot.register_next_step_handler(message, check_code_game)

@bot.message_handler(func=lambda message: message.text == "Скасувати")
def cancel_current_action(message):
    bot.send_message(message.chat.id, "Дію скасовано.", reply_markup=types.ReplyKeyboardRemove())
    send_welcome(message)

def check_code_game(message):
    if message.text == CORRECT_CODE:
        bot.send_message(message.chat.id, SUCCESS_MESSAGE, reply_markup=types.ReplyKeyboardRemove())
        try:
            with open(VIDEO_PATH, 'rb') as video:
                bot.send_video(message.chat.id, video)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "На жаль, відео не знайдено. Перевірте шлях до файлу.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Виникла помилка при відправці відео: {e}")
        send_welcome(message)
    elif message.text == "Скасувати":
        cancel_current_action(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Скасувати"))
        bot.send_message(message.chat.id, 'Неправильний код. Спробуй ще раз:', reply_markup=markup)
        bot.register_next_step_handler(message, check_code_game)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_guess = types.KeyboardButton("Вгадай код")
    item_alarm = types.KeyboardButton("Будильник")
    item_memes = types.KeyboardButton("Меми")

    markup.add(item_guess, item_alarm, item_memes)

    bot.send_message(message.chat.id, "Чим хочете зайнятися?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_text_messages(message):
    if message.text == "Вгадай код":
        start_guess_code_game(message)
    elif message.text == "Будильник":
        alarm_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        alarm_markup.add(types.KeyboardButton("Щоденні нагадування"))
        alarm_markup.add(types.KeyboardButton("Нагадування за інтервалом"))
        alarm_markup.add(types.KeyboardButton("Скасувати всі нагадування"))
        alarm_markup.add(types.KeyboardButton("Головне меню"))
        bot.send_message(message.chat.id, "Оберіть опцію будильника:", reply_markup=alarm_markup)
    elif message.text == "Меми":
        send_random_meme(message)
        main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        main_menu_markup.add(types.KeyboardButton("Головне меню"))
        bot.send_message(message.chat.id, "Ось ваш мем! Для нового мему натисніть /meme, або поверніться в головне меню.", reply_markup=main_menu_markup)
    elif message.text == "Головне меню":
        send_welcome(message)

def main():
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    print("Бот запущено...")
    bot.polling(non_stop=True)

if __name__ == "__main__":
    main()




