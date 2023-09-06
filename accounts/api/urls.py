from django.urls import path
from .views import *

urlpatterns = [
    path('user_create/',UserCreateApi.as_view(),name="user_create"),
    path('user_login/',LoginApi.as_view(),name="user_login"),
]
