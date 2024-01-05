from telebot import TeleBot, types
from random import randint
from dlb import *
from datetime import datetime, timedelta
import random
import time
import os
from time import sleep
import hashlib
from urllib.parse import urlencode
import uuid
import threading
from payment import process_payment, process_payment2, process_payment3, process_payment4, tg_pay, spotik


bot = TeleBot('6709558983:AAFTU6vRTN4sNnvvWaYRzZf5_Fuib0DXZ4c')

order_numbers = {}


@bot.message_handler(commands=['start'])

def main(message: types.Message):
    user_id = message.from_user.id
    res = bot.get_chat_member(chat_id='@saidyshop', user_id=user_id)
    
    if res.status == "member" or res.status == 'creator':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton("🧊 | О магазине")
        button3 = types.KeyboardButton("💰 | Купить товар")
        button1 = types.KeyboardButton('🆘 | Техподдержка')
        button4 = types.KeyboardButton('👻 | Контакты разработчиков')
        button5 = types.KeyboardButton('🍬 | Правила')
        #button6 = types.KeyboardButton('🎁| Бесплатный подарок')
        markup.row(button3, button, button1,)
        markup.row(button4, button5)
        #markup.row(button6)

        bot.send_message(user_id, "Спасибо за подписку! Вы можете продолжить использование бота.", reply_markup=markup)
    else:
        bot.send_message(user_id, f'Добро пожаловать, {message.from_user.first_name}\n\nПеред началом подпишись на [канал](https://t.me/saidyshop)',
        reply_markup=markup,
        parse_mode="MarkdownV2"
    )
        
        

    p = open('ds.png', 'rb')
    bot.send_photo(message.chat.id, p)

@bot.message_handler(func=lambda message: not message.text in ['/start', '🧊 | О магазине', '💰 | Купить товар', '🆘 | Техподдержка', '👻 | Контакты разработчиков', '🍬 | Правила', '🎁| Бесплатный подарок'])
def handle_unknown_command(message):
    bot.send_message(message.chat.id, "Извините, я вас не понял👾\nВоспользуйтесь списком команд или напишите /start.")





@bot.message_handler(func=lambda message: message.text == "👻 | Контакты разработчиков")
def about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, s)

@bot.message_handler(func=lambda message: message.text == "🍬 | Правила")
def about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    rules = open('rules.png', 'rb')
    bot.send_photo(message.chat.id, rules, caption=pravila)

@bot.message_handler(func=lambda message: message.text == "🧊 | О магазине")
def about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    ab = open('about.png', 'rb')
    bot.send_photo(message.chat.id, ab, caption=p)

@bot.message_handler(func=lambda message: message.text == "🆘 | Техподдержка")
def about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, w)


