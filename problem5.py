# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# First, list the prime factors of each number
# Then multiply each factor the greatest number of times it occurs in either number
# Then multiply each factor by the greatest # of times it occurs in either number

def getPrimeFactors(n):
    '''Accepts an integer n and returns prime factors as a list'''
    
    primeList = []
    primeDict = {}
    
    # Want to make sure loop functions with new n value, so wrap in a while loop
    should_restart = True
    while should_restart:
        should_restart = False
        # Loop through each number from 1 to n
        for i in range(2,n+1):
            prime = False
            # If that number is a factor of n, test if it is prime
            if n % i == 0:
                # To test if prime, check all numbers from 2 to i
                for j in range(2,i+1):
                    # If j goes into i evenly, j is a factor of i, and i is not prime.
                    if i != j and i % j == 0:
                        prime = False
                    else:
                        prime = True
                # If i is a prime factor of n, add to the primes list
                if prime == True:
                    n = n//i    # Divide n by the prime factor found
                    # primeList.append(i)
                    if i not in primeDict:
                        primeDict[i] = 1
                    else:
                        primeDict[i] += 1
                    should_restart = True
                    break
                
    return primeDict
    
def findLCM(maxNumber):
    '''Accepts an integer maxNumber indicating the maximum number to test for.
    Turns each number in maxNumber into prime factors + then obtains LCM from that set.'''
    
    LCMDict = {}
    
    # Loop through numbers, get prime factors. If the prime factor is not in the dict already, add it in with the count equal to count for that number. If the prime factor is in the dict already, check if it's reached its max; if not, add it in.
    for i in range(1, maxNumber+1):
        primeFactors = getPrimeFactors(i)
        for k,v in primeFactors.iteritems():
            if k not in LCMDict:
                LCMDict[k] = v
            else:
                if LCMDict[k] < v:
                    LCMDict[k] = v
    
    # Final solution
    sum = 1
    for k,v in LCMDict.iteritems():
        sum *= k**v
    
    # print LCMDict
    # print 'sum is: ',sum
    
    return sum

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print 'Expecting 2 and 5: '
    primeDict = getPrimeFactors(10)
    print primeDict
    print 'Expecting 2 and 2 and 5: '
    primeDict = getPrimeFactors(20)
    print primeDict
    print 'Expecting 3 and 3: '
    primeDict = getPrimeFactors(9)
    print primeDict
    print '========================\n'
    print 'Testing findLCM(20)'
    print 'Expecting 2:2, 3:1, 5:1'
    print findLCM(5)
    print 'Expecting 2:3, 3:1, 5:1, 7:1'
    print findLCM(8)
    print 'Expecting 3:2'
    print findLCM(9)
    print '\n\nFinal!'
    print findLCM(20)
    print '========================\n'
    print 'Testing output'
    for i in range(1,21):
        print '/t',i
        print '/t',232792560.0/i
    ##Isn't working for 9 and 18