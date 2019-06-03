# coding: utf-8

from kivy.app import App
from kivy.uix.image import AsyncImage
import urllib.request

import certifi
print("Certifi location: %s" % certifi.where())


class HTTPsApp(App):
	def build(self):
		try:
			contents = urllib.request.urlopen("https://www.google.com/").read()
			print(contents)
		except Exception as e:
			print("Fail to retrieve https://www.google.com/ %s")
		return AsyncImage(source='https://media.makeameme.org/created/its-working-oyy433.jpg')

HTTPsApp().run()
