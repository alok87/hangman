#!/usr/bin/python

import random, sys, os, string

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class play:
	attempts = 0 
	maxAttempt = 6
	leftAttempts = 6
	lettersinLine = []
	lettersSelected = [] 
	correctGuess = []
	lettersList = []
	guessState = ''
	gameStatus= ''
		
	def __init__(self):
		self.line = {}
		play.lettersList = range(ord('A'),ord('Z')+1) 
		play.gameStatus=True
		self.playGame()

	def setRandomLine(self):
        	self.line = random.choice(open(sys.argv[1]).readlines())
        	self.line = self.line[:-1]
		self.lengthLine = len(self.line)
		for charLine in self.line:
			charLine = charLine.upper()
			print charLine
			if ord(charLine) >= 65 and ord(charLine) <= 90:
				if ord(charLine) not in play.lettersinLine: 
					play.lettersinLine.append(ord(charLine)) 
			
	def showView(self):
		#os.system('clear')
		print color.BOLD + color.BLUE + "H A N G M A N - Beatles Song" + color.END + "\n", 
		
		# Display the Letter List - showing selected(in green) and not selected letters
		letrCount = 0
		for letr in range(65,91):
			if letrCount%10 == 0:
				print "\n"
			letrCount += 1
			chrNletter = chr(letr)
			if letr in play.lettersList and letr not in play.lettersSelected:
				print " %2s " % chrNletter,
			elif letr in play.lettersSelected:
				print color.BOLD + color.RED + " %2s " % chrNletter + color.END, 

		# Display the answer - Temporary for debug
		# print "\n\nAnswer:\n" + color.BOLD + "%s" % self.line + color.END

		# Attempts Calculation
		print "\n\nAttempts Before You Hang Yourself: " + color.RED + "%s" % play.leftAttempts + color.END + "\n"
		
		# Display Guessed Data 
		for chrt in self.line:	
			chrt = chrt.upper()	
			chrtNum = ord(chrt)
			if chrtNum in range(ord('A'),ord('Z')+1):
				if chrtNum in play.lettersSelected:
					print color.BOLD + "%s" % chrt + color.END,
				else: 
					print color.BOLD + "_" + color.END,				
			else:
				print color.BOLD + chrt + color.END,
		print "\n"


	def takeInput(self):
		while True:
    			userInput = raw_input(color.BOLD + "Input Letter: " + color.END)
    			if len(userInput) == 1:
        			if userInput in string.letters:
            				break
        			print "\n" + color.RED + 'Please enter only letters' + color.END + "\n",
    			else:
        			print "\n" + color.RED + 'Please enter only one character' + color.END + "\n",
		userNum = ord(userInput.upper())

		if userNum in play.lettersList:
			if userNum not in play.lettersSelected:
				play.lettersSelected.append(userNum)	
				if userNum in play.lettersinLine:
					play.correctGuess.append(userNum)
				play.guessState = True
				if userInput.upper() not in self.line:
					play.attempts += 1
					play.leftAttempts -= 1
			else: 	
				print "\n" + color.RED + 'Please do not enter the already selected letters' + color.END + "\n",
				play.guessState = False
		else:
			print "\n" + color.RED + 'Please enter a valid letter from [A-Z] !' + color.END + "\n",
			play.guessState = False
		
	def playGame(self):
		self.setRandomLine()
		while play.attempts < play.maxAttempt:
			self.showView()
			if play.gameStatus == True:   
				play.guessState = False
				while play.guessState != True:
					self.takeInput()					
			print sorted(play.lettersinLine)
			print sorted(play.correctGuess)	
			if sorted(play.lettersinLine) == sorted(play.correctGuess):
				play.gameStatus = False
				self.showView()		
				print "\n" + color.BOLD + color.GREEN + "You Won, You won't hang yourself !" + color.END,
				sys.exit()	
	
		play.gameStatus = False	
		self.showView()		
		print "\n" + color.BOLD + color.RED + "You Lost, You choose to hang yourself !" + color.END,
play()		
