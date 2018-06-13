from django.db import models


# Create your models here.

class Resume_class(models.Model):
    name= models.CharField(max_length=30)
    email=models.EmailField(max_length=70, null=True)
    phone = models.IntegerField(default=200)
    whywehire_message = models.CharField(max_length=1000, blank=True)
    pdf_file = models.CharField(max_length=1000000)
