from django.db import models
# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100,null=True)
    email= models.EmailField(max_length=100,null=True)
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id)