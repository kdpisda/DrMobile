# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    pincode = models.IntegerField()
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class CompanyDetails(models.Model):
    company = models.CharField(max_length=50)   
    model = models.CharField(max_length=100)
    # quantity = models.IntegerField(blank=True) 

    def __str__(self):
        return self.company