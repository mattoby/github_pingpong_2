import unittest

def fun(x):
    return x + 1

def fun2(x):
    '''
    designed to fail.
    '''

    return x + .5

class MyTest(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(3), 4)

    def test_fun2(self):
        self.assertEqual(fun2(3), 5)

if __name__=='__main__':
    unittest.main()

