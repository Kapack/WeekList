from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.CreateBasicFolder.Magento.MagentoBaseFolderFile import MagentoBaseFolderFile
from lib.CreateBasicFolder.Shopify.ShopifyBaseFolderFile import ShopifyBaseFolderFile
from lib.Drive.GoogleDrive import GoogleDrive
from lib.Shared import Shared
from config.definitions import ROOT_DIR, WEEKLIST_DIR
# import os
import shutil

class CreateBasicFolder:
    def __init__(self, week:bool, tvc:bool, file_id:bool):
        userInput = self.userInput(week, tvc, file_id)
        week = userInput[0]        
        tvcNo = userInput[1]
        file_id = userInput[2]                

        self.parentFolder(week = week)
        orgFilePath = self.googleDrive(week = week, file_id = file_id)        
        self.magentoFolder(week = week, orgFile = orgFilePath, tvcNo = tvcNo)
        self.shopifyFolder(week = week)        
        self.moveParentFolder(week = week)
        self.openFolder(week = week)
    
    def userInput(self, week:bool, tvc:bool, file_id:bool):    
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id)
        return userInput                
    
    # Creates the "root" directory (week)
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
        return filepath

    # Create Magento Template Files
    def magentoFolder(self, week:str, orgFile:str, tvcNo:str) -> str:
        print('Creates Magento folder...')
        magentoFolder = MagentoBaseFolderFile(path = ROOT_DIR + '/' + week + '/Magento', week = week, orgFile = orgFile, tvcNo = tvcNo)
        basePath = magentoFolder.createBaseFolder()
        return basePath

    # Create Shopify Template Files    
    def shopifyFolder(self, week:str) -> str:
        print('Creates Shopify folder...')        
        shopifyFolder = ShopifyBaseFolderFile(path = ROOT_DIR + '/' + week + '/Shopify', week = week)        
        basePath = shopifyFolder.createBaseFolder()
        return basePath

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