#	11. TESTING YOUR CODE
#Testing proves that your code works as it's supposed to in response to
#all the input types  it's designed to receive.
#Every programmer makes mistakes, so every programmer must test their
#code often, catching problems before users encounter them.
#You'll learn to test your code using tools in Python's unittest module.
#You'll see what a passing test looks like and what  a failing test look
#like, and how it can improve your code.

# Testing a function

def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()

# failing Test