@bot.message_handler(content_types=["text"])
def default_test(message):
    bot.send_chat_action(message.chat.id, 'typing')
    keyboard = types.InlineKeyboardMarkup()
    callback_button1 = types.InlineKeyboardButton(text="Telegram Premium🌟", callback_data="test2")
    callback_button2 = types.InlineKeyboardButton(text="Discord Nitro👾", callback_data="test3")
    callback_button3 = types.InlineKeyboardButton(text="Spotify Premium🥎", callback_data="test4")
    keyboard.add(callback_button1)
    keyboard.add(callback_button2, callback_button3)
    bot.send_message(message.chat.id, "Можешь купить такие позиции:", reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test2":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Добавить в корзину➕', callback_data='buy1')
            keyboard.add(callback_button, callback_button1)
            tg = open('tg.png', 'rb')
            bot.send_photo(call.message.chat.id, tg)
            bot.send_message(call.message.chat.id, "➖➖➖➖➖➖➖➖➖➖➖➖\n📃Товар: Telegram Premium\n💰Цена: 275 ₽ ", reply_markup=keyboard)
            
        elif call.data == 'test4':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='🥎1 month | 249 🥎 ', callback_data='spotify1')
            keyboard.add(callback_button1)
            keyboard.add(callback_button)
            tgf = open('spotik.png', 'rb')
            bot.send_photo(call.message.chat.id, tgf)
            bot.send_message(call.message.chat.id, "➖➖➖➖➖➖➖➖➖➖➖➖\n📃Товар: Spotify Premium\n💰Цена: 249 ₽ ", reply_markup=keyboard)
            
        
        elif call.data == 'spotify1':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='boughtSpotik')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: Spotify Premium🥎 | 1 month\n💰 Цена: 249 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard)

            
            
        
        elif call.data == "test3":
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button2 = types.InlineKeyboardButton(text='❄️Basic month | 199❄️', callback_data='ds1')
            callback_button3 = types.InlineKeyboardButton(text='❄️Basic year | 1199❄️', callback_data='ds2')
            callback_button4 = types.InlineKeyboardButton(text='❄️Full month | 399❄️', callback_data='ds3')
            callback_button5 = types.InlineKeyboardButton(text='❄️Full year | 2999❄️', callback_data='ds4')
            keyboard.add(callback_button2)
            keyboard.add(callback_button3)
            keyboard.add(callback_button4)
            keyboard.add(callback_button5)
            keyboard.add(callback_button)
            ds = open('discord.png', 'rb')
            bot.send_photo(call.message.chat.id, ds)
            bot.send_message(call.message.chat.id, "➖➖➖➖➖➖➖➖➖➖➖➖\nDiscord Nitro\nЦены смотри на фото! 👆", reply_markup=keyboard)

        elif call.data == 'ds1':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='boughtDS1')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: 🍄Dicsord Nitro | Basic month\n💰 Цена: 199 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard)

        elif call.data == 'ds2':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='boughtDS2')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: 🍄Dicsord Nitro | Basic year\n💰 Цена: 1199 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard)

        elif call.data == 'ds3':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='boughtDS3')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: 🍄Dicsord Nitro | Full month\n💰 Цена: 399 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard)

        elif call.data == 'ds4':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='boughtDS4')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: 🍄Dicsord Nitro | Full year\n💰 Цена: 2999 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard)

        
            #tg
        elif call.data == 'buy1':
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
            callback_button1 = types.InlineKeyboardButton(text='Перейти к оплате🌟', callback_data='bought1')
            keyboard.add(callback_button, callback_button1)
            current_time = datetime.now() + timedelta(hours=3)
            formatted_time = current_time.strftime("%H:%M:%S")
            order_number = random.randint(1000000, 1000000000)
            order_numbers[call.message.chat.id] = order_number
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'➖➖➖➖➖➖➖➖➖➖➖➖\n📃 Товар: 🍄Telegram Premium\n💰 Цена: 275 ₽\n📦 Кол-во: 1 шт.\n💡 Заказ: {order_number}\n🕐 Время заказа: {formatted_time}\n\n\n⚠️ Внимание просим вас быть бдительными так как данный сервис как и другие наши сервиса берут комиссию за платёж ! Мы будем делать всё возможное, что-бы комиссия была меньше\n➖➖➖➖➖➖➖➖➖➖➖➖', reply_markup=keyboard)



        elif call.data == 'boughtDS1':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            process_payment(bot, call, order_number)

        elif call.data == 'boughtDS2':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            process_payment2(bot, call, order_number)
        
        elif call.data == 'boughtDS3':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            process_payment3(bot, call, order_number)
        
        elif call.data == 'boughtDS4':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            process_payment4(bot, call, order_number)
        
        elif call.data == 'bought1':
            order_number = order_numbers.get(call.message.chat.id)
            tg_pay(bot, call)
            
        elif call.data == 'boughtSpotik':
            order_number = order_numbers.get(call.message.chat.id)
            spotik(bot, call)
            
        
        
        elif call.data == 'cancel':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            
        elif call.data == 'cancel2':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            
        elif call.data == 'cancel3':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            
        elif call.data == 'cancel4':
            order_number = order_numbers.get(call.message.chat.id)  # Получение номера заказа для данного чата
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            
        elif call.data == 'cancelTG':
            order_number = order_numbers.get(call.message.chat.id)
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            
        elif call.data == 'cancelSPOTIK':
            order_number = order_numbers.get(call.message.chat.id)
            bot.send_message(call.message.chat.id, f'Заказ \#`{order_number}` был отменен', parse_mode='MarkdownV2')
            


        elif call.data == "back":
            keyboard = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="Telegram Premium🌟", callback_data="test2")
            callback_button2 = types.InlineKeyboardButton(text="Discord Nitro👾", callback_data="test3")
            callback_button3 = types.InlineKeyboardButton(text="Spotify Premium🥎", callback_data="test4")
            keyboard.add(callback_button1)
            keyboard.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Можешь купить такие позиции:", reply_markup=keyboard)


bot.polling(none_stop=True)







