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
__execution__ = "python exam3.py"
#------------------------------------------------------------------------------
# Library
import random

#------------------------------------------------------------------------------
class BitwiseClass():
	def __init__(self):
		self.list = [0x0f,0x00,0xa0,0x23,0x01,0xf1,0xa9,0x20,0x33,0x77,\
					 0x67,0x55,0xb2,0xdc,0x37,0x11,0x99,0xaa,0x89,0x69]
		self.list2 = []
		self.list3 = []
		self.list4 = []
		self.list5 = []
		self.mask = 0xff #mascara para corrimiento
		self.r = 0
		
	def ANDoperation(self):
		for i in self.list:
			self.list2.append(i)
		for i in range(len(self.list)):
			self.r = self.list[i] & self.mask		
			self.list2.append(self.r)
		print(self.list2)
	def ORoperation(self):
		for i in self.list:
			self.list3.append(i)
		for i in range(len(self.list)):
			self.r = self.list[i] | self.mask		
			self.list3.append(self.r)
		print(self.list3)
	def XORoperation(self):
		for i in self.list:
			self.list4.append(i)
		for i in range(len(self.list)):
			self.r = self.list[i] ^ self.mask		
			self.list4.append(self.r)
		print(self.list4)	
	def SHIFToperation(self):
		for i in self.list:
			self.list5.append(i)
		for i in range(len(self.list)):
			self.r = self.list[i] << 2		
			self.list5.append(self.r)
		print(self.list5)
		


#------------------------------------------------------------------------------
if __name__ == "__main__":
	j = BitwiseClass()
	j.ANDoperation()
	j.ORoperation()
	j.XORoperation()
	j.SHIFToperation()
#------------------------------------------------------------------------------