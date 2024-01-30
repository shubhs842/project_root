# app/__init__.py
from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
import spacy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Load spaCy model
nlp = spacy.load(app.config['SPACY_MODEL'])

from app import views, models
