import shelve

with open('pap.txt') as book:
    lines = book.readlines()

shelf = shelve.open('books')
shelf['Pride and Prejudice'] = lines
shelf.close()

shelf = shelve.open('books')
newlines = shelf['Pride and Prejudice']
print(newlines[100])
shelf.close()
