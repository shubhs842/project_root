# celery_worker.py
from app import celery

if __name__ == '__main__':
    celery.worker_main(['celery', '-A', 'app.celery', 'worker', '--loglevel=info'])
