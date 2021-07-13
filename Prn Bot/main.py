import telebot
from bs4 import BeautifulSoup
import config
import random
import requests
from urllib.request import Request, urlopen

bot = telebot.TeleBot(config.token)
r = 'http://porno365.love/movie/'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, просто напиши /porn :)")
    elif message.text == '/porn':
        bot.send_message(message.from_user.id, ''.join(prnGenerator()))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Просто напиши /porn :)")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def prnGenerator():
    for i in range(1000):
        try:
            a = random.randint(1, 27500)
            req = Request(r+str(a), headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            page_soup = BeautifulSoup(webpage, "html.parser")
            title = page_soup.find("Ошибка 404 :(")
            if title == None:
                return r+str(a)
                break
        except:
            pass

bot.polling(none_stop=True, interval=0)