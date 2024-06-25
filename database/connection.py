"модуль подключения к базе данных"

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE =os.getenv("DATABASE")
USER =os.getenv("DB_USER")
PASSWORD =os.getenv("DB_PASSWORD")
HOST =os.getenv("DB_HOST")
NAME =os.getenv("DB_NAME")

engine = create_engine(
    f"{DATABASE}://{USER}:{PASSWORD}@{HOST}/{NAME}", echo=True)


TABLES = {
    "doctor": """
    CREATE TABLE IF NOT EXISTS doctor (
    id INTEGER PRIMARY KEY auto_increment,
    full_name VARCHAR(250) NOT NULL,
    prof VARCHAR(50) NOT NULL,
    image TEXT,
    about TEXT
    )
    """
}
