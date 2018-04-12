#!/usr/bin/env python3

import random, datetime

# generateNumbers function generates random Cash 5 numbers.
def generateNumbers():

	# Open file and print date at top of file.
	lotteryFile = open('cashFive.txt', 'a')

	while True:

		# Ask user how many lottery numbers to generate.
		howMany = int(input('How many numbers to generate?: '))

		# If user has entered the number 0, ask them to try again.
		if howMany == 0:
			print('Please enter a number greater than 0!')
		else:
			break

	# Print timestamp before number(s).
	timeStamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	lotteryFile.write(timeStamp + '\n')	

	# Loop number generation based on user input.
	start = 0
	while (start < howMany):

		# Generate 5 unique random numbers (1-43).
		fiveNums = 0
		myNums = []
		while (fiveNums < 5):
			number = random.randint(1, 43)
			if number in myNums:
				continue
			else:
				myNums.append(number)
				fiveNums += 1

		# Sort numbers accending.
		myNums.sort(key=int)

		# Convert numbers from ints to strings, add a 0 to items less then 10.
		lstStrings = []
		for x in myNums:
			if x < 10:
				lstStrings.append(str(x).zfill(2))
			else:
				lstStrings.append(str(x))

		# Write output to file and to the screen.
		lotteryFile.write(' '.join(lstStrings[0:5]) + '\n')
		print(' '.join(lstStrings[0:5]))
		start += 1

	# Notify user that output was saved to a file.
	print('Number(s) saved to "cashFive.txt".')

	# Print a newline to separate numbers.
	lotteryFile.write('\n')

	# Close file.
	lotteryFile.close()

if __name__ == '__main__':
	generateNumbers()
