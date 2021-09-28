import os
import xlrd

class ReadXls:
	def __init__(self, weekNumber, filename, fieldnames):
		self.weekNumber = weekNumber
		self.filename = filename
		self.fieldnames = fieldnames
		self.readFile()

	def readFile(self):
		filepath = os.getcwd() + '/' + self.weekNumber + '/' + self.filename		
		workbook = xlrd.open_workbook(filepath)
		sheet = workbook.sheet_by_index(0)
		# Create Dict from list, zip(key, values)
		dictOfValues = { field : [] for field in self.fieldnames }	


		# Loop through given fields
		for fieldname in self.fieldnames:
			for row in range(sheet.nrows):
				for col in range(sheet.ncols):
					# If cell value is fieldname
					if sheet.cell_value(row, col) == fieldname:
						# Append to Dictionary
						dictOfValues[fieldname] = sheet.col_values(col, row)

		# return
		return dictOfValues