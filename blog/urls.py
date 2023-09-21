from django.contrib import admin
from django.urls import path, include
from core.views import blog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog, name='blog' ),
    path('api/',include("core.api.urls")),
    path('accounts/', include('accounts.urls') ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
