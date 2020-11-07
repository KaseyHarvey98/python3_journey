count = 0 
with open('Unit2.2.py') as program:
    for line in program:
        if 'for' in line:
            count += 1
print(count)
