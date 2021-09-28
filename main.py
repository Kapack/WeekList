import os
import shutil
from subprocess import call

from lib.CreateFolder import CreateFolder
from lib.CreateCsv import CreateCsv
from lib.CreateXls import CreateXls
from lib.ReadXls import ReadXls
from lib.Drive.GoogleDrive import GoogleDrive

class Main:
	def __init__(self):
		userInput = self.userInput()
		weekNumber = userInput[0]
		file_id = userInput[1]
		tvcNo = userInput[2]

		self.parentFolder(weekNumber)
		orgFilename = self.googleDrive(weekNumber, file_id)
		self.adminFolder(weekNumber)
		self.imgFolder(weekNumber)
		self.pricesFolder(weekNumber)
		self.localizationFolder(weekNumber)
		# orgFilename = '240-LIST-V05.xls'
		self.tvcFolder(weekNumber, orgFilename, tvcNo)
		self.wePackFolder(weekNumber, tvcNo)
		self.moveParentFolder(weekNumber)
		self.openFolder(weekNumber)

	def userInput(self):
		# weekNumber = raw_input("Week number?: ")
		# file_id = raw_input("Enter the file id to download: ")
		# tvcNo = raw_input("Enter the TVC no?: ")

		weekNumber = '001-TEST'
		file_id = '1IpyptKbfEvDK2z6hVdOxvImuJzryE5jZ'
		tvcNo = 'E20031500001'

		return [weekNumber, file_id, tvcNo]

	# Creates the "root" directory
	def parentFolder(self, weekNumber):
		createFolder = CreateFolder(weekNumber)
		createFolder.folder()

	# Download WeekList from Google Drive
	def googleDrive(self, weekNumber, file_id):
		googleDrive = GoogleDrive(weekNumber, file_id)
		# Creates token so our user can access/use Google APIs
		serviceToken = googleDrive.token()
		# Download the file
		orgFile = googleDrive.downloadFile(serviceToken)	
		return orgFile

	# Admin
	def adminFolder(self, weekNumber):
		createFolder = CreateFolder(weekNumber + '/Admin')
		path = createFolder.folder()
		
		# Create Main File
		fieldnames = ['supplier_sku', 'ean', 'sku', 'name', 'price', 'qty', 'description', 'image', 'small_image', 'thumbnail', 'visibility', 'attribute_set_code', 'product_type', 'product_websites', 'weight', 'product_online', 'news_from_date', 'options_container', 'stock_is_in_stock']
		rows = {'supplier_sku' : '', 'ean': '', 'sku': '', 'price': '', 'qty': '',  'description' : '', 'image' : '', 'small_image': '', 'thumbnail': '', 'visibility' : 'Catalog, Search', 'attribute_set_code': 'Migration_Default', 'product_type' : 'simple', 'product_websites' : 'base,se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'weight': '1', 'product_online': '1', 'news_from_date': 'MM/DD/YY', 'options_container': 'Block after Info Column', 'stock_is_in_stock' : '=IF(F2=0;"No";"Yes")'}
		createCsv = CreateCsv(path, '1-OnlyAdd-Upload-' + weekNumber + '-admin.csv', fieldnames, rows)

		# Create Attributes file
		fieldnames = ['sku', 'manufacturer', 'model', 'color', 'product_type']
		rows = {'sku' : '', 'manufacturer' : '', 'model': '', 'color': '', 'product_type': 'simple'}
		createCsv = CreateCsv(path, 'Upload-' + weekNumber + '-admin-attributes.csv', fieldnames, rows)

		# Create Category and Location file
		fieldnames = ['sku', 'categories', 'location', 'product_type']
		rows = {'sku': '', 'categories': '', 'location':'', 'product_type': 'simple'}
		createCsv = CreateCsv(path, 'Upload-' + weekNumber + '-admin-cat_loc.csv', fieldnames, rows)

	# Images
	def imgFolder(self, weekNumber):
		createFolder = CreateFolder(weekNumber + '/IMG')
		path = createFolder.folder()
		# Creates additional image file
		fieldnames = ['sku', 'additional_images', 'label', 'position', 'disabled', 'product_type']
		rows = {'sku' : 'LCP-01-24-A0001', 'additional_images': 'LCP-01-24-A0001-A.jpg', 'label': '', 'position': '', 'disabled': '0', 'product_type' : 'simple'}
		createCsv = CreateCsv(path, 'Upload-' + weekNumber + '-admin-attributes.csv', fieldnames, rows)

	# Prices
	def pricesFolder(self, weekNumber):
		createFolder = CreateFolder(weekNumber + '/Prices')
		path = createFolder.folder()
		# Create prices files
		fieldnames = ['sku', 'price', 'store_view_code', 'product_websites', 'product_type']
		rows = {'sku' : 'SKU', 'price': '99', 'store_view_code': 'dk, se, no', 'product_websites': 'dk, se, no', 'product_type': 'simple'}
		createCsv = CreateCsv(path, 'Upload-' + weekNumber + '-CO-prices.csv', fieldnames, rows)

	# Languages
	def localizationFolder(self, weekNumber):
		createFolder = CreateFolder(weekNumber + '/Translate')
		path = createFolder.folder()
		#
		fieldnames = ['sku', 'name', 'description', 'url_key', 'store_view_code', 'product_websites', 'product_type']
		rows = {'sku': '', 'name': '', 'description': '', 'url_key':'', 'store_view_code': 'se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'product_websites': 'se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'product_type': 'simple'}
		createCsv = CreateCsv(path, 'Upload-' + weekNumber + '-CO-content.csv', fieldnames, rows)

	# TVC Folder
	def tvcFolder(self, weekNumber, orgFilename, tvcNo):
		createFolder = CreateFolder(weekNumber + '/TVC')
		path = createFolder.folder()
		
		# Which fields we want from org file
		fieldnames = ['P/N', 'ean', 'sku', 'Q\'ty']

		# Getting values from xls
		readXls = ReadXls(weekNumber, orgFilename, fieldnames)	
		fileColumns = readXls.readFile()

		# Changing columns according to TVC requirements
		fileColumns['SKUS'] = fileColumns.pop('sku')
		fieldnames[2] = 'SKUS'

		# Create Xls. TVC requires sku spelled differently
		createXls = CreateXls(path + weekNumber + '-' + tvcNo + '-TVC.xls', fieldnames, fileColumns)

	# WePack Folder 
	def wePackFolder(self, weekNumber, tvcNo):
		createFolder = CreateFolder(weekNumber + '/WePack')
		path = createFolder.folder()		
		#
		fieldnames = ['P/N', 'Image', 'sku', 'name', 'manufacturer', 'model', 'Description', 'Q\'ty']
		createXls = CreateXls(path + weekNumber + '-' + tvcNo + '-Checklist.xls', fieldnames)

	# Move the folder to Import Products/Week Lists
	def moveParentFolder(self, weekNumber):		
		original = os.getcwd() + '/' + weekNumber
		target = '/Users/marketing/Documents/Lux-Case/Import Products/Week Lists'		
		shutil.move(original,target)

	# Open folder in Finder
	def openFolder(self, weekNumber):
		targetDirectory = "/Users/marketing/Documents/Lux-Case/Import Products/Week Lists/" + weekNumber
		call(["open", targetDirectory])

if __name__ == '__main__':
	Main()