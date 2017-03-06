import unittest
from primeNumbers import primeNumbers
class TestSolution(unittest.TestCase):

	def test_alphabet(self):
		self.assertTrue(type, int)

	def test_one(self):
		self.assertEqual(primeNumbers (1),"Null")
		
	def test_negative(self):
		self.assertEqual(primeNumbers(-1),"The number must be positive")

	def test_ifEmpty(self):
		self.assertEqual(primeNumbers(""),"Input a number")
	
	def test_ifPrime(self):
		self.assertEqual(primeNumbers(10),[2,3,5,7])

	


if __name__ =="__main__":
	unittest.main()