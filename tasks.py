# app/tasks.py
from celery import Celery
from app import celery, db, nlp
from app.models import NewsArticle

@celery.task
def process_news_article(article_id):
    article = NewsArticle.query.get(article_id)
    if article:
        # Perform NLP classification using spaCy
        doc = nlp(article.content)
        # Placeholder logic for categorization
        # You should replace this with a more sophisticated classification mechanism
        if any(token.text.lower() in ['terrorism', 'protest', 'political', 'unrest', 'riot'] for token in doc):
            article.category = 'Terrorism/Protest/Political Unrest/Riot'
        elif any(token.text.lower() in ['positive', 'uplifting'] for token in doc):
            article.category = 'Positive/Uplifting'
        elif any(token.text.lower() in ['natural', 'disaster'] for token in doc):
            article.category = 'Natural Disasters'
        else:
            article.category = 'Others'
        db.session.commit()
