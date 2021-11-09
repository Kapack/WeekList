from lib.Shared import Shared
from lib.CreateNewFolder.ReadXls import ReadXls
from lib.CreatePrice.CreatePrice import CreatePrice

from config.definitions import ROOT_DIR, WEEKLIST_DIR, ADMIN_FIELDNAMES
#
import xlwt
from subprocess import call

class ReadyToImport:
    def __init__(self, week:bool, tvc:bool, file_id:bool):
        userInput = self.userInput(week, tvc, file_id)        
        orgFile = self.downloadNewestChecklist(week = userInput[0], file_id = userInput[1])        
        # Create dict        
        orgValues = self.createAdminDictFromDrive(orgFilepath = orgFile)         
        #
        adminValues = self.createPrices(adminValues = orgValues[1])
        # Create Final
        filename = self.createAdminFromDict(adminValues = adminValues, week = userInput[0])        
        self.moveFile(week = userInput[0], filename = filename)
        self.openFolder(week = userInput[0])

    # For users input
    def userInput(self, week:bool, tvc:bool, file_id:bool) -> list:
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id)              
        return userInput

    # Downloads the newest list from GDrive 
    def downloadNewestChecklist(self, week:str, file_id:str) -> str:
        # download the file from Google Drive
        shared = Shared()
        filename = shared.downloadNewestChecklist(week = week, file_id = file_id)                
        filepath = ROOT_DIR + '/' + week + '/' + filename
        #        
        return filepath
    
    def createAdminDictFromDrive(self, orgFilepath:str) -> dict:
        xls = ReadXls()
        orgFileFieldnames = xls.getFieldnames(orgFilepath)        
        adminDict = xls.getValues(orgFilepath, orgFileFieldnames)
        return [orgFileFieldnames, adminDict]

    def createPrices(self, adminValues:dict) -> dict:
        createPrice = CreatePrice()
        adminValues = createPrice.prices(adminValues = adminValues)
        return adminValues
    
    # 
    def createAdminFromDict(self, adminValues:dict, week:str) -> str:           
        # Creating our work book 
        woorkbook = xlwt.Workbook()
        sheet = woorkbook.add_sheet('Sheet1')    
        
        i = 0
        for adminField in ADMIN_FIELDNAMES:            
            # Create Fieldnames
            sheet.write(0, i, adminField) 
            # If field in ADMIN_FIELDNAMES exists in adminValues.key
            
            if adminField in adminValues.keys():                
                # Remove first from adminValues
                adminValues[adminField].pop(0)
                # Write values
                ii = 1
                for value in adminValues[adminField]:                                        
                    sheet.write(ii, i, value)                
                    ii += 1

            i += 1
        # Save workboook
        filename = week + '-Admin-Upload.xls'
        woorkbook.save(ROOT_DIR + '/' + week + '/' + filename)
        return filename
    
    # Moves a week folder from this folder, to local week list folder
    def moveFile(self, week:str, filename:str):             
        shared = Shared()     
        # paths
        currentPath = ROOT_DIR + '/' + week + '/' + filename
        newPath = WEEKLIST_DIR + week + '/Admin/' + filename
        # move file
        shared.moveFile(week = week, currentPath = currentPath, newPath = newPath)

    # Open folder in Finder
    def openFolder(self, week:str):        
        shared = Shared()
        shared.openFolder(targetDirectory = WEEKLIST_DIR + week)