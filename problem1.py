# Problem 1 - 3s and 5s

def find3and5(maxNum, toPrint=True):
    total = 0
    for i in range(1,maxNum):
        if toPrint == True:
            print 'Testing i ',i
            print 'Remainder 3: ',i % 3 
            print 'Remainder 5: ',i % 5
        if i%3 == 0 or i%5 == 0:
            total += i
    return total
    
if __name__ == "__main__":
    total = find3and5(1000,toPrint=False)
    print total