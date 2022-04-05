#	TESTING A CLASS
#You'll write test for a class

#*A Variety of Assert Methods
#Assert methods test whether a condition you believe is true at a
#especific point in your code is indeed true. If the condition
#is true as expected, your asumption about how that part of your 
#program behaves is confirmed; you can be confident that no errors
#exist. 

#*A Class to Test
#There are a few differences betwen test a function and test a class

class AnonymousSurvey:

	def __init__(self, question):
		"""Store a question, and prepare to store responses."""
		self.question = question
		self.responses = []

	def show_question(self):
		"""Show the survey question."""
		print(self.question)

	def store_response(self, new_response):
		"""Store a single response to the survey."""
		self.responses.append(new_response)

	def show_results(self):
		"""Show all the responses that have been given."""
		print("Survey results:")
		for response in self.responses:
			print(f"- {response}")