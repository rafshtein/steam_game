import sqlite3
import telebot

# Токен бота
TOKEN = ''

# Создаем бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /add_game
@bot.message_handler(commands=['add_game'])
def add_game(message):
    bot.send_message(message.chat.id, 'Введите заголовок игры:')
    bot.register_next_step_handler(message, add_game_title)

def add_game_title(message):
    title = message.text
    bot.send_message(message.chat.id, 'Введите рейтинг игры:')
    bot.register_next_step_handler(message, lambda msg: add_game_rating(msg, title))

def add_game_rating(message, title):
    rating = message.text
    bot.send_message(message.chat.id, 'Введите дату релиза игры (в формате YYYY-MM-DD):')
    bot.register_next_step_handler(message, lambda msg: add_game_release_date(msg, title, rating))

def add_game_release_date(message, title, rating):
    release_date = message.text
    bot.send_message(message.chat.id, 'Введите краткое описание игры:')
    bot.register_next_step_handler(message, lambda msg: add_game_summary(msg, title, rating, release_date))

def add_game_summary(message, title, rating, release_date):
    summary = message.text

    # Создаем объект SQLite в этом потоке
    conn = sqlite3.connect('steam_games.db')
    cursor = conn.cursor()

    # Добавляем игру в базу данных
    cursor.execute('''
        INSERT INTO games (title, rating, release_date, summary)
        VALUES (?, ?, ?, ?)
    ''', (title, rating, release_date, summary))
    conn.commit()
    conn.close()

    bot.send_message(message.chat.id, 'Игра добавлена в базу данных!')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для добавления игр в базу данных.')

# Запускаем бота
bot.polling()
