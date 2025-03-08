from rest_framework import serializers 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 

from user.models import CustomUser 



# This Serializer Used for user sign up 

# Here I am using model serializer and overriding the default create method 

class UserSignUpSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser 
        fields  = ['id','email','first_name','last_name','phone_number','password']

    

    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        return user
    



# Here Create Custom Login Serializer 


class UserLoginSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)



    def validate(self,data):

        email = data.get('email', None)
        password = data.get('password', None)


        user = authenticate(email=email, password=password)

        # Here check either any credentials valid or not 
        if not user :
            raise serializers.ValidationError("Invalid credentials")
        

        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        
        # Generate JWT token for user

        refresh = RefreshToken.for_user(user)


        return {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'access_token': str(refresh.access_token),
           'refresh_token': str(refresh)
        }


# Here Create User Logout Serializer 


class UserLogOutSerializer(serializers.Serializer):

    RefreshToken = serializers.CharField()

    
    def validate(self, data):
        self.RefreshToken = data.get('RefreshToken')
        return data
    


    # during logout , existing token are stored in blacklist so that it can't be used again
    def save(self,**kwargs):
        try:
            token = RefreshToken(self.RefreshToken)
            token.blacklist()
            return {'message': 'User Logout Successfully'}
        
        except Exception as e:
            return serializers.ValidationError('Invalid RefreshToken or expiration')
        


# User Serializer for get portion 


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','email','first_name','last_name','phone_number']