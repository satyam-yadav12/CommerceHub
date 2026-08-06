from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import timedelta

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")

    # jwt configurations
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_SAMESITE = "Lax"
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=59)

    JWT_SESSION_COOKIE = False

    # cors configurations
    CORS_ORIGIN = os.getenv("FRONTEND_ORIGIN")
