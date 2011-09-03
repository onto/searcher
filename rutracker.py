#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import time
import re

class Rutracker():

    def __init__(self):

        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(self.opener)

    def login(self, login, password):

        params = urllib.urlencode({"login_username" : login,
                                   "login_password" : password,
                                   "login" : "Вход"})

        try:
            self.opener.open("http://login.rutracker.org/forum/login.php", params)
        except :
            pass

    def get_forum_ids(self):

        forum_ids = []

        page = self.opener.open("http://rutracker.org/forum/tracker.php")
        soup = BeautifulSoup(page.read())

        for optgroup in ["&nbsp;Музыка","&nbsp;Электронная музыка","&nbsp;Рок-музыка"]:
            for group in soup.findAll('optgroup',label=optgroup):
                for option in group.findAll('option', attrs={'class' : None}):
                    forum_ids.append(option['value'])

        return forum_ids

    def search(self, text, ids):
        links = {}

        for id in ids:
            link = "http://rutracker.org/forum/tracker.php?f=%s&nm=%s" % (id, text)

            try:
                page = self.opener.open(link)
                soup = BeautifulSoup(page.read())
                for result in soup.findAll('a', attrs={'class' : 'med tLink bold'}):
                    links[(str(result['href']))[result['href'].find('=')+1:]] = BeautifulSoup(str(result)).a.text

                time.sleep(1)
            except :
                pass
            
        return links

