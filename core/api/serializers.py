from rest_framework import serializers
from core.models import *

class BlogModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at']