from rest_framework import serializers
from core.models import *
# from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from taggit.serializers import TaggitSerializer,TagListSerializerField

class BlogModelSerializer(TaggitSerializer, serializers.ModelSerializer ):
    tags = TagListSerializerField()
    class Meta:
        model = Blog
        exclude = ['created_at', 'updated_at']
        # fields = ['title', 'tags']