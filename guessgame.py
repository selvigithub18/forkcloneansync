# This is a game to guess numbers
import random
secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 to 20")
#Ask the user to guess a number
for guessesTaken in range (1,7):
	print ("Take a guess")
	guess = int(input())

	if guess < secretNumber:
		print("your guess is low, try again")
	elif guess > secretNumber:
		print("your guess is high, try again")
	else:
		break
if guess == secretNumber:
	print("Hooray you guessed it in " + str(guessesTaken) + " times")
else:
	print("Nope. The number i was thinking was " + str(secretNumber))
