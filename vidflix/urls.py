
from django.contrib import admin
from django.urls import path


# collection of valid router for rental app
urlpatterns = [
    path('', views.index, name="root"),
    path('test', views.test, name="test"),
    path('home/something', views.index, name="long"),
    path('details', views.details, name="long")
]
