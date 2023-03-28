from django.urls import path
from .views import Crawler

urlpatterns = [
    path('Crawler/', Crawler.as_view(), name='Crawler'),
]
