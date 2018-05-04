# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Max, F, Q
from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    # list=BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    # list=BookInfo.books1.filter(pk__lte=3)
    # list=BookInfo.books1.aggregate(Max('bput_date'))
    # list=BookInfo.books1.filter(bread__gt=F('bcomment'))
    # list=BookInfo.books1.filter(pk__lt=4,btitle__contains='天')
    # list = BookInfo.books1.filter(pk__lt=4).filter( btitle__contains='天')
    list=BookInfo.books1.filter(Q(pk__lt=4) | Q( btitle__contains='飞'))
    context={'list1':list}
    return render(request,'booktest/index.html',context)
