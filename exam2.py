#!/usr/bin/env oython3
#-*- coding: utf -8 -*-
#----------------------------------------------------------
__author__ = "Jhon Toro"
__copyright__ = "Copyright 2018, ST Projects"
__credits__ = "Jhon"
__license__ = "GLP 2"
__version__ = "1.0.1"
__maintainer__ = "JFTM"
__email__ = "jhontoro.m7@gmail.com"
__status__ = "active"
__execution__ = "python exam1.py"
#----------------------------------------------------------
# Library
import random
#----------------------------------------------------------
class myFirstClass():
	def __init__(self):
		self.list1 = [1,2,3,4,5,6]
		self.list2 = []
		self.a = 3
		self.b = random.randint(1,10)
		
	def function1(self):
		if(self.a == self.b):
			print(self.a)
			print("YOU ARE THE WINNER")
		else:
			print(self.b)
			print("YOU ARE A LOSER")
	
	def function2(self):
		for i in self.list1:
			self.list2.append(i)
			print(i)
		print(len(self.list1))
		print(len(self.list2))
		
		random.shuffle(self.list2)
		if self.list2[4] == 5 :
			print("correct")
		else:
			print("incorrect")
#----------------------------------------------------------
#execution
if __name__ == "__main__":
	j = myFirstClass()
	j.function1()
	j.function2()
