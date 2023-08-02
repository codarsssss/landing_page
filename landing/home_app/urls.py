from django.urls import path
from .views import *

app_name = 'home_app'

urlpatterns = [
    path('', index, name='index_t'),
    path('news_<slug:slug>/', news_detail, name='news')
]
