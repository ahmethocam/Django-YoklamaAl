from django.db import models

# Create your models here.
class Okul(models.Model):
    okuladi = models.CharField(max_length=128)

