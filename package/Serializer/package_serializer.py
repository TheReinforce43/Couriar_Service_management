from rest_framework import serializers 


# Import related serializer and model 
from package.Model.package_model import PackageModel
from user.Serializer.user_serializer import GetUserSerializer 



class CreatePackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PackageModel
        # fields = ('id', 'name', 'description', 'price', 'quantity', 'sender','receiver')
        fields = '__all__'



class GetPackageSerializer(serializers.ModelSerializer):

    sender = GetUserSerializer()
    receiver = GetUserSerializer()


    class Meta:
        model = PackageModel
        # fields = ('id', 'name', 'description', 'price', 'quantity', 'sender', 'receiver')
        fields = '__all__'