from rest_framework.viewsets import ModelViewSet 

from package.Model.package_model import PackageModel
from package.Serializer.package_serializer import (
    CreatePackageSerializer,
    GetPackageSerializer
)



class PackageModelViewSet(ModelViewSet):
    pass 

