from lib.Shared import Shared
from lib.ReadFiles.ReadXls import ReadXls
from lib.Import.Shopify.Struct import Struct
from lib.Import.Shopify.Ongoing import Ongoing
from config.const import ROOT_DIR, WEEKLIST_DIR
import shutil

class ReadyToImport:
    def __init__(self, week:bool, tvc:bool, file_id:bool, shippingNo:bool):
        userInput = self.userInput(week, tvc, file_id, shippingNo)                           
        orgFile = self.downloadNewestChecklist(week = userInput[0], file_id = userInput[1])        
        orgValues = self.createAdminDictFromDrive(orgFilepath = orgFile)

        # A list of file names we will move later into weekList folder        
        filenames = []
        # Struct
        filenames.append(self.createStructImport(orgValues = orgValues, week = userInput[0]))
        # Ongoing
        filenames.append(self.createOngoingImport(orgValues = orgValues, week = userInput[0]))

        # Move Files
        self.moveFile(week = userInput[0], filenames = filenames)
        self.openFolder(week = userInput[0])

    # For users input
    def userInput(self, week:bool, tvc:bool, file_id:bool, shippingNo:bool) -> list:                
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id, shippingNo)    
        return userInput

    # Downloads the newest list from GDrive 
    def downloadNewestChecklist(self, week:str, file_id:str) -> str:
        # download the file from Google Drive
        shared = Shared()
        filename = shared.downloadListFromDrive(week = week, file_id = file_id)
        filepath = ROOT_DIR + '/' + week + '/' + filename
        #
        return filepath

    def createAdminDictFromDrive(self, orgFilepath:str) -> dict:
        xls = ReadXls()
        orgFileFieldnames = xls.getFieldnames(orgFilepath)
        adminDict = xls.getValues(orgFilepath, orgFileFieldnames)
        return adminDict

    # Create Struct    
    def createStructImport(self, orgValues:str, week:str) -> str:
        struct = Struct() 
        adminValues = struct.createPrices(adminValues = orgValues)
        # adminValues = orgValues
        filename = struct.createAdminFromDict(adminValues = adminValues, week = week)
        return filename
    
    # Create Ongoing
    def createOngoingImport(self, orgValues:list, week:str) -> str:
        ongoing = Ongoing()        
        filename = ongoing.createOngoingFromDict(adminValues = orgValues, week = week)        
        return filename

    # Moves a week folder from this folder, to local week list folder
    def moveFile(self, week:str, filenames:list):             
        for filename in filenames:
            # paths
            currentPath = ROOT_DIR + '/' + week + '/' + filename
            newPath = WEEKLIST_DIR + week + '/Shopify/Admin/' + filename
            # Move files
            shutil.move(currentPath, newPath)        
        # remove devFolder
        shutil.rmtree(ROOT_DIR + '/' + week)

    # Open folder in Finder
    def openFolder(self, week:str):        
        shared = Shared()
        shared.openFolder(targetDirectory = WEEKLIST_DIR + week)