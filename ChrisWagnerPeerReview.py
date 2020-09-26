# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Chris Wagner
# Creation Date: September 26th, 2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	# A logic error was fixed in the print statement.
	# The original code used triple apostrophes, causing the string to be ignored when the program was run.
	# Now each line of the string has quotation marks on either side to make the string printable.
	# There was also an unnecessary print statement removed.
	print("You are in a land full of dragons. In front of you, "
		  "you see two caves. \nIn one cave, the dragon is friendly "
		  "and will share his treasure with you. \nThe other dragon "
		  "is greedy and hungry, and will eat you on sight.")

def checkCave():
	# The second time.sleep() method had an incorrect parameter. It was changed from 3 seconds to 2 seconds.
	# An extra print statement was removed as it was unnecessary.
	# The print statement in the else conditional was missing parentheses
	# There was no need for a friendlycave variable, so it was removed.
	# The "chooseCave()" function was not needed and its function was replaced with the "chosenCave" input below.
	# chosenCave is no longer a parameter of checkCave()
	chosenCave = int(input("Will you choose cave 1 or 2? "))
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#sleep for 2 seconds
	time.sleep(2)

	# The conditional was fixed so 1 gets you treasure, 2 gets you eaten, and any other number is rejected.
	if chosenCave == 1:
		print('Gives you his treasure!')
	elif chosenCave == 2:
		print('Gobbles you down in one bite!')
	else:
		print('There are only two caves to choose from!')

def main():
	#This main() function was created to make execution of the program easier.
	#The option to play again was added into a main function after displayIntro() and checkCave().
	#The while loop was updated and set to True,
	#and if statements determine whether the program will continue or break
	while True:
		displayIntro()
		checkCave()

		playAgain = input('Do you want to play again? Y/n: ')
		playAgain = playAgain.upper()
		if playAgain == 'Y':
			continue
		elif playAgain == 'N':
			break


main()