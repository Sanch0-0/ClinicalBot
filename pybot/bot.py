"Модуль с ботом"

from telebot import TeleBot  # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

bot = TeleBot(token=os.getenv("TOKEN", "DEFAULT TOKEN"))

def start_polling() -> None:
    "функция запускает бота"

    bot.infinity_polling()
