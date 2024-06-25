"Основной файл запуска телеграм бота"

from database import Manager
from pybot import start_polling

if __name__ == "__main__":
    Manager.create_tables()
    start_polling()
