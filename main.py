# coding: utf-8

import certifi
import os

# Here's all the magic !
os.environ['SSL_CERT_FILE'] = certifi.where()

from kivy.app import App
from kivy.uix.image import AsyncImage
import urllib.request

# Importing an "external" file to check the conf is global to the entire app
import test


class HTTPsApp(App):

    def build(self):
        contents = urllib.request.urlopen("https://www.google.com/").read()
        return AsyncImage(
            source='https://media.makeameme.org/created/its-working-oyy433.jpg'
        )

HTTPsApp().run()
