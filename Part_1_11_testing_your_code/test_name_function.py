#*Unit Test and Test Cases
#Library that provides tools for testing your code
#A unit test verifies that one especific aspect of a function 
#behavior is correct.
#A test case is a collection of unit tests that toguether prove that
#a function behaves as it's supposed to, within the full range of
#situations you expect it to handle.

#*A passing Test

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Test for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 'mozart',
			'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()

#*Responding to a Filed Test
#The best option here is to make the middle name optional.

#*Adding_New_Tests
