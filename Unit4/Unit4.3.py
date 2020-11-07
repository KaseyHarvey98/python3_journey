import random

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def wordlists(filename):
    words = {}
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                length = len(word)
                if length in words:
                    words[length].append(word)
                else:
                    words[length] = [word]
    return words

def rejoin(characters):
    word =''
    for character in characters:
        word += character
    return word

def scramble(word):
    mixed = list(word)
    random.shuffle(mixed)
    return rejoin(mixed)

words = wordlists('pap.txt')

level = 3

while True:
    word = random.choice(words[level])
    mixed = scramble(word)
    print('Letters: ', mixed)
    guess = input ('Guess: ')
    if guess == word:
        print('Right')
        level += 1
    else:
        print('Sorry ', word)
        level -= 1
