#Visit Project Gutenberg and find a few texts you'd like to analyze.
#Download the text files for these works, or copy the raw text from your
#browser into a text files on your computer.
#You can use the count() method to find out how many times a word or
#phrase appears in a string.
#Write a program that reads the files you found at project gutemberg
#and determines how many times the word 'the' appears in each text.
#Try counting 'the ', with a space in the string.

def word_counter(filename, word):
		"""Return number of times word appears in the file"""
		with open(filename, encoding='utf-8') as f:
				contents = f.read()
		
		word = word
		w_c = contents.lower().count(word)
		print(w_c)

filename = input("Insert file name: ")
word = input("Insert word you want count: ")
word_counter(filename, word)