from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import *
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


class PeopleViewSet(viewsets.ModelViewSet):                                 # ModelViewSet заменяет 4 следующих класса
    # queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return People.objects.all()[:3]
        else:
            return People.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)                                  # detail=True для получения одного объекта, False для списка
    def all_category(self, request):                                        # http://127.0.0.1:8000/api/v2/people/all_category/
        cats = Category.objects.all()
        return Response({'category': [c.name for c in cats]})

    @action(methods=['get'], detail=True)                                   # http://127.0.0.1:8000/api/v2/people/1/category/
    def category(self, request, pk=None):
        cat = Category.objects.get(pk=pk)
        return Response({'category': cat.name})

# ---------------------------------------
class PeopleAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class PeopleAPIList(generics.ListCreateAPIView):                            # ListCreateAPIView для get и post запросов
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )                      # Для создания поста нужно быть авторизованным
    pagination_class = PeopleAPIListPagination


class PeopleAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsOwnerOrReadOnly, )                              # IsOwnerOrReadOnly - custom permission


class PeopleAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAdminOrReadOnly, )                              # IsAdminOrReadOnly - custom permission


class PeopleAPIDetail(generics.RetrieveUpdateDestroyAPIView):               # RetrieveUpdateDestroyAPIView выделяет, обновляет, удаляет объект
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )
# ---------------------------------------

# ------------------------------------------------------
