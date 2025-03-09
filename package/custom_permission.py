from rest_framework.permissions import BasePermission 

"""

Custom permissions can soft delete or update the value 
by either admin or personal package sender 

"""
 

class IsAdminOrSender(BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user 


