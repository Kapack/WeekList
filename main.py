#!/usr/bin/env python2.7
from lib.CreateNewFolder.CreateNewFolder import CreateNewFolder
from lib.PrepareForEAN.PrepareForEAN import PrepareForEAN
from lib.Wepack.Wepack import Wepack

class Main:
	def __init__(self):
		whatToDo = self.whatToDo()
		# whatToDo = 2

		# Which method to run depending on 
		if whatToDo == 1:
			self.createTheFolder()
		
		elif whatToDo == 2:
			self.prepareForEAN()
		
		elif whatToDo == 3:
			self.createChecklistToWePack()

		else:
			print('Your choice is not valid')

	def whatToDo(self):
		userInput = input('What do you want to do? \n 1: Create a new Folder? \n 2: Prepare for EAN and upload TVC-list to Drive? \n 3: Update Stock and send to Pavo and Friends? \n')
		return userInput

	def createTheFolder(self):
		CreateNewFolder()
	
	def prepareForEAN(self):
		PrepareForEAN()
	
	def createChecklistToWePack(self):
		wepack = Wepack()
		wepack.createChecklist()
	
if __name__ == '__main__':
	Main()