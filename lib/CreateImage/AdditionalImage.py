from config.const import ROOT_DIR, WEEKLIST_DIR
from lib.Shared import Shared
from lib.ReadFiles.ReadOds import ReadOds
from lib.CreateImage.Magento.Magento import Magento
from lib.CreateImage.Shopify.Shopify import Shopify


class AdditionalImage:    
    def __init__(self, week:bool, tvc:bool, file_id:bool, add_img:bool):            
        userInput = self.userInput(week, tvc, file_id, add_img)      
        filepath = self.downloadListFromDrive(week = userInput[0], add_img = userInput[1])
        dataDict = self.readOds(filepath = filepath)

        filepaths = []
        filepaths.append(self.createMagentoFile(dataDict=dataDict, week = userInput[0]))
        filepaths.append(self.createShopifyFile(dataDict=dataDict, week = userInput[0]))
   
        self.moveFile(filepaths = filepaths, week = userInput[0])
        self.openFolder(week = userInput[0])

    # For users input
    def userInput(self, week:bool, tvc:bool, file_id:bool, add_img:bool) -> list:
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id, add_img)              
        return userInput

    def downloadListFromDrive(self, week:str, add_img:str) -> str:
        shared = Shared()
        filename = shared.downloadListFromDrive(week = week, file_id = add_img)        
        filepath = ROOT_DIR + '/' + week + '/' + filename
        # filepath = ROOT_DIR + '/' + week + '/' + 'ADDITIONAL_week_import_list-354.ods'
        return filepath
    
    def readOds(self, filepath:str) -> dict:
        readOds = ReadOds()
        dataDict = readOds.valuesToDict(filepath = filepath, sheet_index=1)

        # remove info we don\'t need
        remove_keys = ['##CPI', 'disabled']
        for key in remove_keys:
            dataDict.pop(key)        
        return dataDict
    
    def createMagentoFile(self, dataDict:dict, week:str) -> str:
        magento = Magento()
        filepath = magento.createAdditionalImageFile(dataDict = dataDict, week = week)
        return filepath
    
    def createShopifyFile(self, dataDict:dict, week:str) -> str:
        shopify = Shopify()
        images = shopify.consolidateField(dataDict = dataDict)
        filepath = shopify.createXls(values = images, week = week)
        return filepath     
    
    def moveFile(self, filepaths:list, week:str) -> None:
        shared = Shared()
        shared.moveFileList(filepaths = filepaths, week = week)
    
    # Open folder in Finder
    def openFolder(self, week:str) -> None:        
        shared = Shared()
        shared.openFolder(targetDirectory = WEEKLIST_DIR + week)             