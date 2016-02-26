##  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##  Find the sum of all the primes below two million.


import math

# Define a primeFilter() function to apply via filter
def primeFilter(num):
    prime = True
    for i in range(2, int(math.ceil(math.sqrt(num)))+1):
        # print '\ti is ',i
        # print '\tmax of range is ', int(math.ceil(math.sqrt(num)))+1
        if num != i and num % i == 0:
            # print '\t\tnum != i and num % i is 0; num % i is ',num%i
            prime = False
    return prime

    
# Sieve - create list of consecutive integers, select p as first prime (p=2), remove multiples of p from the list; set p equal to next integer in list which has not been removed; repeat until p**2 > N; all remaining numbers are prime

def primeSieve(maxNum):
    ''' Create a list of consecutive integers up to maxNum and then filter all non-primes.
    Returns a list of primes '''
    
    # Create a list of consecutive integers
    numList = [i for i in range(1,maxNum+1)]
    
    # Select p as the first prime 2
    p = 2
    
    while p**2 < maxNum:
        # Remove multiples of p from list
        numList = filter(primeFilter, numList)
        
        # Increment p
        p = numList[numList.index(p)+1] ## Next integer in list that has not been removed
        
    return numList  # return numList if you want to test
    
    

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print '===================================='
    print 'Testing primeFilter(10)'
    print 'Expect true: ',primeFilter(2)
    print 'Expect true: ',primeFilter(3)
    print 'Expect false: ',primeFilter(4)
    print 'Expect true: ',primeFilter(5)    # This is returning FALSE?
    print 'Expect false: ',primeFilter(6)
    print 'Expect true: ',primeFilter(7)
    print 'Expect false: ',primeFilter(8)
    print 'Expect false: ',primeFilter(9)
    print 'Expect false: ',primeFilter(10)
    print '===================================='
    print 'Testing primeSieve()'
    print primeSieve(2)
    print primeSieve(3)
    print primeSieve(10)
    print primeSieve(20)
    