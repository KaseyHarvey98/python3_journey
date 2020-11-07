dictionary = {}

while True:
    word = input('Enter English Word: ')
    if word in dictionary:
        print(word, '=' ,dictionary[word])
    else:
        translation = input('Enter translation: ')
        dictionary[word] = translation
