from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name