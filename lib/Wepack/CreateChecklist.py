from subprocess import call

from lib.Shared import Shared
from lib.Drive.GoogleDrive import GoogleDrive
from definitions import WEEKLIST_DIR

class CreateChecklist:
    def __init__(self, week:bool, tvc:bool, file_id:bool):        
        self.openGoogleDrive()
        self.openCM()
        userInput = self.userInput(week, tvc, file_id)
        self.openLocalChecklistFile(userInput[0], userInput[1])
        self.openLocalFolder(userInput[0])
    
    def userInput(self, week:bool, tvc:bool, file_id:bool):
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id)        
        return userInput
    
    # Open in CM in Browser
    def openCM(self):
        shared = Shared()
        shared.openCM()
                
    # Open Google Drive
    def openGoogleDrive(self):
        googleDrive = GoogleDrive()
        googleDrive.openChecklistFolder()
    
    # download the file from Google Drive
    def downloadNewestChecklist(self, week, file_id):
        shared = Shared()
        shared.downloadNewestChecklist(week, file_id)

    # Open Local TVC File
    def openLocalChecklistFile(self, week, tvcNo): 
        targetDirectory = WEEKLIST_DIR + week + '/WePack/' + week + '-' + tvcNo + '-Checklist.xls'
        call(["open", targetDirectory])

    # Open Local Folder    
    def openLocalFolder(self, week):
        targetDirectory = WEEKLIST_DIR + week
        call(["open", targetDirectory])   