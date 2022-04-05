#Write a while loop that prompts users for their name. When they enter
#their name, print a greeting to the screen and add a line recording
#their visit in a file called guest book.txt. Make sure each entry
#appears on a new line in the file.

name = ''

while True:

	if name == 'exit':
		break

	else:

		prompt = "Write your name or write 'exit' if you were done: "

		name = input(prompt)

		filename = "guest_book.txt"

		if name != "exit":

			print(f"Welcome {name}")

		if name != "exit":

			with open(filename, 'a') as file_object:
				file_object.write(f"{name}\n")
