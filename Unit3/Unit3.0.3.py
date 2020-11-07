concordance = {}
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        for word in line.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1

while True:
    word = input('Enter word:')
    if word in concordance:
        print('Found on lines:', concordance[word])
    else:
        print('Not found.')
