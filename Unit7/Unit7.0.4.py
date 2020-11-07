def pctIncrease(begin, end):
    return 100*(end/begin-1)

def increaseByPct(begin, pct):
    return begin+begin*pct/100

def totalPct(pct):
    startValue = 175.1
    value = startValue
    for year in range(5):
        value = increaseByPct(value, pct)
    return pctIncrease(startValue, value)

def goalSeek(lowLimit, highLimit, target):
    for attempt in range(20):
        guess = (lowLimit+highLimit)/2
        result = totalPct(guess)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess

print(goalSeek(-100, 100, 13.2))
