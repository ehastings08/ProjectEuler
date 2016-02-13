# Problem 4 - Largest palindrome product

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def createPerms(numDigits):
    ''' Accepts an integer of the number of digits to create permutations for.
    Then creates all permutations of the valid integers with numDigits digits.
    Input: an integer numDigits to specify the number of digits each item in the output should have
    Output: a list of valid numbers with numDigits digits. '''
    
    if numDigits == 1:
        return list([i for i in range(0,10)])
    else:
        return list([i for i in range(10**(numDigits-1),10**(numDigits))])

        
def isPalindrome(n):
    ''' Takes a number n and determines whether the number is a palindrome (the same back to front and front to back, using recursion '''
    
    nstr = str(n)
    if len(nstr) == 0:
        return True
    if len(nstr) == 1:
        return True
    elif nstr[0] == nstr[-1]:
        nstr = nstr[1:-1]
        return isPalindrome(nstr)
    else:
        return False
        
        
def findPalindromes(numDigits, toPrint=True):
    ''' Takes all numDigits-digit numbers, multiplies 2 together, and finds largest palindrome '''
    if toPrint == True:
        print 'Testing 2 numbers with %d digits each' % (numDigits)
    
    # Obtain sets of all permutations of numDigits 
    permsList = []
    for i in range(2):
        digitPerms = createPerms(numDigits)
        permsList.append(digitPerms)
    
    # Obtain products of those permutations in a single list
    productList = []
    for a in permsList[0]:
        for b in permsList[1]:
            productList.append(a*b)
    productList.sort(reverse=True)
    
    # Loop through products list and determine whether each item is a palindrome. 
    # This will be done more quickly if you sort the products first and work backwards.
    
    for p in productList:
        if toPrint == True:
            print 'Looping, at product p %d' % p
        if isPalindrome(p):
            if toPrint == True:
                print 'Found the largest palindrome at p = %d' % p
            return p
            break
            

if __name__ == "__main__":
    # createPerms(1)
    # createPerms(2)
    # createPerms(3)
    # print isPalindrome(101)
    # print isPalindrome(100)
    # print isPalindrome(10001)
    # print isPalindrome(1001)
    # print isPalindrome(9999)
    # print isPalindrome(9898)
    print '\n\n\n=============================='
    findPalindromes(3, True)
    