vowels = 'aeiou'
fruits = ['apple', 'banana', 'peach', 'grapefruit']
for fruit in fruits:
    print('Vowels in', fruit)
    for letter in vowels:
        if letter in fruit:
          print(letter)
