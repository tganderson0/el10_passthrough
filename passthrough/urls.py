from . import views

from django.urls import path

urlpatterns = [
  path('get-price/', views.get_price),
  path('get-prices/', views.get_prices),
]
