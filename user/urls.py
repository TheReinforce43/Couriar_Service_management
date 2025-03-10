from django.urls import path 

from user.View.user_view import (
    UserSignUpAPI,
    UserLoginAPIView,
    LogOutAPIView,
    UserListAPIView
    

)


urlpatterns = [
    path('signup/',UserSignUpAPI.as_view(),name = 'signup'),
    path('login/', UserLoginAPIView.as_view(), name = 'login'),
    path('logout/', LogOutAPIView.as_view(), name = 'logout'),  
    path('list/', UserListAPIView.as_view(), name = 'list'),
]
