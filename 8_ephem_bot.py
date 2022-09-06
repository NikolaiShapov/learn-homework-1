"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings #Токен Бота от судю

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    print(update)
    update.message.reply_text(user_text)

def planet_in_the_constellation(update, context):
    user_command, planet, *_ = update.message.text.split()
    print(user_command, planet)
    planet_dict = {'Jupiter': ephem.Jupiter(datetime.today()),
            'Mars': ephem.Mars(datetime.today()),
            'Mercury': ephem.Mercury(datetime.today()),
            'Moon': ephem.Moon(datetime.today()),
            'Neptune': ephem.Neptune(datetime.today()),
            'Pluto': ephem.Pluto(datetime.today()),
            'Saturn': ephem.Saturn(datetime.today()),
            'Sun': ephem.Sun(datetime.today()),
            'Uranus': ephem.Uranus(datetime.today()),
            'Venus': ephem.Venus(datetime.today())}
    if planet_dict.get(planet):
        constellation = ephem.constellation(planet_dict.get(planet))
        update.message.reply_text(f'планета {planet} сегодня находится в созвездии - {constellation[-1]}')
    else: update.message.reply_text('Это не планета!')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_in_the_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
