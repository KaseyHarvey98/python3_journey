count = 0
with open('pap.txt') as book:
    for line in book:
        for word in line.split():
            if word == 'the':
                count += 1
print(count)
