def cleanedup(s):
    alphabet = '@abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

lines = 0
longest = 0
usernames = {}
with open('elon-musk.txt') as book:
    for line in book:
        lines +=1
        long = 0

        for word in cleanedup(line).split():
            if word in usernames:
                usernames[word] +=1
            else:
                if '@' in word:
                    usernames[word] = 1
        
        for word in line.split():
            long += 1
            if long > longest:
                longest= long
                lLine = line
                
print('Number of tweets: ', lines)
print('Tweet with max number of words: ', lLine)
print()

    
while True:
    word = input('Enter username: ')
    if word in usernames:
        print('Mentioned', usernames[word], 'times.')
    else:
        print('Not found')
    print()
