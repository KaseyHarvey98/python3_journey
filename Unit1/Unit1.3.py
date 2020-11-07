word = 'substantiate'
substrings = ['ate', 'state', 'a', 'substantiate', 'it', 'tan']
for substring in substrings:
    if substring in word:
        print(substring, 'is a substring of', word)
