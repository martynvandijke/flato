from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json, requests
from django.template import loader
from django.shortcuts import redirect




def index(request):

    if request.user.is_authenticated():
                template = loader.get_template('index.html')
                context = {

                }
                return HttpResponse(template.render(context, request))

    else:
        return redirect('/login/')
