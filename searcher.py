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

class Searcher():

    def __init__(self):
        artists_list = []

    def scan_folder(self, path):
        for songs in os.listdir(path):
            