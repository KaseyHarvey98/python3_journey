import shelve
shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()
for year in range(1920, 1991):
    if cpi[year][1] > cpi[year][2]:
        print(year)
