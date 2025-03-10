

from rest_framework.generics import CreateAPIView 
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView  
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

from user.models import CustomUser 
from user.Serializer.user_serializer import (
    UserLoginSerializer,
    UserLogOutSerializer,
    UserSignUpSerializer ,
    GetUserSerializer
)


# Create Here User Sign Up API 

class UserSignUpAPI(CreateAPIView):
    serializer_class = UserSignUpSerializer
    queryset = CustomUser.objects.all()


# Create User Login API using API View, since we adding more customizing value here 

class UserLoginAPIView(APIView):

    def post(self,request):

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



# User Log Out API View 

class LogOutAPIView(APIView):

    permission_classes=[IsAuthenticated]


    def post(self,request):

        serializer = UserLogOutSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# this api used for list API View 


class UserListAPIView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = GetUserSerializer
    permission_classes = [IsAuthenticated]