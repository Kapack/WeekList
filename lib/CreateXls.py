import xlwt

class CreateXls:
	def __init__(self, path, fieldnames):
		self.path = path
		self.fieldnames = fieldnames
		# Calling the saveFile method
		self.saveFile()


	def saveFile(self):
		path = self.path
		fieldnames = self.fieldnames

		wb = xlwt.Workbook()
		ws = wb.add_sheet('Sheet1')

		# Create FieldNames
		i = 0
		for field in fieldnames:
			ws.write(0, i, field)
			i += 1

		wb.save(path)

