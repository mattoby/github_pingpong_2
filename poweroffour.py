'''
Problem:
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example:
Given num = 16, return true. Given num = 5, return false.
Follow up: Could you solve it without loops/recursion?
'''

#class Solution(object):
#def isPowerOfFour(self, num):

def isSquare(num):

    """Test Cases

    >>> isSquare(4)
    True

    >>> isSquare(-2)
    False

    >>> isSquare(3)
    (False, [])

    >>> isSquare(1)
    (True, 1)

    >>> isPowerOfFour(4)
    True

    >>> isPowerOfFour(0)
    False

    >>> isPowerOfFour(1)
    True

    >>> isPowerOfFour(16)
    True

    >>> isPowerOfFour(14)
    False

    >>> isPowerOfFour(3)
    False

    """


    # Comments for the function isSquare:

    # Seems like it does more than returning justa binary True False,
    # it returns a tuple with True/False as first element and
    # the square root of the number as the second element.


    # Also it fails for the test case isSquare(3). 



    # Comments for the function ispoweroffour:

    ## Cases it works for:
    #
    # It works for powers of 4 when the power is greater than or equal to one


    ## Cases it breaks under:
    #
    # When it is not a power of 4. Like 3 or 14 then we get error not False 
    # When the power is 0. For 4^0 = 1, we get False not True

    '''
    Determines if a number 'num' is a square.

    The algorithm checks num for being equal to each whole square number up to (num/2)^2, and then stops searching if num is not found to be equal to any square number in that range.

    '''
    root = []
    issquare = False

    for n in [x+1 for x in range(num/2)]:
        currsquare = n*n
        if num==currsquare:
            issquare = True
            root = n
            break
        if num<currsquare:
            break

    return issquare, root


def isPowerOfFour(num):
    """
    Checks for num being a fourth root, by checking if it is the square of a square (e.g., to check if num=x*x*x*x where x is an integer, this checks the equivalent statements that num=y*y and y=x*x, where x and y are both integers).

    :type num: int
    :rtype: bool
    """

    ispoweroffour = False

    issquare, root = isSquare(num)
    if issquare:
        ispoweroffour, fourthroot = isSquare(root)

    return ispoweroffour


if __name__ == '__main__':
    import doctest
    doctest.testmod()



