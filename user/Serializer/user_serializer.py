from rest_framework import serializers 

from user.models import CustomUser 



# This Serializer Used for user sign up 

# Here I am using model serializer and overriding the default create method 

class UserSignUpSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser 
        fields  = '__all__'