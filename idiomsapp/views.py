# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from idiomsapp.models import *
from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import os
# Create your views here.
def home(request):
    return render(request, 'Home.html', {})

def idiomsPost(request):
    context={}
    level =  int(request.POST['diff'])
    idioms = Idioms.objects.filter(level = level).order_by('?')
    context['idioms'] = idioms[:50]
    context['first_idiom'] = idioms[51]
    return render(request, 'IdiomsPost.html', context)

@csrf_exempt
def result(request):
    context = {}
    context ['wrongIdioms']  = request.POST['wrongIdioms']
    context ['tick'] = request.POST['tick']
    print context['tick']
    print context['wrongIdioms']
    return render(request, 'result.html', context)


# def write(request):
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     paths = dir_path+"/static/idioms_with_levels.csv"
#     idioms = pd.read_csv(paths)
#     idioms_junior = idioms[idioms["level"] == 3]["idioms"]
#     idioms_middle = idioms[idioms["level"] == 2]["idioms"]
#     for id in idioms_junior:
#         id_temp = id.replace("\r\n","").decode("utf-8-sig")
#         idiom = Idioms(idiom=id_temp,level=3)
#         idiom.save()
#     print a
#     return render(request, 'IdiomsPost.html', {})

