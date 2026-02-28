import telebot
from telebot import types
import random

# Вставьте сюда свой токен
TOKEN = '7870137017:AAH9JAGbsppqvVhRYmLA2Qymld-Uy82ldHg'
bot = telebot.TeleBot(TOKEN)

# Список экологических заданий
eco_tasks = [
    "Задание 1: Соберите мусор в вашем районе.",
    "Задание 2: Посадите дерево или цветы.",
    "Задание 3: Участвуйте в акциях по очистке водоемов.",
    "Задание 4: Проводите время на природе и наблюдайте за экосистемой.",
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Получить задание")
    item2 = types.KeyboardButton("Помощь")
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Добро пожаловать в экологический бот! Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Получить задание")
def send_task(message):
    task = eco_tasks[random.randint(0,3)]
    bot.send_message(message.chat.id, task)

@bot.message_handler(func=lambda message: message.text == "Помощь")
def send_help(message):
    bot.send_message(message.chat.id, "Этот бот предоставляет экологические задания. Нажмите 'Получить задание', чтобы получить новое задание.")

# Запуск бота
bot.polling()
