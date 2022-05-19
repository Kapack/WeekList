from subprocess import call

from lib.Shared import Shared
from lib.Drive.GoogleDrive import GoogleDrive
from lib.ReadFiles.ReadXls import ReadXls
from config.definitions import ROOT_DIR, WEEKLIST_DIR

class CreateChecklist:
    def __init__(self, week:bool, tvc:bool, file_id:bool, add_img:bool, shippingNo:bool):        
        userInput = self.userInput(week, tvc, file_id, add_img, shippingNo)
        week = userInput[0]
        file_id = userInput[2]                
        self.openCM()
        self.openGoogleDrive()
        self.downloadNewestChecklist(week = week, file_id = file_id)        
        self.openLocalChecklistFile(userInput[0], userInput[1])
        self.openLocalFolder(userInput[0])
    
    def userInput(self, week:bool, tvc:bool, file_id:bool, add_img:bool, shippingNo:bool) -> list:
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id, add_img, shippingNo)        
        return userInput
    
    # Open in CM in Browser
    def openCM(self) -> None:
        shared = Shared()
        shared.openCM()
                
    # Open Google Drive
    def openGoogleDrive(self) -> None:
        googleDrive = GoogleDrive()
        googleDrive.openChecklistFolder()
    
    # download the file from Google Drive
    def downloadNewestChecklist(self, week:str, file_id:str) -> None:
        shared = Shared()
        filename = shared.downloadListFromDrive(week, file_id)        
        shared.moveFile(week = week, currentPath = ROOT_DIR + '/' + week + '/' + filename, newPath = WEEKLIST_DIR + week + '/' + filename)            

    # Open Local Checklist File
    def openLocalChecklistFile(self, week, tvcNo) -> None: 
        targetDirectory = WEEKLIST_DIR + week + '/WePack/' + week + '-' + tvcNo + '-Checklist.xls'
        call(["open", targetDirectory])

    # Open Local Folder    
    def openLocalFolder(self, week) -> None:
        targetDirectory = WEEKLIST_DIR + week
        call(["open", targetDirectory])   