import telebot
import os
from dotenv import load_dotenv

token = os.getenv('TOKEN')
id = os.getenv('ID')

def send_notify(message):
    bot = telebot.TeleBot(token)
    bot.send_message(id, message)



if __name__ == '__main__':
    load_dotenv()
