# The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

inputNum = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

testInputNum = '66370484403199890008895243450658'

def findAllAdjacent(inputNum, numAdjacent):
    '''Accepts an integer numAdjacent as the number of adjacent integers to pull from inputNum. Returns a list of all permutations of numAdjacent adjacent numbers.'''
    
    min = 0
    max = numAdjacent
    adjList = []
    
    while min < len(inputNum)-numAdjacent+1:
        adjList.append(inputNum[min:max])
        min += 1
        max += 1
        
    return adjList
    
def getProduct(string):
    ''' Accepts a number-formatted string and splits each integer, multiplies all integers to get the product '''
    
    product = 1
    
    for char in string:
        intNum = int(char)
        product *= intNum
        
    return product
    
def findAllAdjacentProducts(adjList):
    ''' Accepts a list of number-formatted strings, gets the products, and finds the max product of that list. Returns the max's product '''
    
    maxProduct = 0
    
    for numStr in adjList:
        product = getProduct(numStr)
        if product > maxProduct:
            maxProduct = product
            
    return maxProduct

if __name__ == "__main__":
    print '\n\n\n========================\nStarting unit tests'
    print 'Testing findAllAdjacent'
    # adjList = findAllAdjacent(testInputNum,4)
    # print adjList
    adjList = findAllAdjacent(inputNum,13)
    # print adjList
    # print 'Testing getProduct: expecting 756'
    # print getProduct('6637')
    # print '============================'
    print 'Testing findAllAdjacentProducts'
    print findAllAdjacentProducts(adjList)