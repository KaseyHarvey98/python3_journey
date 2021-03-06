def goalSeek(function, limit1, limit2, target, maxError=.01):
    result1 = function(limit1)
    result2 = function(limit2)

    if result1 < target < result2:
        return goalSeeker(function, limit1, limit2, target, maxError)
    if result2 < target < result1:
        return goalSeeker(function, limit2, limit1, target, maxError)
    return None
    
def goalSeeker(function, lowLimit, highLimit, target, maxError=.01):
    error = maxError + 1
    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
    return guess

def mystery(x):
    return x*x-10*x+25

print(goalSeek(mystery, 0, 5, 10, .001))
