fruits = ['apple', 'banana', 'peach', 'plum', 'grapefruit']
mincount = 1000000
for fruit in fruits:
    count = len(fruit)
    if count < mincount:
        mincount = count
        shortest = fruit
print(shortest)
