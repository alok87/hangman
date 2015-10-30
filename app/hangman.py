#!/usr/bin/python

import random, sys, os, string

class Play:
	data_file = 'tmp/beatlesHits.lst'

	def __init__(self):
		self.attempts = 1
		self.max_try = 7
		self.left_try = 7

		self.ltrs_in_line = []
		self.ltrs_selectd = []
		self.ltrs_gussed = []
		self.ltrs_list = {}

		self.line = {}
		for key in range(65,91):
			self.ltrs_list[key] = chr(key)
		self.set_random_line()

	def get_line(self):
		return self.line

	def set_random_line(self):
		self.line = random.choice(open(self.data_file).readlines())
		self.line = self.line[:-1]
		for char_line in self.line:
			char_line = char_line.upper()
			if ord(char_line) >= 65 and ord(char_line) <= 90:
				if ord(char_line) not in self.ltrs_in_line:
					self.ltrs_in_line.append(ord(char_line))

	def show_box(self):
		output = []
		for chrt in self.line:
	    		chrt = chrt.upper()
	        	char_num = ord(chrt)
	        	if char_num in range(ord('A'),ord('Z')+1):
	                	if char_num in self.ltrs_selectd:
	                        	output.append(chrt)
	                	else:
	                        	output.append("_")
	        	else:
	        		output.append(chrt)
		return output

	def process_input(self, input):
		user_num = ord(input)
	    	if user_num in self.ltrs_list.keys():
	    		if user_num not in self.ltrs_selectd:
	        		self.ltrs_selectd.append(user_num)
	            		if user_num in self.ltrs_in_line:
	            			self.ltrs_gussed.append(user_num)
					return 0
	            		elif input not in self.line:
	                		self.attempts += 1
	                		self.left_try -= 1
					return 1
			else:
				return 2
		else:
				return 2

	def check_result(self):
		print self.ltrs_in_line
		print self.ltrs_gussed
		if self.attempts < self.max_try:
			if sorted(self.ltrs_in_line) == sorted(self.ltrs_gussed):
                        	output = "0" #game won
			else:
				output = "2" #game is still on
		else:
			output = "1" #lost
		return output
