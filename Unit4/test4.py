import cards

while True:
    initial = input('Enter inital amount: ')
    bet = int(initial)
    totalRounds = 0

    for number in range(1000):
        bankroll = bet
        rounds = 0
        while 0 < bankroll < 2*bet:
            d = cards.shuffledDeck()
            ace = False
            for number in range(6):
                card = d[number]
                if cards.faceValueOf(card) == 'ace':
                    ace = True
            if ace:
                bankroll += 1
            else:
                bankroll -= 1
            rounds += 1
        totalRounds += rounds


    print('Average number of rounds: ', totalRounds/1000)
