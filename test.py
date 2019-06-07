# coding: utf-8

import urllib.request

# Just to check the CA file is global I open google and display the content
contents = urllib.request.urlopen("https://www.google.com/").read()
print(contents)
