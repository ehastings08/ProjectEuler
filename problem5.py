# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import pprint

def getFactors(n):
    '''Obtains all  factors of a number n
    Input: an integer n
    Output: a list of factors of n '''
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors
    
def getNonOneFactors(n):
    '''Obtains the non-1, non-n factors of a number n
    Input: an integer n
    Output: a list of factors of n where factors != 1 or n'''
    factors = []
    for i in range(1,n+1):
        if i != 1 and i != n:
            if n % i == 0:
                factors.append(i)
    return factors
    
def filterFactorList(factorList):
    ''' Parses a list of factors and throws out factors that are multiples of previous factors '''
    
    # For each value in the factor list, get its subsidiary factors. If they are both in the factor list already, toss the number.
    
    print 'factorList is: ',factorList
    

def getSmallestMultiple(minNum,maxNum):
    ''' '''
    # Get the range of numbers from minNum to maxNum
    numRange = range(minNum, maxNum+1)
    print 'numRange: ',numRange
    
    # Get multiples
    # To get the smallest multiple, as long as you have two composite multiples of a bigger number you don't need to multiply by that number
    # So the numbers 1 to 20 only need multiples 2 and 10 to make sure it is divisible by twenty
    
    # Get unique factors
    factorsDict = {}
    factorsList = []
    for i in numRange:
        factors = getNonOneFactors(i)
        factorsDict[i] = factors
        for f in factors:
            if f not in factorsList:
                factorsList.append(f)
        
    pprint.pprint(factorsDict)
    print factorsList

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    # print getNonOneFactors(10)
    # print getFactors(10)
    print 'Would expect filterFactorList to reduce the below to [1,2,3,4,5,7,9]'
    print filterFactorList([1,2,3,4,5,6,7,8,9,10])
    # getSmallestMultiple(1,20)