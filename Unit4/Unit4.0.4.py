import random
def paperStatus(classSize):
    papers = list(range(classSize))
    random.shuffle(papers)
    for student in range(classSize):
        if papers[student] == student:
            return 'warning'
    return 'okay'
def experiment(classSizes, repetitions):
    for classSize in classSizes:
        print('Class size: ', classSize)
        warnings = 0
        for number in range(repetitions):
            if paperStatus(classSize) == 'warning':
                warnings += 1
        print('Warnings:', warnings, 'out of', repetitions)
        print()
    
experiment([30, 300, 3000], 1000)
