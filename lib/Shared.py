from lib.Drive.GoogleDrive import GoogleDrive
from lib.CreateNewFolder.ReadXls import ReadXls
from lib.CreateNewFolder.CreateXls import CreateXls
from lib.CreateNewFolder.CreateFolder import CreateFolder

from config.definitions import ROOT_DIR, WEEKLIST_DIR

import webbrowser
import os
import shutil
from subprocess import call

class Shared:
    def userInput(self, week: bool=False, tvc: bool=False, file_id: bool=False) -> list:        
        userInput = []
        if week == True:
            weekNumber = input("Week number?: ")
            userInput.append(str(weekNumber))
        
        if tvc == True:
            tvcNo = input("Enter the TVC no?: ")
            userInput.append(str(tvcNo))
        
        if file_id == True:
            file_id = input("Enter the file id to download: ")
            userInput.append(str(file_id))

        # TESTING FILES    
        # userInput.append('302')        
        # userInput.append('E21050300001')
        # userInput.append('1Kolw1q-mCAGzXv_92v0xgKc8cAsnpPiO')

        # userInput[0] = '002'        
        # userInput[1] = 'E21050300001'
        # userInput[2] = '1Kolw1q-mCAGzXv_92v0xgKc8cAsnpPiO'
        return userInput        

    def openCM(self):
        url = 'https://docs.google.com/spreadsheets/d/1TWCdd-HPYJQWlRxknG2EhR1ky2MD1tVl7VSxG1R8hJk/edit#gid=0'
        webbrowser.open(url, new=0)    

    # Download list from google Drive
    def downloadNewestChecklist(self, week, file_id) -> str:
        # download the file from Google Drive
        googleDrive = GoogleDrive()
        # Creates token so our user can access/use Google APIs
        serviceToken = googleDrive.token()        
        # Download the file
        filename = googleDrive.downloadFile(serviceToken, week, file_id)                                
        return filename            
    
    # Moves a week folder from this folder, to local week list folder
    def moveFile(self, week:str, currentPath:str, newPath:str):        
        # Move the downloaded file to local weekfolder  (Current path, NewPath)
        shutil.move(currentPath, newPath)
        # delete devWeek
        shutil.rmtree(ROOT_DIR + '/' + week)
    
    def createAdminFile(self, week, orgFilepath):        
        xls = ReadXls()
        orgFileFieldnames = xls.getFieldnames(orgFilepath)
        orgFileValues = xls.getValues(orgFilepath, orgFileFieldnames)
        # Creates new Admin File and Folder
        createFolder = CreateFolder(path = week + '/Admin')
        path = createFolder.folder()
        filename = week + '-Admin-Upload.xls'
                
        # # Values we need as headers form the admin file
        adminDict = {'SKU' : '', 'Supplier' : '', 'Supplier SKU': '', 'EAN_new' : '', 'Name (en-GB)' : '', 'Price (en-GB)' : '', 'Final Price (en-GB)' : '', 'Price (de-DE)' : '', 'Final Price (de-DE)' : '', 'Price (nl-NL)' : '', 'Final Price (nl-NL)' : '', 'Price (fi-FI)' : '', 'Final Price (fi-FI)' : '', 'Price (da-DK)' : '', 'Final Price (da-DK)': '', 'Price (nb-NO)' : '', 'Final Price (nb-NO)' : '', 'Price (sv-SE)' : '', 'Final Price (sv-SE)' : '', 'Description (en-GB)' : '', 'Image' : '', 'Model' : '', 'List' : '', 'Gallery' : ''}

        # Loop through the original file, and the admin file
        for orgField in orgFileValues:
            for key in adminDict.keys():
                # If original file has the same key/fieldname as in adminDict, (case insensetive)
                if orgField.lower() == key.lower():
                    # insert value from org. file into adminDict
                    adminDict[key] = orgFileValues[orgField]
        
        # Create the admin Excel File 
        CreateXls(path = path + filename, fieldnames = list(adminDict.keys()), columns = adminDict)  
    
    # Open folder in Finder
    def openFolder(self, targetDirectory:str):        
        targetDirectory = targetDirectory
        call(["open", targetDirectory])
