# The sum of the squares of the first ten natural numbers is 385

# The square of the sum of the first ten natural numbers is 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def getSumOfSquares(maxNumber):
    '''Accepts an integer maxNumber and returns the sum of all squares from 1 to maxNumber'''
    
    sum = 0
    for i in range(1,maxNumber+1):
        sum += i**2
    return sum
    
def getSquareOfSums(maxNumber):
    '''Accepts an integer maxNumber and returns the square of the sum of all numbers from 1 to maxNumber'''
    
    sum = 0
    for i in range(1,maxNumber+1):
        sum += i
    return sum**2

def getDifference(maxNumber):
    '''Accepts an integer maxNumber and returns the difference of the sum of squares and the square of sum'''
    return getSquareOfSums(maxNumber) - getSumOfSquares(maxNumber)
    
if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print 'Testing getSumOfSquares(10)'
    print getSumOfSquares(10)
    print 'Testing getSquareOfSums(10)'
    print getSquareOfSums(10)
    print 'Testing getDifference(10)'
    print getDifference(10)
    print 'Testing getDifference(100)'
    print getDifference(100)
    