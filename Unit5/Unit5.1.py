def printFred(n):
    print('Fred')
    if n-1 > 0:
        printFred(n-1)
        
printFred(100)
