import requests
from django.conf import settings
from .models import price

def alpha_vantage_client(**request):

    alpha_settings = settings.ALPHA_SERVICE
    payload = {"function":alpha_settings['FUNCTION'], "symbol":alpha_settings['SYMBOL'], "interval":alpha_settings['INTERVAL'], "apikey":alpha_settings['APIKEY']}

    response = requests.get(alpha_settings['URL'], params=payload)
    insert_price(response.json())

    return 200


def insert_price(price_data):

    if price_data: price.objects.filter().delete()
    price.objects.create(meta_data = price_data["Meta Data"], data_time_series = price_data["Time Series (5min)"])

    return 200
