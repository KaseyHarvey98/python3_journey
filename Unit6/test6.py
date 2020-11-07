import urllib.request, shelve
# I had to put 'www' to make it work on my computer. The original code did not have this.
# If it gives errors this way, please try running with just 'http://nancymcohen.com/csci133/cpiai.txt'
#Thank you
url = 'http://www.nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()
cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]
shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()

def average(nums):
    total = 0
    for n in nums:
        total += n
    return total/len(nums)

def averageInterval(num, year):
    total = 0
    for n in num:
        total += cpi[year][int(n)]
    return total/len(num)

#Previously used to find interval
def printlist(year, interval):
    cpiForMonths = []
    for num in interval:
        cpiForMonths.append(cpi[year][int(num)])
    return cpiForMonths
    
while True:
    dates = input('Enter query: ')
    date = dates.split()
    if len(date) == 1:
        print([cpi[int(date[0])][num] for num in range(1,13)], average(cpi[int(date[0])][1:13]))

    else:
        print([cpi[int(date[0])][int(num)] for num in date[1:]], averageInterval((date[1:]),int(date[0])))
        #print(printlist(int(date[0]),date[1:]), averageInterval((date[1:]),int(date[0])))
