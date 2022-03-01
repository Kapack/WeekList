from lib.Shared import Shared
from lib.Drive.GoogleDrive import GoogleDrive
from config.definitions import ROOT_DIR, WEEKLIST_DIR

from subprocess import call

class UpdateLocationQty:
    def __init__(self, week:bool, tvc:bool, file_id:bool):                        
        self.openCM()
        self.openChecklistFolder()        
        userInput = self.userInput(week, tvc, file_id)
        self.downloadNewestChecklist(userInput[0], userInput[1])
        self.openLocalDownloadFolder()        
        self.openLocalWepackFolder(userInput[0])

    # Open in CM in Browser
    def openCM(self):
        shared = Shared()
        shared.openCM()
    
    # Open Google Drive
    def openChecklistFolder(self):
        googleDrive = GoogleDrive()
        googleDrive.openChecklistFolder()

    # For users input
    def userInput(self, week:bool, tvc:bool, file_id:bool):
        shared = Shared()
        userInput = shared.userInput(week, tvc, file_id)      
        return userInput
    
    def downloadNewestChecklist(self, week:str, file_id:str):
        # download the file from Google Drive
        shared = Shared()
        filename = shared.downloadListFromDrive(week, file_id)
        shared.moveFile(week = week, currentPath = ROOT_DIR + '/' + week + '/' + filename, newPath = WEEKLIST_DIR + week)

    # Local Download folder
    def openLocalDownloadFolder(self):
        targetDirectory = "/Users/marketing/Downloads/"
        call(["open", targetDirectory])
    
    def openLocalWepackFolder(self, weekNumber):
        targetDirectory = WEEKLIST_DIR + weekNumber + '/WePack/'
        call(["open", targetDirectory])