from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from instagrapi import Client

cl = Client()
cl.login("rakamakafo_bt", "Itit1225!!")
app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start","Hello"])
def start(message):
    msg = bot.send_message(message.chat.id, 'привет, введи любой текст и отправь')
    bot.register_next_step_handler(msg, start_2)


def start_2(message):
    bot.send_message(message.chat.id, f'на предыдущем шаге вы ввели\n{message}')

@bot.message_handler(func=lambda x: x.text.lower().startswith('python'))
def message_text(message):
    bot.send_message(message.chat.id, 'Python')

@app.route("/" + TOKEN, methods=["POST"])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200

@app.route("/")
def main():
    bot.remove_webhook()
    bot.set_webhook(url="https://it-gen-bot.herokuapp.com/" + TOKEN)
    return "Python Telegram Bot", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
