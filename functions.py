import random


# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.
def check_word(correct, incorrect, word, tries):
  guess = input('Guess a letter: ').lower()
  if not guess.isalpha() or len(guess) != 1: 
    print('Please enter a single letter.')
    check_word(correct, incorrect, word, tries) 
  if guess in incorrect or guess in correct:
    print('You already guessed that!')
    
  elif guess in word:
    correct.append(guess)
    print('Nice! The letter is there\n')
  else:
    incorrect.append(guess)
    tries += 1
    print('Uh oh, that was wrong\n')
  return tries
  





# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(word,correct):
  progress = ''
  for character in word:
    if character in correct:
      progress = progress + character
    else:
      progress = progress + '_'
  return progress



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()
  
    



#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordList = open('words.txt').read().split()
  word = random.choice(wordList)
  print('Word = ' + '_'*len(word))
  return word


  

#Put the introduction code/input player name into here 
def introduction():
  print('Welcome to Hangman!')
  name = input('What is your name? ')
  print(f'Hello {name}! Good luck!')
  print("Try to guess the word before the spider gets hung!")


