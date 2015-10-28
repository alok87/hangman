#!/usr/bin/python

import random, sys, os, string

class Play:
	attempts = 1
	maxAttempt = 7
	leftAttempts = 7
	dataFile = 'tmp/beatlesHits.lst.new'

	lettersinLine = []
	lettersSelected = []
	correctGuess = []
	lettersList = {}

	def __init__(self):
		self.line = {}
		for key in range(65,91):
			Play.lettersList[key] = chr(key)
		self.setRandomLine()

	def getLine(self):
		return self.line

	def resetInstance(self):
		self.lettersinLine = []
		self.lettersSelected = []
		self.correctGuess = []
		self.setRandomLine()

	def setRandomLine(self):
		self.line = random.choice(open(Play.dataFile).readlines())
		self.line = self.line[:-1]
		self.lengthLine = len(self.line)
		for charLine in self.line:
			charLine = charLine.upper()
			if ord(charLine) >= 65 and ord(charLine) <= 90:
				if ord(charLine) not in Play.lettersinLine:
					Play.lettersinLine.append(ord(charLine))

	def showGuessedBox(self):
		output = []
		for chrt in self.line:
	    		chrt = chrt.upper()
	        	chrtNum = ord(chrt)
	        	if chrtNum in range(ord('A'),ord('Z')+1):
	                	if chrtNum in Play.lettersSelected:
	                        	output.append(chrt)
	                	else:
	                        	output.append("_")
	        	else:
	        		output.append(chrt)
		return output

	def processInput(self, input):
		userNum = ord(input)
	    	if userNum in Play.lettersList.keys():
	    		if userNum not in Play.lettersSelected:
	        		Play.lettersSelected.append(userNum)
	            		if userNum in Play.lettersinLine:
	            			Play.correctGuess.append(userNum)
					return 0
	            		elif input not in self.line:
	                		Play.attempts += 1
	                		Play.leftAttempts -= 1
					return 1
			else:
				return 2
		else:
				return 2

	def checkResult(self):
		if Play.attempts < Play.maxAttempt:
			if sorted(Play.lettersinLine) == sorted(Play.correctGuess):
                        	output = "0" #game won
			else:
				output = "2" #game is still on
		else:
			output = "1" #lost
		return output
