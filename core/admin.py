from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','created_at']

admin.site.register(Blog,BlogAdmin)