#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

class Rutracker():

    def __init__(self):
        self.forum_ids = []

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(self.opener)

    def login(self, login, password):

        login_values = {"login_username" : login,
                        "login_password" : password,
                        "login" : "Вход"}

        params = urllib.urlencode(login_values)

        try:
            self.opener.open("http://login.rutracker.org/forum/login.php", params)
        except :
            pass

    def get_forum_ids(self):

        self.forum_ids = []

        page = self.opener.open("http://rutracker.org/forum/tracker.php")
        soup = BeautifulSoup(page.read())

        for optgroup in ["&nbsp;Музыка","&nbsp;Электронная музыка","&nbsp;Рок-музыка"]:
            for group in soup.findAll('optgroup',label=optgroup):
                for option in group.findAll('option', attrs={'class' : None}):
                    self.forum_ids.append(option['value'])

    def search(self, text):
        pass
