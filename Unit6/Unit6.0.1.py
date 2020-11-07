import urllib.request
url = 'http://www.meadoweast.com/csci133/hf.txt'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()

index = 0
for line in lines:
    line = line.decode()[:-2]
    if '***' in line:
        print(index, line)
    index += 1
