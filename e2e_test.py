import urllib.request

HOST = 'http://simple-mta.appspot.com'

# [START e2e]
response = urllib.request.urlopen("/")
html = response.read()
assert(html == "Tranquily Base")
# [END e2e]
