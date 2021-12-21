from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50,default="")
    Number = models.IntegerField(max_length=100,default="")
    email = models.EmailField(max_length=100)
    password = models.IntegerField(max_length=100,default="")

    def __str__(self):
        return self.name