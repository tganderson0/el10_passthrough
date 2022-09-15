from . import views

from django.urls import path

urlpatterns = [
  path('get-price/', views.get_price),
  path('get-prices/', views.get_prices),
  path('set-uc-sessions/', views.set_uc_session),
]
