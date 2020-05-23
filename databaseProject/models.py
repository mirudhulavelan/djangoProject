from django.db import models

class update(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    pin = models.CharField(max_length=6, default='xxxxxx')
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    skill = models.CharField(max_length=50, default='python')
    exp = models.CharField(max_length=20, default='Nil')
    edu = models.CharField(max_length=30, default='B.E')

class Meta:
    db_table = 'update'

