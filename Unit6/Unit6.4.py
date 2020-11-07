import shelve
shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()

def increased(begin, end):
    return (100*(end/begin-1))

maxinc = 0
for year in range(1913, 2009):
    incr = increased(cpi[year][5],cpi[year][9])
        
    if incr > maxinc:
        maxinc = incr
        maxyr = year
print(maxyr, maxinc)
