# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here
def year_archive(request,year):
   # return HttpResponse('Hello,World '+year)
    a_list = Article.objects.filter(pub_date__year=year)
    return render_to_response('news/year_archive.html', {'year': year, 'article_list': a_list})

def index(request):
    return HttpResponse('Hello,World')