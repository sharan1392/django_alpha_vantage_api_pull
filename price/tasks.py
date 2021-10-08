from price.celery import app
from .client import alpha_vantage_client

@app.task
def periodic_task_fetch_price():
    """
        calls to get the prices
        :param request
    """
    alpha_vantage_client()
    print("Triggered alphavantage price request, Please try GET method to see the prices")
