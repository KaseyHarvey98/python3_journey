def f(x):
    return 17.7/(4*x**2-12*x+13)

def vals(begin, end, num):
    step = (end-begin)/(num-1)
    return[begin+n*step for n in range(num)]

begin = float(input ('Enter Beginning number: '))
end = float(input ('Enter Ending number: '))
print(max([f(x) for x in vals(begin,end,100)]))

