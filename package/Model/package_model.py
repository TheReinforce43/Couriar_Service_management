from django.db import models
from user.models import CustomUser 

from support_snippet.pacakge_status import STATUS_CHOICES

class PackageModel(models.Model):
   
    sender = models.ForeignKey(CustomUser, related_name='sender_user',on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='receiver_user', on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Package from {self.sender} to {self.receiver}"
