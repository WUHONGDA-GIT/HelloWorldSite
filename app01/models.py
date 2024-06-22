from django.db import models

# Create your models here.
"""
对数据库的操作
"""

class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
