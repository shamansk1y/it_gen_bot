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


@bot.message_handler(commands=['go'])
def gen_keyboard(message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton("Matchday", url="https://www.flashscore.ua/soccer/world/world-cup/#/2/8/zkyDYRLU/live"), InlineKeyboardButton("Group", url="https://www.flashscore.ua/soccer/world/world-cup/standings/#/2/8/zkyDYRLU/table"), InlineKeyboardButton("Bombardier", url="https://www.flashscore.ua/soccer/world/world-cup/standings/#/2/8/zkyDYRLU/top_scorers"), InlineKeyboardButton("Results", url="https://www.flashscore.ua/soccer/world/world-cup/results/"), InlineKeyboardButton("Matches", url="https://www.flashscore.ua/soccer/world/world-cup/fixtures/"))
    bot.send_message(message.chat.id, 'World Cup 2022', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello, user!\n all command:\n "/go"\n "/user_info"\n')



def all_groups():
    pass


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
