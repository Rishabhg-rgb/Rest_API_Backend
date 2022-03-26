from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name