#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

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
        """
        It return {'id':'title of section', ...} like:
        {'1142': 'Folk, NewAge и Flamenco (DVD Video)',
         '1788': 'Metal (DVD Video)'}
        """

        forum_ids = {}

        page = self.opener.open("http://rutracker.org/forum/tracker.php")
        soup = BeautifulSoup(page.read(), fromEncoding="utf-8")

        for optgroup in ["&nbsp;Музыка","&nbsp;Электронная музыка","&nbsp;Рок-музыка"]:
            for group in soup.findAll('optgroup', label=optgroup):
                for option in group.findAll('option', attrs={'class' : None}):
                    forum_ids[option['value']] = option.text[3:-6]

        return forum_ids

    def search(self, text, ids):
        """
        It return result of searching in assigned forum sections like:
        {'http://rutracker.org/forum/viewtopic.php?t=3597138':
        u'(Punk/Hardcore/Ska-Punk)VA - Russian Tribute To Anti-Flag - 2011, MP3, V0',}
        """

        links = {}

        for id in ids:
            link = "http://rutracker.org/forum/tracker.php?f=%s&nm=%s" % (id, text)

            try:
                page = self.opener.open(link, timeout=60)
                soup = BeautifulSoup(page.read(), fromEncoding="utf-8")
                for result in soup.findAll('a', attrs={'class' : 'med tLink bold'}):
                    links["http://rutracker.org/forum/"+result['href'][2:]] = \
                    BeautifulSoup(str(result)).a.text
            except :
                pass
            
        return links

