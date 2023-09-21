from django.urls import path
from .views import *


urlpatterns = [
    path('',BlogApi.as_view(),name="blog_api"),
    path('<int:id>',BlogApi.as_view(),name="blog_api_id"),
    path('show/',ShowApi.as_view(),name="show_api"),
    path('show/<int:id>',ShowApi.as_view(),name="show_api_id"),
    path('show/<slug:tag_slug>/',ShowApi.as_view(),name="tag_slug"),
]
