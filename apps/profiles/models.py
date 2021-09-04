from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    position = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)

class Skills(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.PROTECT)
    python_xp = models.IntegerField()
    javascript_xp = models.IntegerField()
    sql_xp = models.IntegerField()
    java_xp = models.IntegerField()
    spark_xp = models.IntegerField()
    html_xp = models.IntegerField()
    others_xp = models.IntegerField()
