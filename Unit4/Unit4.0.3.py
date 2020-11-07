import random

def oneGame(initial):
    countFlips = 0
    bankroll = initial
    while 0 < bankroll < 2*initial:
        flip = random.choice(['heads', 'tails'])
        countFlips += 1
        if flip == 'heads':
            bankroll += 1
        else:
            bankroll -= 1
    return countFlips

def experiment(initials, repetitions):
    for initial in initials:
        print('Initial bankroll:', initial)
        totalFlips = 0
        for number in range(repetitions):
            totalFlips += oneGame(initial)
        print('Average number of flips:', totalFlips/repetitions)
        print()
        
experiment([10, 20, 40], 2000)
