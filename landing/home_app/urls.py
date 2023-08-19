from django.urls import path
from .views import *

app_name = 'home_app'

urlpatterns = [
    path('', index, name='index'),
    path('policy/', policy_view, name='policy')
]
