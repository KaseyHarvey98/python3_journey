concordance = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
with open('pap.txt') as book:
    linenum = 1
    for line in book:
        cleanline = ''
        for character in line.lower():
            if character in alphabet:
                cleanline += character
            else:
                cleanline += ' '
        for word in cleanline.split():
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
