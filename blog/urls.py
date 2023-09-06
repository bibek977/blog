from django.contrib import admin
from django.urls import path, include
from core.views import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog, name='blog' ),
    path('accounts/', include('accounts.urls') ),
]