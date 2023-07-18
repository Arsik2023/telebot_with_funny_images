import telebot
from telebot import types
import Class_Fox_API
import Class_Doq_API
import Class_Cat_API
import Class_random_cat_text
import Class_cat_animation

token = '5922342212:AAH21sOH9MwqzcSFv8Qg_RON52A9J4WnWKQ'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])

def start_message(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,"Привет, солнышко☀️")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_cats = types.KeyboardButton("Котики")
        button_foxs = types.KeyboardButton("Фото лисичек")
        button_dogs = types.KeyboardButton("Фото собачек")
        button_me = types.KeyboardButton("О разработчике")
        markup.add(button_cats, button_foxs, button_dogs, button_me)
        bot.send_message(message.chat.id, text="Выбери, что тебе надо", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def firsts_buttons_functions(message):
    if message.text == "О разработчике":
        bot.send_message(message.chat.id,"Фамилия и имя: Сосян Арсен")
        bot.send_message(message.chat.id, "Имя пользователя в Telegram: @pythonarsik")
        bot.send_message(message.chat.id,"Электронная почта: arsiktimic@gmail.com")
        bot.send_message(message.chat.id,"Ссылка на GitHub: https://github.com/Arsik2023", disable_web_page_preview = True)
        bot.send_message(message.chat.id, "Используемые мной API")
        bot.send_message(message.chat.id, "API для котиков: https://cataas.com/cat?json=true", disable_web_page_preview = True)
        bot.send_message(message.chat.id, "API для котиков с текстом: https://cataas.com//cat/PEQrlesC9ZhBnlgo/says/hello?json=true", disable_web_page_preview = True)
        bot.send_message(message.chat.id, "API для котиков с гифкой: https://cataas.com/cat/gif?json=true", disable_web_page_preview = True)
        bot.send_message(message.chat.id, "API для лисичек: https://randomfox.ca/floof", disable_web_page_preview = True)
        bot.send_message(message.chat.id, "API для собачек: https://dog.ceo/dog-api/documentation/random", disable_web_page_preview = True)
    elif message.text == "Котики":
        bot.send_message(message.chat.id, "А зачем тебе котик, если ты и являешься котиком?)❤️")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_cat = types.KeyboardButton("Фото котика")
        button_cat_text = types.KeyboardButton("Фото котика с текстом")
        button_cat_animation = types.KeyboardButton("Гифка с котиком")
        button_menu = types.KeyboardButton("Назад в меню")
        markup.add(button_cat, button_cat_text, button_cat_animation, button_menu)
        bot.send_message(message.chat.id,"Выберите, что вам нужно", reply_markup=markup)
    elif message.text == "Фото котика":
        bot.send_message(message.chat.id, "😺Лови котика😺")
        url_cat = Class_Cat_API.Random_cat_photo
        url_cat = url_cat.Random_cat_url()
        bot.send_photo(message.chat.id, url_cat)
    elif message.text == "Фото котика с текстом":
        bot.send_message(message.chat.id, "С каким текстом будет фотка котика?")
        bot.register_next_step_handler(message, func_message_expect)
    elif message.text == "Гифка с котиком":
        bot.send_message(message.chat.id, "😺Лови котика😺")
        url_cat_animation = Class_cat_animation.Random_cat_animation
        url_cat_animation = url_cat_animation.Random_cat_animation_url()
        bot.send_animation(message.chat.id, url_cat_animation)
    elif message.text == "Фото лисичек":
        bot.send_message(message.chat.id,"🦊Лови лисичку🦊")
        url_fox = Class_Fox_API.Random_fox_photo
        url_fox = url_fox.Random_fox_url()
        bot.send_photo(message.chat.id, url_fox)
    elif message.text == "Фото собачек":
        bot.send_message(message.chat.id,"🐶Лови собачку🐶")
        url_dog = Class_Doq_API.Random_dog_photo
        url_dog = url_dog.Random_dog_url()
        bot.send_photo(message.chat.id, url_dog)
    elif message.text == "Назад в меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_cats = types.KeyboardButton("Котики")
        button_foxs = types.KeyboardButton("Фото лисичек")
        button_dogs = types.KeyboardButton("Фото собачек")
        button_me = types.KeyboardButton("О разработчике")
        markup.add(button_cats, button_foxs, button_dogs, button_me)
        bot.send_message(message.chat.id, "Вы вернулись назад")
        bot.send_message(message.chat.id, "Выберите, что вам нужно", reply_markup = markup)
def func_message_expect(message):
    bot.send_message(message.chat.id, "😺Лови котика😺")
    url_cat_text = Class_random_cat_text.Random_cat_photo_text(message.text)
    url_cat_text = url_cat_text.Random_cat_photo_text_url()
    bot.send_photo(message.chat.id, url_cat_text)
bot.infinity_polling()