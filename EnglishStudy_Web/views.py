__author__ = 'k15bh_000'
from django.http import HttpResponse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return None