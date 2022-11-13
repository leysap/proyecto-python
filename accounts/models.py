from django.db import models
from django.contrib.auth.models import User

class ExtensionUsuario(models.Model):
    avatar= models.ImageField(upload_to='avatares',null=True, blank=True)
    web= models.CharField(max_length=50, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'