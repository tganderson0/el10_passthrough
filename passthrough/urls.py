from . import views

from django.urls import path

urlpatterns = [
  path('get-prices/', views.get_prices)
]
