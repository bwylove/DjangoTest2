# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 自定义管理器作用：
# 1。更改默认查询结果
# 2.增加模型类方法（推荐在管理器使用）

# BookInfo.books2.values()
# <QuerySet [
# {'bcomment': 34L, 'btitle': u'\u5c04\u96d5\u82f1\u96c4\u4f20', 'bput_date': datetime.datetime(1980, 5, 1, 0, 0, tzinfo=<UTC>), 'isDetele': False, u'id': 1L, 'bread': 12L},
# {'bcomment': 24L, 'btitle': u'\u96ea\u5c71\u98de\u72d0', 'bput_date': datetime.datetime(1987, 11, 11, 0, 0, tzinfo=<UTC>), 'isDetele': False, u'id': 4L, 'bread': 58L},
# {'bcomment': 0L, 'btitle': u'\u78a7\u8840\u5251', 'bput_date': datetime.datetime(1990, 1, 1, 0, 0, tzinfo=<UTC>), 'isDetele': False, u'id': 6L, 'bread': 0L},
# {'bcomment': 0L, 'btitle': u'\u98de\u72d0\u5916\u4f20', 'bput_date': datetime.datetime(2018, 5, 4, 0, 0, tzinfo=<UTC>), 'isDetele': False, u'id': 7L, 'bread': 0L}
# ]>

class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDetele=False)

    # 自定义类创建对象
    def create(self, btitle, bput_date):
        b = BookInfo()
        b.btitle = btitle
        b.bput_date = bput_date
        b.bread = 0
        b.bcomment = 0
        b.isDetele = False
        return b

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bput_date=models.DateTimeField(db_column='put_date')
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(null=False)
    isDetele=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'
    books1=models.Manager()
    # 使用自定义管理器
    books2=BookInfoManager()
#     自定义类创建对象
    @classmethod
    def create(cls,btitle,bput_date):
        b=BookInfo()
        b.btitle=btitle
        b.bput_date=bput_date
        b.bread=0
        b.bcomment=0
        b.isDetele=False
        return b


class HeroInfo(models.Model):
    hname=models.CharField(max_length=100)
    hgender=models.BooleanField(default=False)
    hcontent=models.CharField(max_length=10000)
    isDetele=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)