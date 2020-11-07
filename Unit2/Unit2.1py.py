count = 0
with open('pap.txt') as book:
    for line in book:
        for letter in line:
               if letter == 'e':
                   count +=1
print(count)
