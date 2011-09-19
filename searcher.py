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


import gtk
import os
import sys
import rutracker

try:
    import eyeD3
except:
    sys.exit()

def scan_folder(path):

    artists_list = []

    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            if os.path.isfile(filename) and eyeD3.isMp3File(filename):
                tag = eyeD3.Tag()
                try:
                    tag.link(filename)
                    if tag.getArtist() not in artists_list:
                        artists_list.append(tag.getArtist())
                except :
                    pass

    return artists_list
