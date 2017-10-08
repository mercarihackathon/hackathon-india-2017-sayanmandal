# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'juice/juiceLoc.html')
