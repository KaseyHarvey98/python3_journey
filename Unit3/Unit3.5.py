def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total/len(numbers)

while True:
    numbers = input('Enter numbers: ')
    userNumbers = []
    for word in numbers.split():
        userNumbers.append(int(word))
    print(average(userNumbers))
