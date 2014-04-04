from django.shortcuts import render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

########################################################
######### Generic views of every section ##################
#########################################################
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

<<<<<<< HEAD
def login(request):
    username = request.POST['user']
=======
########################################################
######### End of generic views of every section ##############
#########################################################



# Check for a valid login - handle POST request
# Authentication system
def auth(request):
    username = request.POST['username']
>>>>>>> 041d75c1c8368cf70e3936722a58bc0a59c125b2
    password = request.POST['password']

    print (type(request))

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse("<p>You're logged in</p>")
    else:
        return HttpResponse("<p>Invalid login<p>")
