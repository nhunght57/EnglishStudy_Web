from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import UserProfile
import datetime

# Create your views here.

# I want to return http referer for 2 levels, so I declared this global variable here
previous_request = None


# Check for a valid login - handle POST request
# Authentication system
def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    # If user tick on "Ghi nhớ", request.POST['keepsession'] will be 'yes', else it will be 'no'
    if 'keepsession' in request.POST:
        keepsession = request.POST['keepsession']
    else:
        keepsession = 'no'

    print("User " + username + " authentication requested, keepsession=" + keepsession)

    user = authenticate(username=username, password=password)

    if user is not None:
        # Do not use like "keepsession is 'yes'" here. It will always return false
        # since 'is' is identity testing and '==' is for equality testing
        if keepsession == 'no':
            request.session.set_expiry(0)

        login(request, user)
        print("User " + username + " logged in")

        if previous_request is not None:
            return HttpResponseRedirect(previous_request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect("../../")

    else:
        print("Authentication failed")
        return HttpResponse("<p>Invalid login<p>")


# This method use for handling POST request in signup_view

def create_new_user_object(username, email, password, birthday, home):
    user = User.objects.create_user(username=username, email=email, password=password)
    user.profile = UserProfile(birthday = birthday, home = home)
    user.save()
    user.profile.save()

def create_account(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password_verify = request.POST['password_verify']
    birthday = request.POST['birthday']
    home = request.POST['home']

    try:
        user = User.objects.get_by_natural_key(username=username)
    except User.DoesNotExist:
        user = None

    # Each condition in this list must be satisfied for the signing up process
    conditions = {
        'requested_username_is_available': user is None,
        'valid_email_address': "@" in email,
        'password_and_password_verify_is_matched': password == password_verify
    }

    if all(condition is True for condition in conditions.values()):
        create_new_user_object(username, email, password, birthday, home)
        return HttpResponse("<p>User " + username + " successfully created</p>")

    elif conditions['requested_username_is_available'] is False:
        return HttpResponse("<p>Requested username is already taken</p>")

    elif conditions['valid_email_address'] is False:
        return HttpResponse("<p>Requested e-mail address is not valid</p>")

    elif conditions['password_and_password_verify_is_matched'] is False:
        return HttpResponse("<p>Passwords did not match</p>")

    else:
        return HttpResponse("<p>Unknown error. Please check your info again</p>")


# users will manage their account here
def account_detail(request):
    return render(request, 'accounts/account_detail.html')


# call this function to sign user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# user can login by using this view
def login_view(request):
    global previous_request
    previous_request = request
    return render(request, 'accounts/login.html')


# user can sign up by using this view
def signup(request):
    return render(request, 'accounts/signup.html')