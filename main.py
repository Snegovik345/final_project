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
