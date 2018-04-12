#!/usr/bin/env python3

from lib import cashFive, powerBall, megaMillions

# Ask user what type of lottery number they want to generate.
while True:
	print('What type of lottery number(s) would you like the generate?')
	lotteryType = int(input('Cash Five = 1, Powerball = 2, Mega Millions = 3: '))

	# Only allow a valid selection, otherwise have user retry.
	if lotteryType not in (1,2,3):
		print('Invalid selection!')
	else:
		break

# Call Cash Five script.
if lotteryType == 1:
	cashFive.generateNumbers()

# Call Powerball script.
if lotteryType == 2:
	powerBall.generateNumbers()

# Call Mega Millions script.
if lotteryType == 3:
	megaMillions.generateNumbers()

