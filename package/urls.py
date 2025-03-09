from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 

from package.View.package_api import PackageModelViewSet


routers = DefaultRouter()


routers.register(r'packages', PackageModelViewSet,basename='packages')


urlpatterns = [
    path('',include(routers.urls)),
]
