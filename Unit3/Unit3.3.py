def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext


concordance = {}
with open('pap.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            if word in concordance:
                concordance[word] += 1
            else:
                concordance[word] = 1

while True:
    word = input('Enter word: ')
    if word in concordance:
        print(word, ' has been found ', concordance[word], 'times')
    else:
        print('Not found')
                
