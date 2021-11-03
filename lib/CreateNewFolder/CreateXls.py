import xlwt

class CreateXls:
	def __init__(self, path, fieldnames, columns=None):
		self.path = path
		self.fieldnames = fieldnames
		self.columns = columns
		# Calling the saveFile method
		self.saveFile()

	def saveFile(self):		
		path = self.path
		fieldnames = self.fieldnames
		columns = self.columns
		
		# Creating our work book 
		woorkbook = xlwt.Workbook()
		sheet = woorkbook.add_sheet('Sheet1')

		# If columns from orgFile has been added, create a file with values
		if columns != None:

			i = 0
			for field in columns:				
				# Write fieldname / header
				sheet.write(0, i, field)
						
				# Remove first field from columns so we don't have two headers
				if type(columns[field]) == list:
					columns[field].pop(0)				
					
				# Write cells values
				ii = 1
				for col in range(len(columns[field])):
					sheet.write(ii, i, columns[field][col])
					ii += 1				
				i += 1

		# Create a file with only fieldnames
		else:
			# Create FieldNames
			i = 0
			for field in fieldnames:
				sheet.write(0, i, field)
				i += 1

		woorkbook.save(path)

