import telebot
import random
bot = telebot.TeleBot("7913215781:AAF37tQ3q1aI5KgBhnjIFhvmbDitvRByi40")

quiz_questions = [
    "1. Сколько лет разлагается пластиковая бутылка? (20/100/450/1000)",
    "2. Какой материал наиболее экологичен? (Стекло/Пластик/Алюминий)",
    "3. Что экономит больше воды? (Душ/Выкл.воду при чистке зубов/Посудомойка)",
    "4. Какой % пластика перерабатывается в мире? (9%/25%/50%)",
    "5. Что разлагается быстрее? (Стекло/Бан.кожура/Пакет)"
]

correct_answers = ["450", "Стекло", "Посудомойка", "9", "Бан.кожура"]

# Словарь с инструкциями по утилизации (добавьте в начало кода)
recycle_guide = {
    "батарейка": "🔋 Сдавайте в специальные пункты приёма (часто есть в магазинах электроники). Никогда не выбрасывайте в общий мусор – одна батарейка загрязняет 20 м² земли!",
    "лампочка": "💡 Содержит ртуть! Утилизируйте только в специальных эко-боксах или пунктах приёма опасных отходов.",
    "пластик": "🧴 Помойте, снимите этикетку, смните. Сдавайте в контейнеры для пластика (маркировка 1-PET или 2-HDPE).",
    "алюминиевая банка": "🥫 Сполосните, смните. Можно сдать в металлолом или контейнер для металла. Переработка экономит 95% энергии!",
    "картон": "📦 Разберите, удалите скотч и плёнку. Сухой картон – в макулатуру. Жирную пиццебокс – нет (жир мешает переработке).",
    "стекло": "🍾 Не разбивайте! Снимите крышку (металл и стекло перерабатываются отдельно). Цветное и прозрачное стекло тоже разделяйте.",
    "одежда": "👕 Целую – в благотворительность. Изношенную – в специальные контейнеры для текстиля (переработают на ветошь или утеплитель).",
    "электроника": "📱 Сдавайте в специализированные пункты (например, «СберЭлектроника»). Даже сломанные приборы содержат ценные металлы.",
    "пакет": "🛍 Обычные пакеты почти не перерабатываются. Используйте многоразовые сумки! Биоразлагаемые пакеты требуют особых условий.",
    "чеки": "🧾 Не сдавайте в макулатуру! Бумага с термопокрытием содержит BPA. Выбрасывайте в общий мусор (увы, пока не перерабатываются)."
}
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
    /quiz - проверь свои знания по теме экологии, ответив на 5 вопросов!
    /recycle - узнай как сортировать всем известные вещи!
    Давай вместе сделаем планету чище! ♻️
    """
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")
@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    bot.send_message(message.chat.id, "🌍 Эко-викторина (5 вопросов):")
    msg = bot.send_message(message.chat.id, quiz_questions[0])
    bot.register_next_step_handler(msg, process_answer1)


def process_answer1(message):
    check_answer(message, 0, quiz_questions[1], process_answer2)

def process_answer2(message):
    check_answer(message, 1, quiz_questions[2], process_answer3)

def process_answer3(message):
    check_answer(message, 2, quiz_questions[3], process_answer4)

def process_answer4(message):
    check_answer(message, 3, quiz_questions[4], process_answer5)

def process_answer5(message):
    if message.text.lower() == correct_answers[4].lower():
        bot.send_message(message.chat.id, "✅ Верно!\n\nВикторина завершена!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно! Правильно: {correct_answers[4]}\n\nВикторина завершена!")


def check_answer(message, answer_index, next_question, next_handler):
    if message.text.lower() == correct_answers[answer_index].lower():
        bot.send_message(message.chat.id, "✅ Верно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно! Правильно: {correct_answers[answer_index]}")
    
    msg = bot.send_message(message.chat.id, next_question)
    bot.register_next_step_handler(msg, next_handler)



@bot.message_handler(commands=["tip"])
def send_random_tip(message):
    tips = random.choice(eco_tips)
    bot.reply_to(message, f"🌎 *Экосовет дня:*\n\n{tips}", parse_mode="Markdown")



@bot.message_handler(commands=["challenge"])
def send_random_challenge(message):
    challenges = random.choice(eco_challenge)
    bot.reply_to(message, f"♻️ *Твой экологический челлендж:*\n\n{challenges}", parse_mode="Markdown")


@bot.message_handler(commands=['meme'])
def send_meme(message):
    # Генерируем случайное число от 1 до 8
    meme_number = random.randint(1, 8)
    meme_filename = f'экомемас для проекта_{meme_number}.jpg'  
    try:
        with open(meme_filename, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except FileNotFoundError:
        bot.reply_to(message, "Извините, мем не найден. Попробуйте ещё раз.")



@bot.message_handler(commands=['recycle'])
@bot.message_handler(func=lambda msg: msg.text.lower().startswith('/recycle'))
def handle_recycle(message):
    try:
        # Разбиваем текст на части
        parts = message.text.split(maxsplit=1)
        
        # Если нет предмета - показываем список
        if len(parts) < 2:
            items_list = "\n".join([f"• {item}" for item in recycle_guide.keys()])
            bot.send_message(message.chat.id, 
                          "♻️ Введите предмет после команды:\n/recycle <предмет>\n\n"
                          f"Доступные предметы:\n{items_list}")
            return
            
        item = parts[1].lower().strip()
        
        # Ищем предмет в словаре
        if item in recycle_guide:
            response = f"♻️ {item.capitalize()}:\n\n{recycle_guide[item]}"
        else:
            response = f"❌ Предмет '{item}' не найден. Доступные варианты:\n"
            response += "\n".join([f"• {key}" for key in recycle_guide.keys()])
            
        bot.send_message(message.chat.id, response)
        
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(message.chat.id, "⚠️ Произошла ошибка. Попробуйте снова.")




    

bot.polling()
