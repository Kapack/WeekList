import csv
import pandas as pd
import os

class CreateCsv:
	def __init__(self, path, filename, fields=[], rows={}):
		self.path = path
		if not os.path.exists(self.path):
			os.makedirs(self.path)

		self.filename = filename
		self.fields = fields
		self.rows = rows		
		
	# Save file with single row
	def saveSimpleFile(self) -> None:		
		path = self.path		
		filename = self.filename
		fields = self.fields
		rows = self.rows

		with open(path + filename, 'w') as file:
			fieldnames = fields
			writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
			writer.writeheader()			
			writer.writerow(rows)
	
	def saveFile(self) -> bool:
		path = self.path		
		filename = self.filename		
		rows = self.rows
	
		df = pd.DataFrame(rows)
		df.to_csv(path + filename, index=False, sep=';')
