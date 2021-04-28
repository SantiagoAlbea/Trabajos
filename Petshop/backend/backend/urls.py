"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls import url, include

from django.conf.urls.static import static

from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import AllowAny

# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
#from rest_framework_simplejwt.views import (
 #   TokenObtainPairView,
  #  TokenRefreshView,
   # TokenVerifyView
#)
# from apps.auth.api import TokenObtainPairView

from rest_framework import permissions
#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),

#    path('api/', InfoApi.as_view(), name='info_api'),
    path('api/personas/', include('apps.personas.urls', namespace='personas')),
    path('api/ventas/', include('apps.ventas.urls', namespace='ventas')),
    path('api/turnos/', include('apps.turnos.urls', namespace='turnos')),
    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth"),

#    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 #   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  #  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
