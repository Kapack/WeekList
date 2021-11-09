# import os
import xlrd
# from config.definitions import ROOT_DIR


class ReadXls:

	def getFieldnames(self, filepath) -> list:				
		# Open File
		workbook = xlrd.open_workbook(filepath)
		# Getting all Sheet names
		sheet_names = workbook.sheet_names()
		# The first sheet
		firstSheet = workbook.sheet_by_name(sheet_names[0])
		# Getting the row from the first sheet	
		firstRow = firstSheet.row_values(0)				
		return firstRow
	
	def getValues(self, filepath, fieldnames) -> dict:				
		# Read file
		workbook = xlrd.open_workbook(filepath)
		# Getting the first sheet
		sheet = workbook.sheet_by_index(0)
		# Create Dict from list, zip(key, values)			
		dictOfValues = { field : [] for field in fieldnames }		
		# Loop through given fields
		for fieldname in fieldnames:			
			for row in range(sheet.nrows):				
				for col in range(sheet.ncols):
					# If cell value is fieldname
					if sheet.cell_value(row, col) == fieldname:
						# Append to Dictionary
						dictOfValues[fieldname] = sheet.col_values(col, row)
		# Return the dict
		return dictOfValues

		


	# Magento

	# def __init__(self, weekNumber, filename, fieldnames):
	# 	self.weekNumber = weekNumber
	# 	self.filename = filename
	# 	self.fieldnames = fieldnames
	# 	self.readFile()

	# def readFile(self):
	# 	# filepath = os.getcwd() + '/' + self.weekNumber + '/' + self.filename		
	# 	filepath = ROOT_DIR + '/' + self.weekNumber + '/' + self.filename		
	# 	workbook = xlrd.open_workbook(filepath)
	# 	sheet = workbook.sheet_by_index(0)
	# 	# Create Dict from list, zip(key, values)
	# 	dictOfValues = { field : [] for field in self.fieldnames }	

	# 	# Loop through given fields
	# 	for fieldname in self.fieldnames:
	# 		for row in range(sheet.nrows):
	# 			for col in range(sheet.ncols):
	# 				# If cell value is fieldname
	# 				if sheet.cell_value(row, col) == fieldname:
	# 					# Append to Dictionary
	# 					dictOfValues[fieldname] = sheet.col_values(col, row)

	# 	# return
	# 	return dictOfValues