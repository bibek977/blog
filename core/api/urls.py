from django.urls import path
from .views import *


urlpatterns = [
    path('',BlogApi.as_view(),name="blog_api"),
    path('show/',ShowApi.as_view(),name="show_api"),
    path('show/<slug:tag_slug>/',ShowApi.as_view(),name="tag_slug"),
]
