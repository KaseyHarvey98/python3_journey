import os

def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz@_0123456789'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

def findMentions(filename):
    mentioned = {}
    mention = []
    top3 = []
    count = 0
    with open(filename) as book:
        for line in book:
            for word in cleanedup(line).split():
                if word in mentioned:
                    mentioned[word] += 1
                else:
                    mentioned[word] = 1
    for word in mentioned:
            if word[:1] == '@':
                mention.append([mentioned[word],word])
    mention.sort()
    for number in range(-3,0):
            top3.append(mention[number])
    return top3


for filename in os.listdir('.'):
    if filename[-7:] == '.tweets':
        mentions = []
        print(filename)
        mentions = findMentions(filename)
        for names in mentions:
            for ats in range (1,2):
                for name in range (0,1):
                    print('   ', names[ats],names[name])
