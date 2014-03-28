from django.shortcuts import render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'homepage/home.html'

    def get_queryset(self):
        return None


class 

def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    return HttpResponse("<p>Invalid login</p>")