from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.CreateBasicFolder.Stock.StockFolder import StockFolder
from lib.CreateBasicFolder.Magento.MagentoBaseFolderFile import MagentoBaseFolderFile
from lib.CreateBasicFolder.Shopify.ShopifyBaseFolderFile import ShopifyBaseFolderFile
from lib.Drive.GoogleDrive import GoogleDrive
from lib.Shared import Shared
from config.const import ROOT_DIR, WEEKLIST_DIR
# import os
import shutil

class CreateBasicFolder:
    def __init__(self, week:bool, tvc:bool, file_id:bool, add_img:bool, shippingNo:bool):
        """
        Creates all the folders we need

        :param bool week: Should there be a userinput for week
        :param bool tvc: Should we ask user for tvc
        :param bool file_id: Should we ask user for file_id
        :param bool file_id: Should we ask user for shippingNo        
        """

        userInput = self.userInput(week, tvc, file_id, add_img, shippingNo)
        week = userInput[0]        
        tvcNo = userInput[1]        
        file_id = userInput[2]        
        shippingNo = userInput[3]

        self.parentFolder(week = week)
        orgFilePath = self.googleDrive(week = week, file_id = file_id)        
        self.stockFolder(week = week, orgFile = orgFilePath, tvcNo = tvcNo, shippingNo = shippingNo)
        self.magentoFolder(week = week, orgFile = orgFilePath, tvcNo = tvcNo)
        self.shopifyFolder(week = week)        
        self.moveParentFolder(week = week)
        self.openFolder(week = week)
    
    def userInput(self, week:bool, tvc:bool, file_id:bool, add_img:bool, shippingNo:bool):    
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id, add_img, shippingNo)
        return userInput                
    
    # Creates the week_number directory
    def parentFolder(self, week:str) -> str:
        print('Creates Parent folder...')
        createFolder = CreateFolder(path = ROOT_DIR + '/' + week + '/')
        path = createFolder.folder()
        return path
    
    # Download WeekList from Google Drive
    def googleDrive(self, week:str, file_id:str) -> str:
        googleDrive = GoogleDrive()
        # Creates token so our user can access/use Google APIs
        serviceToken = googleDrive.token()
        # Download the file
        orgFile = googleDrive.downloadFile(serviceToken, week, file_id)        
        filepath = ROOT_DIR + '/' + week + '/' + orgFile
        
        # filepath = ROOT_DIR + '/' + week + '/368-LIST-V03_Skus_Tested.xls'

        return filepath
    
    # Creates stock folders (TVC and WePack)
    def stockFolder(self, week:str, orgFile:str, tvcNo:str, shippingNo:str) -> None:
        print('Creates Stock Folder')
        StockFolder(path = ROOT_DIR + '/' + week + '/Stock', week = week, orgFile = orgFile, tvcNo = tvcNo, shippingNo = shippingNo)

    # Create Magento Template Files
    def magentoFolder(self, week:str, orgFile:str, tvcNo:str) -> None:
        print('Creates Magento folder...')
        MagentoBaseFolderFile(path = ROOT_DIR + '/' + week + '/Magento', week = week, orgFile = orgFile, tvcNo = tvcNo)
                
    # Create Shopify Template Files    
    def shopifyFolder(self, week:str) -> None:
        print('Creates Shopify folder...')        
        ShopifyBaseFolderFile(path = ROOT_DIR + '/' + week + '/Shopify', week = week)

    # Move the folder to Import Products/Week Lists
    def moveParentFolder(self, week:str) -> None:
        print('Moves to directory...')		
        original = ROOT_DIR + '/' + week
        target = WEEKLIST_DIR
        shutil.move(original,target)

    # Open folder in Finder
    def openFolder(self, week:str) -> None:
        shared = Shared()
        shared.openFolder(targetDirectory = WEEKLIST_DIR + week)