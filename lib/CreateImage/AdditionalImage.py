from config.definitions import ROOT_DIR, WEEKLIST_DIR
from lib.Shared import Shared
from lib.CreateFiles.CreateXlsx import CreateXlsx

from pandas_ods_reader import read_ods

class AdditionalImage:    
    def __init__(self, week:bool, tvc:bool, file_id:bool, add_img:bool):            
        userInput = self.userInput(week, tvc, file_id, add_img)      
        filepath = self.downloadListFromDrive(week = userInput[0], add_img = userInput[1])
        dataDict = self.readOds(filepath = filepath)
        images = self.consolidateField(dataDict = dataDict)
        filename = self.createXls(values = images, week = userInput[0])        
        self.moveFile(filename = filename, week = userInput[0])
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
        return filepath
    
    def readOds(self, filepath:str) -> dict:
        base_path = filepath
        sheet_index = 1
        # Reading ods
        dataFrame = read_ods(base_path , sheet_index)
        # convert to dict
        dataDict = dataFrame.to_dict()
        # remove info we don\'t need
        remove_keys = ['##CPI', 'disabled']
        for key in remove_keys:
            dataDict.pop(key)
        
        return dataDict
    
    def consolidateField(self, dataDict:dict) -> dict:
        # Creating a list with all the skus
        skus = []        
        for headers in dataDict:
            if headers.lower() == 'sku':
                for sku in dataDict[headers]:
                    skus.append(dataDict[headers][sku])                    
        
        # Removing duplicates from skus[], and make them to dict keys
        images = dict.fromkeys(skus)
        # Giving a list as value
        for sku in images:
            images[sku] = list()

        # Appending Images
        for headers in dataDict:
            if headers.lower() == 'image_url':
                # Looping trough each image_url
                for image in dataDict[headers]:
                    # looping through each sku
                    for sku in images.keys():
                        # image_url without -X.jpg. If that matches sku
                        if dataDict[headers][image].rsplit('-', 1)[0] == sku:
                            # Append to dict
                            images[sku].append(dataDict[headers][image])
        # Return
        return images

    def createXls(self, values:dict, week:str) -> str:
        filename = week + '-Gallery.xlsx'         
        filepath = ROOT_DIR + '/' + week + '/' + filename
        create = CreateXlsx()
        create.createAdditionalImages(filepath = filepath, fieldnames = ['SKU', 'Gallery'], values = values)
        return filename
    
    def moveFile(self, filename:str, week:str) -> None:
        shared = Shared()
        currentPath = ROOT_DIR + '/' + week + '/' + filename        
        newPath = WEEKLIST_DIR + week + '/Shopify/Img/' + filename    
        shared.moveFile(week = week, currentPath = currentPath, newPath = newPath)
    
    # Open folder in Finder
    def openFolder(self, week:str) -> None:        
        shared = Shared()
        shared.openFolder(targetDirectory = WEEKLIST_DIR + week)             