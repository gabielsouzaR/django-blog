from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
   return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
    return HttpResponse("olá Django")
