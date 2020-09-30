from rest_framework import serializers
from news.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['title','category']

