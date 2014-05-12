# -*- coding: utf-8 -*-
__author__ = 'Nam Xuan'

from lettuce import *
from django.http import response
from  django.test.client import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

@step('I go to login page to log in English_Web with my account is nam and my pass is 123')
def go_to_login_page(step):
    username = 'exp'
    password = '123'
    world.client = Client()
    world.client.login(username=username,password=password)

@step('I go to Tracnghiem page and see that there is no question in database')
def go_to_tracnghiem_page(step):
    world.response = world.client.get(reverse('tracnghiem:index'))

@step('I see "(.*)"')
def check_response(step,text):
    expect = str(text)
    assert expect == str(world.response.content) ,\
    'got %s'  %str(world.response.content)

# @step('I have number (\d+)' )
# def have_number(step,number):
#     world.number = int(number)
#
# @step('I calc the factorial')
# def calc_factorial(step):
#     world.result = factorial(world.number)
#
# @step('the result is (\d+)')
# def check_result(step,expected):
#     expected = int(expected)
#     assert expected == world.result, \
#         "Got %d" % world.result
#
#
# def factorial(number):
#
#     if (number == 0) is True:
#         return 1
#     return number * number * factorial(number-1)
