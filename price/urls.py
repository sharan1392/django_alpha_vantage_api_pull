from django.urls import path

from . import views

urlpatterns = [
    path('vi/quotes', views.GetPrices.as_view())
]
