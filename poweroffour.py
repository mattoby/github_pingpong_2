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
    '''
    Determines if a number 'num' is a square.
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
    :type num: int
    :rtype: bool
    """

    ispoweroffour = False

    issquare, root = isSquare(num)
    if issquare:
        ispoweroffour, fourthroot = isSquare(root)

    return ispoweroffour




