from django.db import models

# Create your models here.

class Contact_List(models.Model):
       Fullname=models.CharField(max_length=20)
       PhoneNumber=models.BigIntegerField()
       emailAddress=models.EmailField()
       Date=models.DateField(auto_now_add=True)
