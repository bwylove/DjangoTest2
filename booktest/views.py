# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    # list=BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    list=BookInfo.books1.filter(pk__lte=3)
    context={'list':list}
    return render(request,'booktest/index.html',context)
