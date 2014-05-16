# -*- coding: utf-8 -*-

Feature:  Test authentication
          In order to log in English_web
          As a tiny person want to learn English
          I will log in English-web

          Scenario: Login with valid credentials
            Given I go to English_Web
            And I click "Dang nhap" button
            When I log in with account is "nam" and pass is "123"
            Then I see "Hi, nam"

          Scenario: Login with invalid username
            Given I go to English_Web
            And I click "Dang nhap" button
            When I log in with account is "example" and pass is "123"
            Then I see "you haven't log in"

          Scenario: Login with invalid password
            Given I go to English_Web
            And I click "Dang nhap" button
            When I log in with account is "nam" and pass is "passsai"
            Then I see "you haven't log in"

          Scenario: Logout from login
            Given I go to English_Web
            And I click "Dang nhap" button
            When I log in with account is "example" and pass is "123"
            Then I log out
            And I cannot see "Hi, nam"




