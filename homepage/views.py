from django.shortcuts import render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'homepage/home.html'

    def get_queryset(self):
        return None


class KhoahocView(generic.ListView):
    template_name = 'homepage/Khoahoc.html'

    def get_queryset(self):
        return None

class VideoTiengAnhView(generic.ListView):
    template_name = 'homepage/videotienganh.html'

    def get_queryset(self):
        return None

class BaiHatTiengAnhView(generic.ListView):
    template_name = 'homepage/baihattienganh.html'

    def get_queryset(self):
        return None

class TaiLieuView(generic.ListView):
    template_name = 'homepage/tailieu.html'

    def get_queryset(self):
        return None

class TroChoiView(generic.ListView):
    template_name = 'homepage/trochoi.html'

    def get_queryset(self):
        return None

class TracNghiemView(generic.ListView):
    template_name = 'homepage/tracnghiem.html'

    def get_queryset(self):
        return None

def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    if user is not None:
        login(request, user)
        return HttpResponse("<p>You're logged in</p>")
    else:
        return HttpResponse("<p>Invalid login<p>")