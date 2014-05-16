# -*- coding: utf-8 -*-
__author__ = 'Nam Xuan'


from lettuce import *
from  django.test.client import Client
from django.core.urlresolvers import reverse


@step('I go to English_Web')
def go_to_English_Web(step):
    world.client = Client()
    world.response = world.client.get('localhost:8000')

@step('I click "Dang nhap" button')
def click_dangnhap(step):
    world.response = world.client.get(reverse('accounts:login'))

@step('I log in with account is "(.*)" and pass is "(.*)"')
def log_in(step,username,password):
    # username = 'nam'
    # password = '123'
    world.client.login(username=username,password = password)
    world.response = world.client.get(reverse('accounts:detail'))

@step(r'I see "(.*)"')
def check_response(step,keyword):
    if keyword in str(world.response.content) :
        assert True
    else: assert False,\
    'Lỗi: responsse trả về không đúng theo mong đợi'

@step('I log out')
def log_out(step):
    world.client.logout()
    world.response = world.client.get('localhost:8000')

@step('I cannot see "(.*)"')
def cannot_see(step,keyword):
    if keyword not in str(world.response.content) :
        assert True
    else: assert False,\
    'Lỗi: responsse trả về không đúng theo mong đợi'


