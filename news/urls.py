from django.urls import path
from .views import  index

urlpatterns = [
  # path('scrape/', scrape, name="scrape"),
  path('', index, name="index"),
]