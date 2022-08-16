from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# 1-----------------------------------------------------
#
# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer
#
# 2-----------------------------------------------------
#
# class PeopleAPIView(APIView):
#     def get(self, request):
#         lst = People.objects.all().values()     # all() получает queryset, a values() преобразовывает в набор определенных значений
#         return Response({'posts': list(lst)})   # Response переводит словарь в json-строку
#
#     def post(self, request):
#         post_new = People.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': model_to_dict(post_new)})
#
# 3-----------------------------------------------------
#
# class PeopleAPIView(APIView):
#     def get(self, request):
#         lst = People.objects.all()                                          # all() получает queryset, a values() преобразовывает в набор определенных значений
#         return Response({'posts': PeopleSerializer(lst, many=True).data})   # Response переводит словарь в json-строку, тоже самое что и ф-я encode()
#
#     def post(self, request):
#         serializer = PeopleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = People.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         return Response({'post': PeopleSerializer(post_new).data})
#
# 4-----------------------------------------------------
#
# class PeopleAPIView(APIView):
#     def get(self, request):
#         lst = People.objects.all()                                          # all() получает queryset, a values() преобразовывает в набор определенных значений
#         return Response({'posts': PeopleSerializer(lst, many=True).data})   # Response переводит словарь в json-строку, тоже самое что и ф-я encode()
#
#     def post(self, request):
#         serializer = PeopleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'error': 'method PUT is not allowed'})
#
#         try:
#             instance = People.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Objects does not exists'})
#
#         serializer = PeopleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#
#         if not pk:
#             return Response({'error': 'method Delete is not allowed'})
#
#         try:
#             instance = People.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({'error': 'Objects does not exists'})
#
#         return Response({'post': 'delete post ' + str(pk)})
#
# 5-----------------------------------------------------

class PeopleAPIView(APIView):
    def get(self, request):
        lst = People.objects.all()                                          # all() получает queryset, a values() преобразовывает в набор определенных значений
        return Response({'posts': PeopleSerializer(lst, many=True).data})   # Response переводит словарь в json-строку, тоже самое что и ф-я encode()

    def post(self, request):
        serializer = PeopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'method PUT is not allowed'})

        try:
            instance = People.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = PeopleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'method Delete is not allowed'})

        try:
            instance = People.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Objects does not exists'})

        return Response({'post': 'delete post ' + str(pk)})


class PeopleAPIList(generics.ListCreateAPIView):                            # ListCreateAPIView для get и post запросов
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIUpdate(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):                                 # ModelViewSet заменяет 3 последних класса и удаление
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

# ------------------------------------------------------
