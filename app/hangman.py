#!/usr/bin/python

import random, sys, os, string

class Play:
	dataFile = 'tmp/beatlesHits.lst'

	def __init__(self):
		self.attempts = 1
		self.maxAttempt = 7
		self.leftAttempts = 7


		self.lettersinLine = []
		self.lettersSelected = []
		self.correctGuess = []
		self.lettersList = {}

		self.line = {}
		for key in range(65,91):
			self.lettersList[key] = chr(key)
		self.setRandomLine()

	def getLine(self):
		return self.line

	def resetInstance(self):
		self.lettersinLine = []
		self.lettersSelected = []
		self.correctGuess = []
		self.setRandomLine()

	def setRandomLine(self):
		self.line = random.choice(open(self.dataFile).readlines())
		self.line = self.line[:-1]
		self.lengthLine = len(self.line)
		for charLine in self.line:
			charLine = charLine.upper()
			if ord(charLine) >= 65 and ord(charLine) <= 90:
				if ord(charLine) not in self.lettersinLine:
					self.lettersinLine.append(ord(charLine))

	def showGuessedBox(self):
		output = []
		for chrt in self.line:
	    		chrt = chrt.upper()
	        	chrtNum = ord(chrt)
	        	if chrtNum in range(ord('A'),ord('Z')+1):
	                	if chrtNum in self.lettersSelected:
	                        	output.append(chrt)
	                	else:
	                        	output.append("_")
	        	else:
	        		output.append(chrt)
		return output

	def processInput(self, input):
		userNum = ord(input)
	    	if userNum in self.lettersList.keys():
	    		if userNum not in self.lettersSelected:
	        		self.lettersSelected.append(userNum)
	            		if userNum in self.lettersinLine:
	            			self.correctGuess.append(userNum)
					return 0
	            		elif input not in self.line:
	                		self.attempts += 1
	                		self.leftAttempts -= 1
					return 1
			else:
				return 2
		else:
				return 2

	def checkResult(self):
		print self.lettersinLine
		print self.correctGuess
		if self.attempts < self.maxAttempt:
			if sorted(self.lettersinLine) == sorted(self.correctGuess):
                        	output = "0" #game won
			else:
				output = "2" #game is still on
		else:
			output = "1" #lost
		return output
