from flask import Flask
import telegram

token = '1145825632:AAEnIwxQgZ4ni7KwY0maUcP5xL9CHIoaI0U'
user = '717402002'


# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     # app.run()
bot = telegram.Bot(token=token)
bot.sendMessage(chat_id=user, text="안녕?")
