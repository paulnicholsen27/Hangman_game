from random import randint
import sys
import os

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=80))
os.system("clear")
def generate_word():
	f = open('hangmandictionary.txt')
    new_dictionary = [word[:-2] for word in f if 5 < len(word) < 11]
	f.close()
	secret_word = new_dictionary[randint(0,len(new_dictionary)-1)]
	word_length = len(secret_word)
	return secret_word, word_length


def make_a_guess(guessed_so_far):
	guess = raw_input("Guess a letter: ").lower()
	while len(guess) != 1 or not guess.isalpha():
		print "That is not a valid letter.  Try again."
		guess = make_a_guess(guessed_so_far)
	if guess in guessed_so_far:
		print "You already guessed that letter.  Try again."
		guess = make_a_guess(guessed_so_far)
	return guess
		
def draw_hangman(n):
	hangman_pics = ["""
\n
  +---+\r
  |   |\r
      |\r
      |\r
      |\r
      |\r
 =========\r""", '''
\n
  +---+\r
  |   |\r
  O   |\r
      |\r
      |\r
      |\r
 =========\r''', '''
\n
  +---+\r
  |   |\r
  O   |\r
  |   |\r
      |\r
      |\r
 =========\r''', '''
\n
  +---+\r
  |   |\r
  O   |\r
 /|   |\r
      |\r
      |\r
 =========\r''', '''
\n
  +---+\r
  |   |\r
  O   |\r
 /|\  |\r
      |\r
      |\r
 =========\r''', '''
\n
  +---+\r
  |   |\r
  O   |\r
 /|\  |\r
 /    |\r
      |\r
 =========\r''', '''
\n
  +---+\r
  |   |\r
  O   |\r
 /|\  |\r
 / \  |\r
      |\r
 =========\r''', '''
 \n
    \O/\r
     |\r
    / \ \r
\n''' 
 ]
 	print hangman_pics[n]

def word_printer(secret_word, guessed_so_far):
	hidden_word = ""
	for letter in secret_word:
		if letter in guessed_so_far:
			hidden_word += (letter + " ")
		else:
			hidden_word += "__ "
	return hidden_word

def play_again():
	play_again = raw_input("Would you like to play again? (y/n)")
	if play_again == 'y'or play_again == 'Y':
		word_generator()
		hangman()
	else:
		print "OK--thanks for playing!"
		raise SystemExit

def hangman():
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
	secret_word, word_length = word_generator()
	guessed_so_far = []
# 	print secret_word
	hidden_word = word_printer(secret_word, guessed_so_far)
	bad_letters=[]
	n = 0
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )

	draw_hangman(n)
	print hidden_word

	while n <= 6:
		if n == 6:
			print "Sorry, you have lost."
			print "The word was: '"+secret_word+"'"
			play_again()
		if hidden_word.find("__ ") == -1:
			draw_hangman(7)
			print "You have saved the Hangman!"
			print "\n"
			print "The word was: '"+secret_word+"'!"
			play_again()
		else:
			letter_guess = make_a_guess(guessed_so_far)
			guessed_so_far.append(letter_guess)	
			if letter_guess not in secret_word:
				bad_letters.append(letter_guess)
				n += 1
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		draw_hangman(n)
		hidden_word = word_printer(secret_word, guessed_so_far)
		print hidden_word
		print "Incorrect letters: ", bad_letters

	
		
hangman()
