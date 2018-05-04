# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bput_date=models.DateTimeField(db_column='put_date')
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(null=False)
    isDetele=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname=models.CharField(max_length=100)
    hgender=models.BooleanField(default=False)
    hcontent=models.CharField(max_length=10000)
    isDetele=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)