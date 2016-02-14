# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import pprint

def getFirstMultiples(n, numMultiples):
    ''' Takes a number n and returns the first numMultiples multiples of n '''
    multiples = set()
    for i in range(1, numMultiples+1):
        multiples.add(n*i)
    return multiples
   
   
def getLeastCommonMultiple(numMin, numMax, numMultiples):
    ''' Gets the first numMultiples of each number in the range numMin-numMax and returns the LCM '''
    
    multiples = {}
    multiplesSet = set()
    
    for num in range(numMin, numMax+1):
        numSet = getFirstMultiples(num, numMultiples)
        multiples[num] = numSet
        multiplesSet.add(numSet)
    
    print multiplesSet
    

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print getFirstMultiples(5, 10)
    print getFirstMultiples(19, 10)
    print '========================\n'
    print getLeastCommonMultiple(1,20,10)