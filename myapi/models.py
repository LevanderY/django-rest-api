from django.db import models
from django.core.validators import MinLengthValidator

class Users(models.Model):
    firstName = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    lastName = models.CharField(max_length=255, validators=[MinLengthValidator(2)]) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName