import random

faceValues = ['ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'jack',
              'queen', 'king']

suits = ['clubs', 'diamonds', 'hearts',
         'spades']


deck = []

def shuffledDeck():
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]

def faceValueOf(card):
    return card.split()[0]

d = shuffledDeck()

for number in range(5):
    print(d[number])    

