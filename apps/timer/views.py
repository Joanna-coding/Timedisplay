# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time  import gmtime, strftime

# Create your views here.

def time(request):

    context = {
        "time": strftime("%Y-%m-%d: %H:%M:%S", gmtime())
    }
    # context = {
    #     "time": request.POST["time"],
    # }
    # return HttpResponse(response, context)
    return render(request, 'timer/index.html', context)
