import telebot
from telebot import types
import secrets
import string
BOT_TOKEN = '8671664616:AAFI1-LPZxzvO0bgRl_WpYrrRwpOQbHdCUg'
bot = telebot.TeleBot(BOT_TOKEN)

# --- ФУНКЦИЯ ГЕНЕРАЦИИ ---
def generate_password(length):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for i in range(length))

# --- 1. СТАРТ И КНОПКА ---
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    # Кнопка теперь вызывает функцию настройки длины
    btn = types.InlineKeyboardButton("🔐 Настроить длину пароля", callback_data="set_length")
    markup.add(btn)
    
    bot.send_message(message.chat.id, "Привет! Я бот для генерации паролей.", reply_markup=markup)

# --- 2. ОБРАБОТКА НАЖАТИЯ НА КНОПКУ ---
@bot.callback_query_handler(func=lambda call: call.data == "set_length")
def ask_length(call):
    # Просим пользователя ввести число
    msg = bot.send_message(call.message.chat.id, "Введите длину пароля (число от 8 до 50):")
    
    # ВАЖНО: Регистрируем следующий шаг. 
    # Когда пользователь ответит сообщением, сработает функция process_length_input
    bot.register_next_step_handler(msg, process_length_input)

# --- 3. ОБРАБОТКА ВВОДА ДЛИНЫ ---
def process_length_input(message):
    try:
        length = int(message.text)
        
        # Проверка на разумные пределы
        if 8 <= length <= 50:
            password = generate_password(length)
            bot.send_message(message.chat.id, f"🔐 Ваш пароль:\n`{password}`", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "❌ Длина должна быть от 8 до 50. Введите /start для начала.")
            
    except ValueError:
        # Если ввели не число
        bot.send_message(message.chat.id, "❌ Это не число! Введите /start для начала.")

# Запуск
print("Бот запущен...")
bot.polling(none_stop=True)