from django.db import models

# Create your models here.

#书籍表
class Book(models.Model):
    title=models.CharField(max_length=16)
    price=models.FloatField()
    pub_data=models.DateField()
    publish=models.CharField(max_length=16)