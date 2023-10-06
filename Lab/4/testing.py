# lab 4
# https://docs.google.com/document/d/1FNMzdhH01qCwqy9iaURvJIBB-H2uYIW8/edit

def is_prime(number):
    # number is int and > 1    
    for i in range(2, number//2 + 1):
            # from 2...to...half of number
            
            # if number mod i (divide by i and return remainder) is equal to zero, is_factor true. 
            is_factor = number % i == 0 
            if is_factor:
                # number ain't prime
                return False
    # got through for loop prime checker without returning false, so 
    return True

def decompose(number, results):
        for i in range(2, number +1):
            if number % i == 0:
                # divisible by i, we found a factor, now look for the next one
                results.append(i)
                return decompose(number//i, results)

def prime_decomposition(number):
    results = []
    decompose(number, results)
    return results

import unittest
#decomp.prime_decomposition()
# Write a function called prime_decomposition, that receives as input a positive integer, and returns a list with the prime number decomposition of the number received as input. For example, prime_decomposition(2) returns [2], prime_decomposition(10) returns [2,5], and prime decomposition(12) returns [2,2,3]. You do not have to perform error checking on the input.

"""
Test cases:
0 -> []
1 -> []
2 -> [2]
10 -> [2,5]
12 -> [2,2,3]
"""
class PrimeDecomposition(unittest.TestCase):
    def runner(self,a,b):
        self.assertEqual(a,b)
    def test_checkInputOutput(self):
        tests = ((0,[]),
                 (1,[]),
                 (2,[2]),
                 (7,[7]),
                 (47,[2,2,2,2,3]))

        for test in tests:
            self.runner(prime_decomposition(test[0]),test[1])
    def test_TestBurningInHell(self):
        self.assertEqual(prime_decomposition(48),[2,2,2,2,3])
    
if __name__=="__main__":
    unittest.main()