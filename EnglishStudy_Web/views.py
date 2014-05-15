__author__ = 'k15bh_000'
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = 'index2.html'

    def get_queryset(self):
        return None

def about(request):
    return render(request, 'about.html')