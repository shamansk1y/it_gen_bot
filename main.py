from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(command=["start"])
def message_start(message):
    bot.send_message(message.chat.id, "Hello user!")

@bot.message_handler(command=["courses"])
def message_courses(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_windth=1)

    with open("courses.txt") as file:
        courses = [item.split(",") for item in file]

        for title, link in courses:
            url_button = telebot.types.InlineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(url_button)
        bot.send_message(message.chat.id, "List of courses", reply_markup=keyboard)

