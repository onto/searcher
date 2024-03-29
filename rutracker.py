#!/usr/bin/env python
# coding=utf-8

# Copyright (C) 2011 Anton Lashkov <lenton_91@mail.ru>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

