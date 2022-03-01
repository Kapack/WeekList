import csv

class CreateCsv:
	def __init__(self, path, fileName, fields, rows={}):
		self.path = path
		self.fileName = fileName
		self.fields = fields
		self.rows = rows
		# Calling the save file method
		self.saveFile()

	def saveFile(self):
		path = self.path
		fileName = self.fileName
		fields = self.fields
		rows = self.rows
		
		with open(path + fileName, 'w') as file:
			fieldnames = fields
			writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
			writer.writeheader()
			writer.writerow(rows)
