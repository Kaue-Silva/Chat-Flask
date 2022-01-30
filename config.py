from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool, default=False)
SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
