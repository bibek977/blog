from django.urls import path,include
from .views import *

urlpatterns = [
    path('',accounts,name='accounts'),
    path('api/',include('accounts.api.urls'))
]
