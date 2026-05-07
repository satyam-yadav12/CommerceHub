from dotenv import load_dotenv
import os
from pathlib import Path

basedir = Path(__file__).resolve().parent

load_dotenv(basedir / ".env")


class Config:
    print(f"DATABASE URI: {os.getenv('SQLALCHEMY_DATABASE_URI')}")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_DATABASE_URI")
        or "mysql+pymysql://root:Hello%40123@localhost/test"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
