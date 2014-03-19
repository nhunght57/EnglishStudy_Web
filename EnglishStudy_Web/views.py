__author__ = 'k15bh_000'
from django.http import HttpResponse

def index(request):
    return HttpResponse("index view")