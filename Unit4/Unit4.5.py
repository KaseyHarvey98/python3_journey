import cards

d = cards.shuffledDeck()

numberOfAces = 0
numberOfClubs = 0
for number in range(5):
    card = d[number]
    print(card)
    if cards.faceValueOf(card) == 'ace':
        numberOfAces += 1
    if cards.suitOf(card) == 'clubs':
        numberOfClubs += 1

print(numberOfAces)
print(numberOfClubs)
