import unittest
from simple_calculator import SimpleCalculator

def test_simple_calculator(unitest.testCase):
	
	test_add(self):
		self.assertEqual(add(3,4),7)
		self.assertEqual(add(3,-4),-1)

	test_subtract(self):
		self.assertEqual(subtract(4,3),1)
		self.assertEqual(subtract(4,-3),7)

	test_multiply(self):
		self.assertEqual(multiply(3,4),12)
		self.assertEqual(multiply(3,0),0)
		self.assertEqual(multiply(3,-4),-12)

	test_divide(self):
		self.assertEqual(devide(4,2),2)
		self.assertEqual(devide(3,2),1.5)
		with self.assertRaises(ZeroDivisionError) :
			divide(4,0)
		
if __name__ == '__main__':
    unittest.main()
	
