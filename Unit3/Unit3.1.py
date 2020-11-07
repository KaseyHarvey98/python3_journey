def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext

longest = 0
with open('pap.txt') as book:
    for line in book:
        for word in cleanedup(line).split():
            long = len(word)
            if long > longest:
                longest= word.len()
                lword = word
print(lword)
