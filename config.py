# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://your_username:your_password@localhost/your_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
    CELERY_RESULT_BACKEND = 'rpc://'
    SPACY_MODEL = 'en_core_web_sm'
