import urllib.request

url = "https://www.googleapis.com/gmail/v1/users/"
user_id = "pratiekkroy@hmail.com"
url = url + user_id + "/profile"
contents = urllib.request.urlopen(url).read()

print(contents)


