import unittest
from assignment1 import is_prime, are_relatively_prime, primes, prime_decomposition
class TestFirstAssignment(unittest.TestCase):
    def test_isPrimeGivesCorrectAnswerForNEqualTwo(self):
        self.assertEqual(True, is_prime(2))
    
if __name__=="__main__":
    unittest.main()
