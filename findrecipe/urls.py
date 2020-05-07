from django.urls import path
from . import views

urlpatterns = [
     path('', views.schema_view),
     path('/search', views.search, name="search"),
     path('/get', views.get, name="get"),
]