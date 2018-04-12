# lotteryNumbers
Python scripts for generating pseudo-random lottery numbers. Use lotteryNumbers.py to select which game and enter the amount of numbers you want to generate. This will output individual text files for each of the lottery games.

Powerball numbers also have the additional ability to perform analysis on winning number history. Powerball number generation can also skip any numbers that have previously won if user desires.


### Examples:

```
What type of lottery number(s) would you like the generate?
Cash Five = 1, Powerball = 2, Mega Millions = 3: 1
How many numbers to generate?: 5
13 15 16 33 37
01 04 15 24 27
03 09 10 22 26
01 13 18 31 32
04 15 26 37 41
Number(s) saved to "cashFive.txt".
```
```
What type of lottery number(s) would you like the generate?
Cash Five = 1, Powerball = 2, Mega Millions = 3: 2
Would you like to check for duplicate winning numbers? (y/n): y
Downloading winning numbers from powerball.com...
Removing header, Date, and PowerPlay number from file...
Writing numbers for analysis to "lottoDatabase.txt"...
No duplicate winning numbers found!
Would you like to prevent numbers that have won from being randomly generated? (y/n): y
Numbers that have won won't be generated.
How many numbers to generate?: 5
14 20 23 43 49 PB: 24
15 24 32 61 62 PB: 19
55 56 57 60 68 PB: 10
19 25 51 68 69 PB: 08
04 08 16 23 67 PB: 07
Number(s) saved to "powerBall.txt".
```
```
What type of lottery number(s) would you like the generate?
Cash Five = 1, Powerball = 2, Mega Millions = 3: 3
How many numbers to generate?: 5
20 21 25 42 48 MB: 03
14 20 23 25 27 MB: 12
09 44 57 63 69 MB: 18
22 29 36 37 49 MB: 16
18 28 36 48 52 MB: 23
Number(s) saved to "megaMillions.txt".
```
