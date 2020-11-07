def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

def lengths(sentence):
    text = []
    for words in sentence:
        text.append(len(words))
    return text

while True:
    line = input('Enter a sentence: ')
    words = cleanedup(line).split()
    print('Average word length:', average(lengths(words)))
