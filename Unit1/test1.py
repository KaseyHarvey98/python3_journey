word = 'coronavirus'
unique = 'abcdefghijklmnopqrstuv'
medications = ['remdesivir', 'hydroxychloroquine', 'kaletra', 'favipiravir']

for letter in unique:
    if letter in word:
        print(word, 'contains', letter)

for letter in unique:
    if letter in word:  
        for medication in medications:
            if letter in medication:
                print(letter, 'is in', word, 'and also in', medication)
        

