from django.urls import path
from .views import *


urlpatterns = [
    path('',BlogApi.as_view(),name="blog_api"),
    path('show/',ShowApi.as_view(),name="show_api")
]
