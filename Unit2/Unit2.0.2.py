count = 0
with open('pap.txt') as book:
    for line in book:
        count += len(line.split())
print(count)
