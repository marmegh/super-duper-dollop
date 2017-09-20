# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import Survey
from django.shortcuts import render, redirect

form = Survey()
def index(request):
    return render(request, "survey/index.html", { "form":form })
