with open('pap.txt') as book:
    for line in book:
        if 'property' in line:
            print(line)
