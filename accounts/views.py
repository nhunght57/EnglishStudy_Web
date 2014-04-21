from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# Create your views here.

# I want to return http referer for 2 levels, so I declared this global variable here
previous_request = None

# Check for a valid login - handle POST request
# Authentication system
def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    # If user tick on "Ghi nhớ", request.POST['keepsession'] will be 'yes'
    if 'keepsession' in request.POST:
        keepsession = request.POST['keepsession']
    else:
        keepsession = 'no'

    print("User " + username + " authentication requested, keepsession=" + keepsession)

    user = authenticate(username=username, password=password)

    if user is not None:
        # Only keep session in maximum of 7 days
        # Do not use like "keepsession is 'yes'" here. It will always return false
        # since 'is' is identity testing and '==' is for equality testing
        if keepsession == 'yes':
            print("Expire in 7 days")
            request.session.set_expiry(604800)

        login(request, user)
        print("User " + username + " logged in")

        if previous_request is not None:
            return HttpResponseRedirect(previous_request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect("../../")

    else:
        print("Authentication failed")
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
    global previous_request
    previous_request = request
    return render(request, 'accounts/login.html')