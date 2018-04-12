#!/usr/bin/env python3

import re
from lib import lottoDatabase

# lottoList function creates a list of integers for easier analysis.
def lottoList():

	# Call lottoDatabase.py to download current winning numbers.
	lottoDatabase.lottoData()

	# Load lottoDatabase.txt into list.
	with open('lottoDatabase.txt', 'r') as winList:
		numData = list(winList)

	# Remove newlines from number list data.
	numData = [x.strip() for x in numData]

	# Required to return numData as a list of strings (integers wouldn't return leading 0).
	return(numData);

# lottoAnalyze function takes list of winning numbers and looks for duplicates.
def lottoAnalyze():

	# Get lottoList.
	numData = lottoList()

	# Create empty dictionary for storing matches, and empty list for handling duplicates.
	matchList = {}
	dupeList = []

	# Compare winning numbers to the rest of the list.
	for x, valx in enumerate(numData):
		for y, valy in enumerate(numData):

			# If x and y index are the same they are not a valid match, continue to next y index item.
			if x == y:
				continue

			# If valx is equal to valy match is valid unless also in dupeList.
			if valx == valy and x not in dupeList:

				# If number is already a key in matchList add to value, else create new entry.
				if valx in matchList:
					matchList[valx] += 1
				else:
					matchList[valx] = 1

				# Add y to dupeList so no inverse duplicates are added to matchList.
				dupeList.append(y)

	# Notify user if there are no winning matches, if there are winning matches print them to screen.
	if not matchList:
		print("No duplicate winning numbers found!")
	else:
		for key,val in matchList.items():
			number = re.sub(r'(\d{2})', r'\1 ', key)
			print('{:.14}'.format(number), "PB:", number[15:17], "won", val, "time(s).")

	return(numData);

if __name__ == '__main__':
	lottoAnalyze()

