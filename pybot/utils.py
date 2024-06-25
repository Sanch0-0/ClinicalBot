"утилиты для работы с бд и прочее"


from typing import Sequence, Any
from sqlalchemy import Row
from database import Manager


def make_request(table_name: str, *args: str, **kwargs) -> str:
    "функция формирует запрос из переданных данных"
    if args:
        args_string = ", ".join(args)
        request = f"SELECT {args_string} FROM {table_name}"
    else:
        request = f"SELECT * FROM {table_name}"

    if kwargs:
        kwargs_list = [f'{key}="{value}"' for key, value in kwargs.items()]
        kwargs_string = ", ".join(kwargs_list)
        request += f" WHERE {kwargs_string}"

    return request


def get_doctors_list(*args: str, **kwargs) -> list[Sequence[Row[Any]]]:
    "функция возвращает список врачей"

    doctors = Manager.select_many(
        request=make_request("doctor", *args, **kwargs)
        )

    return list(doctors)


def get_doctor(*args: str, **kwargs) -> Sequence[Row[Any]] | None:
    "функция принимает id врача и возвращает запись"

    doctor = Manager.select_one(
        request=make_request("doctor", *args, **kwargs)
    )

    return doctor
