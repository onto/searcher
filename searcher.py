#!/usr/bin/env python
# coding=utf-8

import gtk
import os
import sys
import rutracker

try:
    import eyeD3
except:
    sys.exit()

artists_list = []

def scan_folder(path):
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

