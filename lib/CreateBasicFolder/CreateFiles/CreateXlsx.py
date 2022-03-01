import xlsxwriter

class CreateXlsx:
	# Creates a file with only headers 
	def templateFile(self, path:str, fieldnames:list):						
		# Creating our work book 
		workbook = xlsxwriter.Workbook(path)
		# Add Sheet
		worksheet = workbook.add_worksheet()
		# Writing Header
		row = 0
		column = 0
		for field in fieldnames:
			worksheet.write(row, column, field)
			column += 1					
		workbook.close()