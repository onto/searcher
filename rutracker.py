#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import cookielib

class Rutracker():

    def __init__(self):
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(self.opener)

    def login(self, login, password):

        login_values = {"login_username" : login,
                        "login_password" : password,
                        "login" : "Вход"}

        params = urllib.urlencode(login_values)

        page = self.opener.open("http://login.rutracker.org/forum/login.php", params)


