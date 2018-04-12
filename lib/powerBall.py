#!/usr/bin/env python3

import random, datetime
from lib import lottoAnalysis

# generateNumbers function generates random Powerball numbers.
def generateNumbers():

	# Open file for appending generated number(s).
	lotteryFile = open('powerBall.txt', 'a')

	# Ask user if they want to perform analysis for repeat winning numbers.
	pAnalysis = input('Would you like to check for duplicate winning numbers? (y/n): ')
	if pAnalysis == 'y':
		numData = lottoAnalysis.lottoAnalyze()
	else:
		print('No analysis will be performed.')
	
	# Ask user if they would like to prevent winning numbers from randomly being generated.
	preventWins = input('Would you like to prevent numbers that have won from being randomly generated? (y/n): ')

	# If preventWins is 'y', fetch lottoList() to create list for comparison if pAnalysis is not 'y'.
	if preventWins == 'y' and pAnalysis != 'y':
		numData = lottoAnalysis.lottoList()
		print('Numbers that have won won\'t be generated.')
	elif preventWins == 'y' and pAnalysis == 'y':
		print('Numbers that have won won\'t be generated.')
	else:
		print('Numbers that have won can be generated.')

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

		# Generate 5 unique random numbers (1-69).
		fiveNums = 0
		myNums = []
		while (fiveNums < 5):
			number = random.randint(1, 69)
			if number in myNums:
				continue
			else:
				myNums.append(number)
				fiveNums += 1
		
		# Generate random Powerball number (1-26).
		powerBall = random.randint(1, 26)

		# Sort numbers accending.
		myNums.sort(key=int)

		# Convert numbers from ints to strings, add a 0 to items less then 10.
		lstStrings = []
		for x in myNums:
			if x < 10:
				lstStrings.append(str(x).zfill(2))
			else:
				lstStrings.append(str(x))
		if powerBall < 10:
			lstStrings.append(str(powerBall).zfill(2))
		else:
			lstStrings.append(str(powerBall))

		# If preventWins is 'y', generate another number if there is a match, else write to lotteryFile.
		if preventWins == 'y':
			# Join numbers together for comparison.
			compareNum = ''.join(lstStrings)
			
			# Compare generated number with numbers in numData.
			if compareNum in numData:
				continue

		# Write output to file and to the screen.
		lotteryFile.write(' '.join(lstStrings[0:5]) + ' PB: ' + lstStrings[5] + '\n')
		print(' '.join(lstStrings[0:5]), 'PB:', lstStrings[5])
		start += 1

	# Notify user that output was saved to a file.
	print('Number(s) saved to "powerBall.txt".')
	
	# Print a newline to separate numbers.
	lotteryFile.write('\n')

	# Close file.
	lotteryFile.close()

if __name__ == '__main__':
	generateNumbers()
