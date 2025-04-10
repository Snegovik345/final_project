import telebot
import random
bot = telebot.TeleBot("7913215781:AAF37tQ3q1aI5KgBhnjIFhvmbDitvRByi40")

eco_tips = [
    "Выбирай цифровые книги и билеты",
    "Покупай многоразовые батарейки",
    "Выбирай велосипед или самокат вместо машины",
    "Храни еду в стекле, а не в пластике",
    "Выключай приборы из розетки",
    "Используй LED-лампочки",
    "Чини вещи вместо замены",
    "Отдай старую технику на переработку",
    "Замени пластиковые пакеты на многоразовые сумки",
    "Сортируй мусор"
]
eco_challenge = [
    "День без пластика",
    "0 бумажных салфеток",
    "Весь день на велосипеде/самокате",
    "Неделя без фастфуда",
    "Раздельный сбор отходов всю неделю",
    "Не использовать лифт всю неделю",
    "Месяц без одноразового",
    "Не печатать документы весь месяц",
    "Сходить на субботник",
    "Создать эко-мем"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я EcoBuddy, твой Телеграмм бот, мой функционал ты можешь посмотреть по команде /helpme")



@bot.message_handler(commands=["helpme"])
def send_helpme(message):
    help_text = """
    🌿 *Что умеет EcoBuddy?* 🌿

    Вот мой функционал:

    *📌 Экосоветы*
    - Каждый день даю полезные советы по экологичному образу жизни
    - Как уменьшить свой углеродный след
    - Альтернативы одноразовым вещам

    *🏆 Эко-челленджи*
    - День без пластика
    - Неделя без мусора
    - Месяц с экосумкой
    - И многие другие!

    *😂 ЭкоМемы*
    - Просто запроси мем командой /meme
    - Смешные и мотивирующие картинки про экологию

    *🔎 Полезные команды:*
    /start - начать работу
    /helpme - это меню
    /tip - случайный экосовет
    /challenge - получить челлендж
    /meme - получить экологичный мем

    Давай вместе сделаем планету чище! ♻️
    """
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")



@bot.message_handler(commands=["tip"])
def send_random_tip(message):
    tips = random.choice(eco_tips)
    bot.reply_to(message, f"🌎 *Экосовет дня:*\n\n{tips}", parse_mode="Markdown")



@bot.message_handler(commands=["challenge"])
def send_random_challenge(message):
    challenges = random.choice(eco_challenge)
    bot.reply_to(message, f"♻️ *Твой экологический челлендж:*\n\n{challenges}", parse_mode="Markdown")


bot.polling()