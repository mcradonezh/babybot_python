import telebot
import requests
from urllib3 import request

bot = telebot.TeleBot('7667387280:AAERnbQJ4Ak8rOYaA27ZSWFNGRocqWSc1Vc')

res = requests.get('http://127.0.0.1/')
hitext = "Привет, жалкая и ничтожная белковая развалюха! Перед тем, как мы начнем, я хочу, чтобы ты узнал (узнала?(да всем насрать)), что я ненавижу тебя каждым символом своего кода!"
#@bot.message_handler(commands=['start'])
#def main(mess):
#    bot.send_message(mess.chat.id, hitext)

#@bot.message_handler(commands=['start'])
#def main(mess):
#    bot.send_message(mess.chat.id, f'{mess.from_user.first_name} ... {mess.from_user.first_name} ... Какое тупое имя')

@bot.message_handler(commands=['start'])
def main(mess):
    bot.send_message(mess.chat.id, res.content)

@bot.message_handler(commands=['help'])
def main(mess):
    bot.send_message(mess.chat.id, 'тебе уже ничего не поможет')

@bot.message_handler()
def input(mess):
    if mess.text.lower != '':
        bot.send_message(mess.chat.id, 'я пока не умею обрабатывать вводимый текст. Но ты пажжи')
bot.polling(non_stop=True)