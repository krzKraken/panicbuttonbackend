from django.db import models


# Create your models here.
class Equipment(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    client = models.CharField(max_length=30)
    center = models.CharField(max_length=50)
    ubication = models.CharField(max_length=50)
    reported = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
