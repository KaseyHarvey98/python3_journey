import shelve
shelf = shelve.open('books')
book = shelf['Huckleberry Finn']
shelf.close()
for line in book:
    if 'cat' in line:
        print(line)
