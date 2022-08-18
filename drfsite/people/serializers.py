import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *

# 1-----------------------------------------------------

# class PeopleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = People
#         fields = ('title', 'cat_id')

# 2-----------------------------------------------------

# class PeopleModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
# class PeopleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
# def encode():
#     model = PeopleModel('Angelina Joli', 'Angelina Joli is actor')
#     model_sr = PeopleSerializer(model)      # переводим нашу модель в объект сериализация, затем останется перевести в json
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     strem = io.BytesIO(b'{"title":"Angelina Joli","content":"Angelina Joli is actor"}')
#     data = JSONParser().parse(strem)
#     serializer = PeopleSerializer(data=data)    # для декодирование нужно передавать аргумент в параметр data
#     serializer.is_valid()
#     print(serializer.validated_data)            # получаем декодированные данные

# 3-----------------------------------------------------
#
# class PeopleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
# 4-----------------------------------------------------
#
# class PeopleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return People.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
#
# 5-----------------------------------------------------

class PeopleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = People
        fields = ('title', 'content', 'time_create', 'time_update', 'is_published', 'cat', 'user')

# ------------------------------------------------------
