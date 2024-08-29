from telebot import TeleBot, types
import hashlib
from urllib.parse import urlencode
import uuid
from AaioAPI import Aaio
import AaioAPI, time
 
def process_payment(bot, call, order_number):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 199 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '' # Секретный ключ №1 из настроек магазина
        desc = 'Discord Nitro' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IVvHgjxBBY8d')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancel")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)
        
def process_payment2(bot, call, order_number):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 1199 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '676986ec4af15551af7a79fc6cc6a4a2' # Секретный ключ №1 из настроек магазина
        desc = 'Discord Nitro' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IVUB4qLhJ06Z')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancel2")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)
        
        
        
def process_payment3(bot, call, order_number):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 399 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '676986ec4af15551af7a79fc6cc6a4a2' # Секретный ключ №1 из настроек магазина
        desc = 'Discord Nitro' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IV1PmkaOfTIS')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancel3")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)



def process_payment4(bot, call, order_number):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 2999 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '676986ec4af15551af7a79fc6cc6a4a2' # Секретный ключ №1 из настроек магазина
        desc = 'Discord Nitro' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IVWN4obXPYSE')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancel4")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)
        
        
def tg_pay(bot, call):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 275 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '676986ec4af15551af7a79fc6cc6a4a2' # Секретный ключ №1 из настроек магазина
        desc = 'Telegram Premium' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IVGOBhaa9m9r')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancelTG")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)
            
def spotik(bot, call):
    if call.message:
        payment = Aaio()
        order_id = 'python_order_' + str(uuid.uuid4())
        merchant_id = '70718908-23ad-435f-8ffa-71f4077b7145' # ID Вашего магазина
        amount = 249 # Сумма к оплате
        currency = 'RUB' # Валюта заказа
        secret = '676986ec4af15551af7a79fc6cc6a4a2' # Секретный ключ №1 из настроек магазина
        desc = 'Spotify' # Описание заказа
        lang = 'ru' # Язык формы

        url_aaio = AaioAPI.pay(merchant_id, amount, currency, secret, desc)
        print(url_aaio)

        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Назад🔙", callback_data="back")
        callback_button1 = types.InlineKeyboardButton(text='Все системы🔴', callback_data='ds', url=(url_aaio))
        callback_button2 = types.InlineKeyboardButton(text='CRYPTO PAY(USDT,BTC)💸', callback_data='ds', url='t.me/CryptoBot?start=IVq7EYyxKVRK')
        callback_button3 = types.InlineKeyboardButton(text="Отменить заказ🫠", callback_data="cancelSPOTIK")
        keyboard.add(callback_button1, callback_button2)
        keyboard.add(callback_button3)
        keyboard.add(callback_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы можете оплатить товар по ссылке ниже👇", reply_markup=keyboard)
        
        while True:
            AaioAPI.check_payment(url_aaio, payment)
            
            if payment.is_success():              # Если оплата прошла успешно
                bot.send_message(call.message.chat.id, "Оплата прошла успешно😊", reply_markup=keyboard)
            

        
        
    
     
