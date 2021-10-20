from subprocess import call

from lib.Shared import Shared
from lib.Drive.GoogleDrive import GoogleDrive

class Wepack:
    def __init__(self):
        pass
        # self.userInput()
    
    def userInput(self):
        shared = Shared()
        userInput = shared.userInput()        
        return userInput

    def createChecklist(self):                
        self.openCM()
        self.openGoogleDrive()
        userInput = self.userInput()
        self.openLocalChecklistFile(userInput)
    
    # Open in CM in Browser
    def openCM(self):
        shared = Shared()
        shared.openCM()
                
    # Open Google Drive
    def openGoogleDrive(self):
        googleDrive = GoogleDrive()
        googleDrive.openChecklistFolder()

    # Open Local TVC File
    def openLocalChecklistFile(self, userInput):                
        weekNumber = userInput[0]
        tvcNo = userInput[1]     
        targetDirectory = "/Users/marketing/Documents/Lux-Case/Import Products/Week Lists/" + weekNumber + '/WePack/' + weekNumber + '-' + tvcNo + '-Checklist.xls'
        call(["open", targetDirectory])    