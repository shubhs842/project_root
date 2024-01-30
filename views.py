# app/views.py
from flask import render_template
from app import app, db
from app.models import NewsArticle
from app.tasks import process_news_article
import feedparser

@app.route('/')
def index():
    articles = NewsArticle.query.all()
    return render_template('index.html', articles=articles)

@app.route('/update_articles')
def update_articles():
    for feed_url in [
        'http://rss.cnn.com/rss/cnn_topstories.rss',
        'http://qz.com/feed',
        'http://feeds.foxnews.com/foxnews/politics',
        'http://feeds.reuters.com/reuters/businessNews',
        'http://feeds.feedburner.com/NewshourWorld',
        'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
    ]:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            # Check for duplicates
            existing_article = NewsArticle.query.filter_by(title=entry.title).first()
            if not existing_article:
                new_article = NewsArticle(
                    title=entry.title,
                    content=entry.summary,
                    category='Uncategorized'  # Default category
                )
                db.session.add(new_article)
                db.session.commit()
                # Enqueue task for NLP classification
                process_news_article.apply_async(args=[new_article.id])

    return 'Articles updated successfully.'
