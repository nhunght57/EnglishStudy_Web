from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# Check for a valid login - handle POST request
# Authentication system
def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    print(type(request))

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("<p>Invalid login<p>")

# users will manage their account here
def account_detail(request):
    return render(request, 'accounts/account_detail.html')

# call this function to sign user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# user will login by using this view
def login_view(request):
    return render(request, 'accounts/login.html')