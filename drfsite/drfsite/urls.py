"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from people.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')                            # Если в PeopleViewSet не прописывать queryset то нужно указать basename
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),                         # аутентификация по session_id
    path('api/v1/auth/', include('djoser.urls')),                                       # аутентификация по token
    re_path(r'^auth/', include('djoser.urls.authtoken')),                               # аутентификация по token http://127.0.0.1:8000/auth/token/login/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),          # аутентификация по JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),         # аутентификация по JWT
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),            # аутентификация по JWT

    path('api/v1/people_list/', PeopleAPIView.as_view()),
    path('api/v1/people_list/<int:pk>/', PeopleAPIView.as_view()),

    path('api/v2/people_list/', PeopleAPIList.as_view()),
    path('api/v2/people_update/<int:pk>/', PeopleAPIUpdate.as_view()),
    path('api/v2/people_delete/<int:pk>/', PeopleAPIDestroy.as_view()),
    path('api/v2/people_detail/<int:pk>/', PeopleAPIDetail.as_view()),
    path('api/v2/', include(router.urls)),                                              # http://127.0.0.1:8000/api/v2/people/
]
