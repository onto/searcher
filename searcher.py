#!/usr/bin/env python

import gtk
import urllib
import os
import tagpy
import sys

try:
    import eyeD3
except:
    sys.exit()

artists_list = []

def scan_folder(self, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            if os.path.isfile(filename) and eyeD3.isMp3File(filename):
                tag = eyeD3.Tag()
                try:
                    tag.link(filename)
                    if tag.getArtist() not in artists_list:
                        print tag.getArtist()
                        artists_list.append(tag.getArtist())
                except :
                    pass

