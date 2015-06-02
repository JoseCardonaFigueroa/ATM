from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cuenta(models.Model):
    user = models.OneToOneField(User)
    cantidad_total = models.FloatField()
