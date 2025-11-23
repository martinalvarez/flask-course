import os
from flask import Flask
from dotenv import load_dotenv

def load_config(app: Flask):
    load_dotenv()

    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = os.getenv("SECRET_KEY", "default123"),
        ENV = os.getenv("ENV", "production")
    )
