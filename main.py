#!/usr/bin/env python3.0
from lib.CreateNewFolder.CreateNewFolder import CreateNewFolder
from lib.PrepareForEAN.PrepareForEAN import PrepareForEAN
from lib.Wepack.CreateChecklist import CreateChecklist
from lib.Wepack.UpdateLocationQty import UpdateLocationQty
from lib.Import.ReadyToImport import ReadyToImport
from lib.CreateImage.AdditionalImage import AdditionalImage


from lib.Shared import Shared

from config.definitions import WEEKLIST_DIR

class Main:
	def __init__(self):
		whatToDo = self.whatToDo()		
		# whatToDo = '5'

		# Which method to run depending on 
		if whatToDo == '1':
			self.createTheFolder()
		
		elif whatToDo == '2':
			self.prepareForEAN()
		
		elif whatToDo == '3':
			self.createChecklistToWePack()
		
		elif whatToDo == '4':
			self.updateLocationAndQty()
		
		elif whatToDo == '5':
			self.createAddImageList()

		elif whatToDo == '6':
			self.readyToImport()
		
		elif whatToDo == '9':
			self.openWeekListFolder()

		else:
			print('Your choice is not valid')
	# 0
	def whatToDo(self):
		userInput = input('What do you want to do? \n 1: Create a new Folder? (SKU\'s is done.) \n 2: Prepare for EAN and upload TVC-list to Drive? (SKU\'s done. Upload EAN to TVC) \n 3: Update Stock and send to Pavo and Friends? (List is back from TVC) \n 4: Update location and QTY (List is back from WePack) \n 5: Create Additional image list \n 6: List is ready to import! \n 9: Open a Week Folder? \n')
		return userInput

	# 1: Create a new Folder? (SKU\'s is done.)
	def createTheFolder(self):				
		CreateNewFolder(week=True, tvc=True, file_id=True)
		print('Done. Now you\'re ready to prepare and upload TVC to Drive (Step 2).')

	# 2: Prepare for EAN and upload TVC-list to Drive? (SKU\'s done. Upload EAN to TVC)
	def prepareForEAN(self):
		PrepareForEAN(week=True, tvc=True)
		print('Done. You can now upload the TVC file to Drive')
	
	# 3: Update Stock and send to Pavo and Friends? (List is back from TVC)
	def createChecklistToWePack(self):
		CreateChecklist(week=True, tvc=True, file_id=True)
		print('Take info from the newly downloaded original file. Update stock from the mail sent by TVC')

	# 4: Update location and QTY (List is back from WePack)
	def updateLocationAndQty(self):
		UpdateLocationQty(week=True, tvc=False, file_id=True)
	
	# 5: Create Add. Image list	    
	def createAddImageList(self):
		AdditionalImage(week=True, tvc=False, file_id=False, add_img=True)
		print('Additional image list is created')
	
	# 5: Get list ready for import
	def readyToImport(self):
		ReadyToImport(week=True, tvc=False, file_id=True)
		print('Done. Remember to doublecheck the list. Is pricing correct? Is images in correct order? And then it\'s ready to import!')

	# 9: Open a Week Folder?
	def openWeekListFolder(self):
		shared = Shared()
		userInput = shared.userInput(week=True)
		weekNumber = userInput[0]
		shared.openFolder(targetDirectory = WEEKLIST_DIR + weekNumber)
	
if __name__ == '__main__':
	Main()