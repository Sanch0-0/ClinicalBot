"Модуль с основными функциями бота"

from telebot import types  # type: ignore
from database import Manager
from .bot import bot
from .utils import get_doctors_list


@bot.message_handler(commands=["start"])
def hello_user(message: types.Message) -> None:
    "Функция принимает команду /start и приветствует пользователя"

    username = message.from_user.username  # находим username пользователя

    if username is not None:
        bot.send_message(  # отправляем сообщение пользователю
            chat_id=message.chat.id,
            text=f"Привет, {username}!"
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Привет!"
        )


@bot.message_handler(commands=["doctors"])
def doctors_list(message: types.Message) -> None:
    "Функция создаёт клавиатуру докторов и отправляет её пользователю"

    markup = types.InlineKeyboardMarkup(row_width=3)  # клавиатура

    # проходимся циклом по всем докторам
    for doctor in get_doctors_list("id", "full_name"):
        button = types.InlineKeyboardButton(
            text=doctor[1], callback_data=f"doctor_id:{doctor[0]}")  # кнопка "doctor_id:5"
        markup.add(button)  # добавление кнопки в клавиатуру

    bot.reply_to(
        message=message,
        text="Here is a list of doctors",
        reply_markup=markup
    )


@bot.callback_query_handler(
    func=lambda call: call.data.startswith("doctor_id:")
)
def doctor_answer(call: types.CallbackQuery) -> None:
    "Функция отвечает на callback query клавиатуры с врачами"

    doctor_id = call.data.replace("doctor_id:", "")
    doctor = Manager.select_one(request=f"SELECT * FROM doctor WHERE id={doctor_id}")

    if doctor is not None:
        text = f"""
            id: {doctor[0]}
            full_name: {doctor[1]}
            prof: {doctor[2]}
            image: {doctor[3]}
            about: {doctor[4]}
        """
    else:
        text = "Врач не найдет"

    bot.send_message(
        chat_id=call.message.chat.id,
        text=text
    )


@bot.message_handler(content_types=["text"])
def how_are_you(message: types.Message) -> None:
    "Функция принимает текстовое сообщение пользователя и отвечает на него"

    message_text = message.text  # сообщение, которое было отправлено боту

    if message_text.lower() == "how are you?":
        bot.reply_to(  # Ответ на сообщение
            message=message,
            text="I'm good!"
        )


__all__ = [
    "hello_user",
    "doctors_list",
    "doctor_answer",
    "how_are_you",
]
