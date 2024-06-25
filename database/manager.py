"Модуль класса Manager"

from typing import Sequence, Any
from sqlalchemy import Engine, Row, exc, text
from .connection import engine, TABLES


class TablesManager:
    "Класс для управления таблицами бд"
    engine: Engine = engine

    @classmethod
    def create_tables(cls) -> None:
        "метод создания таблиц"

        with cls.engine.connect() as connection:
            for table, request in TABLES.items():

                try:
                    connection.execute(text(request))
                    connection.commit()
                except exc.OperationalError:
                    request_ = request.split()
                    request_.insert(2, "IF NOT EXISTS")
                    request = " ".join(request_)
                    print(
                        f"""Таблица {table} уже существует! Исправьте запрос на \n{request}\n""")


class Manager(TablesManager):
    "Класс для упарвления таблицами и записями"

    @classmethod
    def select_many(cls, request: str) -> Sequence[Row[Any]]:
        "Метод возвращает множество записей"

        with cls.engine.connect() as connection:
            response = connection.execute(text(request))

        return response.all()

    @classmethod
    def select_one(cls, request: str) -> Sequence[Row[Any]] | None:
        "Метод возвращает одну запись"

        with cls.engine.connect() as connection:
            response = connection.execute(text(request))

        try:
            return response.one()
        except exc.NoResultFound:
            return None

    @classmethod
    def insert(cls, request: str) -> None:
        "Метод для ввода данных в бд"

        with cls.engine.connect() as connection:
            connection.execute(text(request))
            connection.commit()

    @classmethod
    def update(cls, request: str) -> None:
        "Метод для обновления записей в бд"

        with cls.engine.connect() as connection:
            connection.execute(text(request))
            connection.commit()

    @classmethod
    def delete(cls, request: str) -> None:
        "Метод для удаления записей в бд"

        with cls.engine.connect() as connection:
            connection.execute(text(request))
            connection.commit()
