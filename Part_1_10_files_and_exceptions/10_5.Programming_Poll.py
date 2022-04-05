#Write a while loop that asks people why they like programming. Each
#time someone enters a reason, add their reason to a file that stores
#all the responses.

reason = ''

while True:

	if reason == 'exit':
		break

	else:

		prompt = "Write 'why do you like programming' or 'exit' if you were done: "

		reason = input(prompt)

		filename = "Programming_Poll.txt"

		if reason != "exit":

			with open(filename, 'a') as file_object:
				file_object.write(f"{reason}\n")