from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Your_CSV(models.Model):
    your_csv = models.FileField()
    description = models.CharField(max_length = 150)
    date = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
