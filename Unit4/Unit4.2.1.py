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
def wordlist(filename):
    words = []
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word not in words:
                    words.append(word)
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

words = wordlist('pap.txt')

while True:
    word = random.choice(words)
    mixed = scramble(word)
    print('Letters: ', mixed)
    guess = input ('Guess: ')
    if guess == word:
        print('Right')
    else:
        print('Sorry ', word)
