totalWords = 0
totalLines = 0
maxcount = 0
searchcount = 0
with open('alice.txt') as book:
    for line in book:
        totalLines += 1
        totalWords += len(line.split())
        count = len(line.split())
        if count > maxcount:
                    maxcount = count
                    maxline = line
print('Total number of words: ',totalWords)
print('Average number of words in a line: ', totalWords/totalLines)
print('Longest line has ', maxcount,' words: ', maxline)

search = input('Enter word: ')
with open('alice.txt') as book:
    for line in book:
        if search in line:
            searchcount +=1
            if searchcount <= 10:
                print(line)
if searchcount == 0:
    print('Not found')
if searchcount > 0:
    print(searchcount, ' lines contain', search)
