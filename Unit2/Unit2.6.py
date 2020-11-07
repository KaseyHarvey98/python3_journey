vowels = 'aeiou'
maxcount = 0
answer = input('Feed me words: ')
words = answer.split()
for word in words:
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
        if count > maxcount:
            maxcount = count
            most = word
print(most)
