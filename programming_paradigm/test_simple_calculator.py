import unittest
from simple_calculator import SimpleCalculator

def TestSimpleCalculator(unitest.testCase):

	def setUp(self):
        	self.calc = SimpleCalculator()
	
	test_add(self):
		self.assertEqual(calc.add(3,4),7)
		self.assertEqual(calc.add(3,-4),-1)

	test_subtract(self):
		self.assertEqual(calc.subtract(4,3),1)
		self.assertEqual(calc.subtract(4,-3),7)

	test_multiply(self):
		self.assertEqual(calc.multiply(3,4),12)
		self.assertEqual(calc.multiply(3,0),0)
		self.assertEqual(calc.multiply(3,-4),-12)

	test_divide(self):
		self.assertEqual(calc.devide(4,2),2)
		self.assertEqual(calc.devide(3,2),1.5)
		with self.assertRaises(ZeroDivisionError) :
			calc.divide(4,0)
		
if __name__ == '__main__':
    unittest.main()
	
