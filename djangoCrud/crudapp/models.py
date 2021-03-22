from django.db import models

# Create your models here.

class contact(models.Model):
    firstName = models.CharField("First name", max_length=50, blank= True, null="True")
    lastName = models.CharField("Last name", max_length=50, blank=True, null="True")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank="True", null="True")
    address = models.TextField(blank="True", null="True")
    description= models.TextField(blank="True", null="True")
    createAt = models.DateTimeField("Created at", auto_now_add=False)

def __str__(self):
    return self.firtsName