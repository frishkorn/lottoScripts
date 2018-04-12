#!/usr/bin/env python3

import urllib.request, re, sys

# lottoData function downloads winning lottery numbers and cleans them up for analysis.
def lottoData():

	# Fetch powerball number history text file.
	print('Downloading winning numbers from powerball.com...')
	try:
		url = 'http://www.powerball.com/powerball/winnums-text.txt'  
		urllib.request.urlretrieve(url, 'winnums-text.txt')
	except urllib.error.URLError:
		print("Unable to access winnums-text.txt!")
		sys.exit()

	# Open winnums-text.txt and clean-up using regex to lottoDatabase.txt.
	print('Removing header, Date, and PowerPlay number from file...')
	with open('winnums-text.txt', 'r') as dataFile, open('lottoDatabase.txt', 'w') as outputFile:
		for line in dataFile:
	
			# Remove header from dataFile.
			if re.match(r'^\D', line) is not None:
				continue
	
			# Remove Date, Power Play number, and replace with just winning numbers.
			else:
				nums = re.sub(r'^(\d+/){2}\d+\s+((\d+\s+){6}).*', r'\2', line)
	
			# Sort first five numbers in ascending order into a list, keeping powerball number at the end. 
			numList = nums.split("  ")
			numList[0:5] = sorted(numList[0:5])

			# Turn list into a single string.
			orderedNums = ''.join(numList)
			
			# Write regexed and sorted line to lottoDatabase.txt.
			outputFile.write(orderedNums)

	print('Writing numbers for analysis to "lottoDatabase.txt"...')

if __name__ == '__main__':
	lottoData()

