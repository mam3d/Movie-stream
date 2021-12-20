from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery()
app.config_from_object("config.settings:base")
app.autodiscover_tasks()


if __name__ == "__main__":
    app.start()