#access libraries and py files 
import spiderDraw as sd
import functions as md
import time, os

print("Welcome!")

#Initialize variables and setup 
#Need to keep track of correct letters, incorrect letters and tries

correct = []  #List of correct letters guessed
incorrect = []  #List of incorrect letters guessed
tries = 0   #Number of incorrect guesses
game = True 

# track wins and losses
wins = 0
losses = 0

#Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]


#Print intro statements (welcome to game, etc)
md.introduction()



#generate a random word from word list
word = md.generate_word()




#Game Loop
while game: 
  progress = ''
  tries = md.check_word(correct, incorrect,word, tries)
  time.sleep(1)
  os.system('clear')
  progress = md.print_word(word,correct)
  print(f'Word = {progress}')
  md.print_spider(tries,spiderList)
  print(f'Incorrect Guesses = {incorrect}')
  print(f'Wins = {wins} | Losses = {losses}')

  #This is where you'll call all of your functions. Just need to decide the proper order.


  #You will also need to specify your win and lose conditions in here
  if '_' not in progress:
    print('Congrats, you win!')
    wins += 1
    
    again= input('Do you want to play agin? (y/n)')
    if again == 'y':
      correct.clear()
      incorrect.clear()
      tries = 0
      word = md.generate_word()
      os.system('clear')
      progress = md.print_word(word,correct)
      md.print_spider(tries,spiderList)
      print(f'Word = {progress}')
      print(f'Incorrect Guesses = {incorrect}')
      print(f'Wins = {wins} | Losses = {losses}')

    else:
      if again == 'n':
        print('Thanks for playing!')
        game = False
      print(f'Final Score - Wins: {wins}, Losses: {losses}')
      
  elif tries > 5:
    print('The spider has devoured you!')
    losses += 1
    again = input('Do you want to play again? (y/n): ').lower()
    if again == 'y':
        correct.clear()
        incorrect.clear()
        tries = 0
        word = md.generate_word()
        os.system('clear')
        progress = md.print_word(word, correct)
        md.print_spider(tries, spiderList)
        print(f'Word = {progress}')
        print(f'Incorrect Guesses = {incorrect}')
    else:
        if again == 'n':
          print('Thanks for playing!')
        print(f'Final Score - Wins: {wins}, Losses: {losses}')
        game = False



