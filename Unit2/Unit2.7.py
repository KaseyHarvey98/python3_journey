maxcount = 0
with open('pap.txt') as book:
    for line in book:
        count = len(line.split())
        if count>maxcount:
            maxline = line
            maxcount = count
print(maxline)
