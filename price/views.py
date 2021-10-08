from django.views import View
from .models import price
from django.http import HttpResponse, JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from price.client import alpha_vantage_client

@method_decorator(csrf_exempt, name='dispatch')
class GetPrices(View):
    """
        This method is to get prices
        :param : request
        :return : price list
    """

    def get(self, request):
        price_data = price.objects.filter().values()
        if price_data: response = {"Meta Data" : price_data[0]["meta_data"], "Time Series" : price_data[0]["data_time_series"]}
        else: response = {"Status" : "No data found"}
        return JsonResponse(response)

    def post(self, request):
        alpha_vantage_client()
        return HttpResponse("Triggered alphavantage price request, Please try GET method to see the prices")
