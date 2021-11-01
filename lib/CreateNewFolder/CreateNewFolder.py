# from WeekList.definitions import ROOT_DIR
from lib.CreateNewFolder.CreateFolder import CreateFolder
from lib.Drive.GoogleDrive import GoogleDrive
from lib.CreateNewFolder.CreateCsv import CreateCsv
from lib.CreateNewFolder.CreateXls import CreateXls
from lib.CreateNewFolder.ReadXls import ReadXls
from lib.Shared import Shared
from config.definitions import ROOT_DIR, WEEKLIST_DIR
#
# import os
import shutil
from subprocess import call

class CreateNewFolder:
    def __init__(self, week:bool, tvc:bool, file_id:bool):
        userInput = self.userInput(week, tvc, file_id)
        weekNumber = userInput[0]        
        tvcNo = userInput[1]
        file_id = userInput[2]
        
        self.parentFolder(weekNumber)
        orgFilename = self.googleDrive(weekNumber, file_id)
        self.adminFolder(weekNumber)
        self.imgFolder(weekNumber)
        self.pricesFolder(weekNumber)
        self.localizationFolder(weekNumber)        
        self.tvcFolder(weekNumber, orgFilename, tvcNo)
        self.wePackFolder(weekNumber, tvcNo)
        self.moveParentFolder(weekNumber)
        self.openFolder(weekNumber)
    
    def userInput(self, week:bool, tvc:bool, file_id:bool):    
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id)
        return userInput                
    
    # Creates the "root" directory
    def parentFolder(self, weekNumber):
        print('Creates Parent folder...')
        createFolder = CreateFolder(weekNumber)
        createFolder.folder()
    
    # Download WeekList from Google Drive
    def googleDrive(self, weekNumber, file_id):
        googleDrive = GoogleDrive()
        # Creates token so our user can access/use Google APIs
        serviceToken = googleDrive.token()
        # Download the file
        orgFile = googleDrive.downloadFile(serviceToken, weekNumber, file_id)
        return orgFile

    # Admin
    def adminFolder(self, weekNumber):
        print('Creates Admin folder...')
        createFolder = CreateFolder(weekNumber + '/Admin')
        path = createFolder.folder()

        # Create Main File
        fieldnames = ['supplier_sku', 'ean', 'sku', 'name', 'price', 'qty', 'description', 'image', 'small_image', 'thumbnail', 'visibility', 'attribute_set_code', 'product_type', 'product_websites', 'weight', 'product_online', 'news_from_date', 'options_container', 'stock_is_in_stock']
        rows = {'supplier_sku' : '', 'ean': '', 'sku': '', 'price': '', 'qty': '',  'description' : '', 'image' : '', 'small_image': '', 'thumbnail': '', 'visibility' : 'Catalog, Search', 'attribute_set_code': 'Migration_Default', 'product_type' : 'simple', 'product_websites' : 'base,se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'weight': '1', 'product_online': '1', 'news_from_date': 'MM/DD/YY', 'options_container': 'Block after Info Column', 'stock_is_in_stock' : '=IF(F2=0;"No";"Yes")'}
        CreateCsv(path, '1-OnlyAdd-Upload-' + weekNumber + '-admin.csv', fieldnames, rows)

        # Create Attributes file
        fieldnames = ['sku', 'manufacturer', 'model', 'color', 'product_type']
        rows = {'sku' : '', 'manufacturer' : '', 'model': '', 'color': '', 'product_type': 'simple'}
        CreateCsv(path, 'Upload-' + weekNumber + '-admin-attributes.csv', fieldnames, rows)

        # Create Category and Location file
        fieldnames = ['sku', 'categories', 'location', 'product_type']
        rows = {'sku': '', 'categories': '', 'location':'', 'product_type': 'simple'}
        CreateCsv(path, 'Upload-' + weekNumber + '-admin-cat_loc.csv', fieldnames, rows)

    # Images
    def imgFolder(self, weekNumber):
        print('Creates Img folder...')
        createFolder = CreateFolder(weekNumber + '/IMG')
        path = createFolder.folder()
        # Creates additional image file
        fieldnames = ['sku', 'additional_images', 'label', 'position', 'disabled', 'product_type']
        rows = {'sku' : 'LCP-01-24-A0001', 'additional_images': 'LCP-01-24-A0001-A.jpg', 'label': '', 'position': '', 'disabled': '0', 'product_type' : 'simple'}
        CreateCsv(path, 'Upload-' + weekNumber + '-admin-attributes.csv', fieldnames, rows)

    # Prices
    def pricesFolder(self, weekNumber):
        print('Creates Prices folder...')
        createFolder = CreateFolder(weekNumber + '/Prices')
        path = createFolder.folder()
        # Create prices files
        fieldnames = ['sku', 'price', 'store_view_code', 'product_websites', 'product_type']
        rows = {'sku' : 'SKU', 'price': '99', 'store_view_code': 'dk, se, no', 'product_websites': 'dk, se, no', 'product_type': 'simple'}
        CreateCsv(path, 'Upload-' + weekNumber + '-CO-prices.csv', fieldnames, rows)

    # Languages
    def localizationFolder(self, weekNumber):
        print('Creates Localization folder...')
        createFolder = CreateFolder(weekNumber + '/Translate')
        path = createFolder.folder()
        #
        fieldnames = ['sku', 'name', 'description', 'url_key', 'store_view_code', 'product_websites', 'product_type']
        rows = {'sku': '', 'name': '', 'description': '', 'url_key':'', 'store_view_code': 'se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'product_websites': 'se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'product_type': 'simple'}
        CreateCsv(path, 'Upload-' + weekNumber + '-CO-content.csv', fieldnames, rows)

    # TVC Folder
    def tvcFolder(self, weekNumber, orgFilename, tvcNo):
        print('Creates TVC folder...')
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
        CreateXls(path + weekNumber + '-' + tvcNo + '-TVC.xls', fieldnames, fileColumns)

    # WePack Folder 
    def wePackFolder(self, weekNumber, tvcNo):
        print('Creates WePack folder...')
        createFolder = CreateFolder(weekNumber + '/WePack')
        path = createFolder.folder()		
        #
        fieldnames = ['P/N', 'Image', 'sku', 'name', 'manufacturer', 'model', 'Description', 'Q\'ty']
        CreateXls(path + weekNumber + '-' + tvcNo + '-Checklist.xls', fieldnames)

    # Move the folder to Import Products/Week Lists
    def moveParentFolder(self, weekNumber):
        print('Moves to directory...')		
        original = ROOT_DIR + '/' + weekNumber
        target = WEEKLIST_DIR
        shutil.move(original,target)

    # Open folder in Finder
    def openFolder(self, weekNumber):
        targetDirectory = WEEKLIST_DIR + weekNumber
        call(["open", targetDirectory])