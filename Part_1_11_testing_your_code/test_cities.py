import unittest
from city_functions import city_country

#class CitiesTestCase(unittest.TestCase):
#	"""Test for city_functions.py"""

#	def test_city_country(self):
#		"""Do city like Bogota and country like Colombia work?"""
#		city_country_form = city_country('bogota', 'colombia')
#		self.assertEqual(city_country_form, 'Bogota, Colombia')

class CitiesTestCase(unittest.TestCase):
	"""Test for city_functions.py"""

	def test_city_country(self):
		"""Do city like Bogota and country like Colombia work with 
		population?"""
		city_country_form = city_country('bogota', 'colombia', '7181000000')
		self.assertEqual(city_country_form, 
			'Bogota, Colombia - Population 7181000000')

	def test_city_country_population(self):
		"""Do city like Bogota and country like Colombia work with 
		population?"""
		city_country_form = city_country('bogota', 'colombia', '7181000000')
		self.assertEqual(city_country_form, 
			'Bogota, Colombia - Population 7181000000')

if __name__ == '__main__':
	unittest.main()