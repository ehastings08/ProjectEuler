# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def getPrimes(numPrimes):
    '''Accepts a maximum number of primes to find and returns a list of numPrimes prime numbers starting with 2.'''
    
    primesList = []
    testNum = 2
    
    while len(primesList) < numPrimes:
        prime = True
        for i in range(2,testNum+1):
            if testNum != i and testNum % i == 0:
                prime = False
        if prime == True:
            primesList.append(testNum)
        testNum += 1
        
    return primesList

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print getPrimes(2)
    print getPrimes(3)
    print getPrimes(4)
    print getPrimes(5)
    print getPrimes(6)
    print getPrimes(10001)
    
    