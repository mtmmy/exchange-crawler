import urllib.request
page = urllib.request.urlopen('https://stackoverflow.com/questions/1843422/get-webpage-contents-with-python')
print(page.read())
