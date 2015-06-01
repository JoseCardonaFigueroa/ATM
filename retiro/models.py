from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Retiros(models.Model):
    user = models.OneToOneField(User)
    monto_retiro = models.FloatField()
    fecha_retiro = models.DateTimeField(auto_now_add=True)

class Cuenta(models.Model):
    user = models.OneToOneField(User)
    cantidad_total = models.FloatField()
