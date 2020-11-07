import urllib.request

url = '​ ​https://meadoweast.com/csci133/hf.txt'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()
print(lines[124])
