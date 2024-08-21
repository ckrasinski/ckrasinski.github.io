from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=700)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, related_name="region")


class Message(models.Model):
    from_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_who")
    to_who = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_who")
    content = models.CharField(max_length=2000)
    timestamp = models.DateTimeField(auto_now_add=True)
