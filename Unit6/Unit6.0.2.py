import urllib.request, shelve
url = 'http://www.meadoweast.com/csci133/hf.txt'
book = urllib.request.urlopen(url)
lines = book.readlines()
book.close()



lines = lines[21:11381]
finalLines = []
for line in lines:
    line = line.decode()[:-2]
    finalLines.append(line)
shelf = shelve.open('books')
shelf['Huckleberry Finn'] = finalLines
shelf.close()
