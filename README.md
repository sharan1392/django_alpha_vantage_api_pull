# django_alpha_vantage_api_pull
django project that fetches the price of BTC/USD from the alphavantage API every hour, and stores it on postgres using celery, redis, docker

# Features
python 3.9
Django v3.0.12
psycopg2 v2.9.1
django-rest-framework v0.1.0
celery v4.2.0
redis v3.5.3
django_celery_beat v1.4.0

# Running it Local : Build and run using docker compose
docker-compose build
docker-compose up
