from lib.Drive.GoogleDrive import GoogleDrive
from config.const import ROOT_DIR, WEEKLIST_DIR
import webbrowser
import shutil
from subprocess import call

class Shared:
    def userInput(self, week: bool=False, tvc: bool=False, file_id: bool=False, add_img: bool=False, shippingNo: bool=False) -> list:
        userInput = []

        if week == True:
            weekNumber = input("Week number?: ")
            userInput.append(str(weekNumber))
        
        if tvc == True:
            tvcNo = input("Enter the TVC no?: ")
            userInput.append(str(tvcNo))        
        
        if file_id == True:
            file_id = input("Enter the checklist file id to download: ")            
            userInput.append(str(file_id))

        if add_img == True:
            add_img = input("Enter the add. image file id: ")
            userInput.append(str(add_img))
        
        if shippingNo == True:
            shippingNo = input("Enter the shipping no: ")
            userInput.append(str(shippingNo))
        

        # TESTING FILES    
        # userInput.append('900')
        # userInput.append('E21050300001')        
        # userInput.append('1Kolw1q-mCAGzXv_92v0xgKc8cAsnpPiO')
        # userInput.append('1WWT3M6B-CFi5JI3otIOwD5KhZGW2Z1bB')
        # userInput.append('SHIPPING')

        # userInput[0] = '302'        
        # # userInput[1] = 'E21050300001'        
        # # userInput[2] = '1Kolw1q-mCAGzXv_92v0xgKc8cAsnpPiO'
        # userInput[3] = '1WWT3M6B-CFi5JI3otIOwD5KhZGW2Z1bB'
        # # userInput[4] = 'Shipping'

        return userInput        

    def openCM(self):
        url = 'https://docs.google.com/spreadsheets/d/1TWCdd-HPYJQWlRxknG2EhR1ky2MD1tVl7VSxG1R8hJk/edit#gid=1984270103'
        webbrowser.open(url, new=0)    

    # Download list from google Drive
    def downloadListFromDrive(self, week, file_id) -> str:
        # download the file from Google Drive
        googleDrive = GoogleDrive()
        # Creates token so our user can access/use Google APIs
        serviceToken = googleDrive.token()        
        # Download the file
        filename = googleDrive.downloadFile(serviceToken, week, file_id)
        return filename            
    
    # Moves a week folder from this folder, to local week list folder
    def moveFile(self, week:str, currentPath:str, newPath:str) -> str:        
        # Move the downloaded file to local weekfolder  (Current path, NewPath)
        shutil.move(currentPath, newPath)
        # delete devWeek
        shutil.rmtree(ROOT_DIR + '/' + week)
        return newPath
    
    def moveFileList(self, filepaths:list, week:str):
        for filepath in filepaths:
            currentPath = ROOT_DIR + '/' + week + '/' + filepath
            newPath = WEEKLIST_DIR + week + filepath
            # Move files
            shutil.move(currentPath, newPath)        
        # remove devFolder
        shutil.rmtree(ROOT_DIR + '/' + week)

    # Open folder in Finder
    def openFolder(self, targetDirectory:str):        
        targetDirectory = targetDirectory
        call(["open", targetDirectory])
