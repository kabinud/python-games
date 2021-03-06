import random

print "What's your name?"

name = raw_input("> ");

print "Hello", name
print "Let's play a game!"
print "In fact, let's play 'Guess the secret number'!"
print "The rules are simple, you just have to try to guess the secret number! You have a limited amount of tries."
print "We will help you out when you make a wrong guess by telling you if the number you picked is bigger or smaller than the secret number."

playing = True
limit = 5
victories = 0

while playing:
	number = random.randint(0, 100)
	tries = 0
	won = False

	while tries <= limit and not won:
		tries += 1
		guess = raw_input("Try number " + str(tries) + ": ")
		if int(guess) == number:
			print "Huuray! You guessed the number!"
			print "Your prize? Who said anything about a prize?"
			won = True
			victories += 1
		elif int(guess) > number:
			print "Why not a smaller number?"
		else:
			print "Why not a bigger number?"

	if not won:
		print "You are a bad guesser. Good luck next time!"

	again = raw_input("Do you want to play again? (y or n) ")

	if again == "n":
		print "Congratulations, %s! You won %d times!" % (name, victories)
		print "Have a good day!"
		playing = False