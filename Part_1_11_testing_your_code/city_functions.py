#def city_country(city, country):
#	"""Organize city and country in the form 'City, Country'"""
#	city_country = f"{city}, {country}"
#	return city_country.title()

def city_country(city, country, population=''):
	"""Organize city and country in the form 'City, Country'"""
	city_country = f"{city}, {country} - population {population}"
	return city_country.title()