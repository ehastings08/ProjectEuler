# Problem 3 - Largest prime factor

# A prime factor is a number that goes into (is divisible by) a given larger number, but is not itself divisible by anything

def findFactors(n):
    '''Accepts a target number as its input, identifies all factors, and returns them in a list'''
    
    # Use reduce to filter out non-factors, go up only to the square root to walk up factor tree to 'halfway', and use set to create an iterable
    # Used Stack Overflow to optimize this as originally used a for loop and list up to sqrt
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n%i == 0)))

def findPrimes(n):
    ''' Accepts a target number as its input, attempts to find all primes within that number, and returns the largest of the prime factors.
    Example: The prime factors of 13,195 are 5, 7, 13, and 29. '''
    
    primeFactors = []
    
    # For each factor, if the factor has any other factors, eliminate it.
    factorList = findFactors(n)
    for f in factorList:
        if findFactors(f) == set([1, f]):
            primeFactors.append(f)
    return max(primeFactors)
    
if __name__ == "__main__":
    # print findFactors(60)
    # print findFactors(1)
    # print findFactors(7)
    # print set([1,7])
    # print findPrimes(60)
    # print findPrimes(13195)
    # print findPrimes(1082)
    print findPrimes(600851475143)