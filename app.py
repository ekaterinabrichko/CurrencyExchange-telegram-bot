import telebot

from config import keys, TOKEN
from exceptions import APIException, Converter

bot = telebot.TeleBot(TOKEN)

# base - валюта, которую хотим перевести, quote - валюта, в которую хотим перевести, amount - кол-во валюты для перевода
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Привет! Это бот для конвертации валют. Введите (или нажмите) /help, чтобы ознакомиться с возможностями бота'

    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help_text(message: telebot.types.Message):
    text = 'Чтобы перевести валюту, введите данные в следующем порядке (через пробел):' \
           ' \n1. Название валюты, которую хотите перевести \n2. Название валюты, в которую хотите перевести' \
           ' \n3. Количество валюты (число) \n \
 Список валют для ввода можете посмотреть тут: /currencies'

    bot.reply_to(message, text)


@bot.message_handler(commands=['currencies'])
def currencies(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise APIException('Введено больше 3х параметров')
        elif len(values) < 3:
            raise APIException('Недостаточно данных для конверсии, введите 3 значения')

        base, quote, amount = values
        total_base = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Упс! \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось выдать результат :( Попробуйте позже.\n{e}')

    else:
        text = f'Цена {amount} {base} в {quote}: {round(total_base, 2)}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
