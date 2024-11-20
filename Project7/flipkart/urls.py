from django.urls import path
from flipkart.views import *
urlpatterns = [
    path('order/',order,name='order')
]