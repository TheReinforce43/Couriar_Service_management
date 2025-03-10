from rest_framework.viewsets import ModelViewSet 

from package.Model.package_model import PackageModel
from package.Serializer.package_serializer import (
    CreatePackageSerializer,
    GetPackageSerializer
)

from package.custom_permission import IsAdminOrSender 
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response 
from rest_framework import status



class PackageModelViewSet(ModelViewSet):

    def get_queryset(self):


        queryset = PackageModel.objects.select_related(
            'sender',
            'receiver'
        )

        user= self.request.user 


        # here set searching parameters

        is_deleted = self.request.query_params.get('is_deleted', None)

        sender_params = self.request.query_params.get('sender_id',None)
        receiver_params = self.request.query_params.get('receiver_id',None)
        status_params = self.request.query_params.get('status',None)

        
        # Set is_deleted params
        if is_deleted is not None :
            is_deleted = is_deleted.lower() in ['true',1]
            queryset = queryset.filter(is_deleted=is_deleted)

        # Set sender params 
        if sender_params:
            queryset = queryset.filter(sender__id=sender_params)

         # Set receiver params 
        if receiver_params:
            queryset = queryset.filter(receiver__id=receiver_params)

        # Set status params 
        if status_params:
            queryset = queryset.filter(status=status_params)


        queryset = queryset.order_by('-created_at')

        return queryset
    

    def get_serializer_class(self):
        
        if self.action in ['list','retrieve']:
            return GetPackageSerializer
        return CreatePackageSerializer
    

    # we give package create ,delete either admin or sender
    # otherwise we by default authenticated user 

 
    def get_permissions(self):
        if self.action in  ['create','destroy','update','partial_update']:
            return [IsAdminOrSender(),IsAuthenticated()]
        
        return [IsAuthenticated()]
    

    # we assume that , package sender is by default logged in user  

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


    def destroy(self, request, *args, **kwargs):
        # Soft delete instead of permanently deleting 

        package = self.get_object()

        package.is_deleted = True
        package.save()

        return Response({
            'message': 'Package deleted successfully'
        },
            status=status.HTTP_204_NO_CONTENT)
    

    

        
    



        


