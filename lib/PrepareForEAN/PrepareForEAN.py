import webbrowser
from subprocess import call

from lib.Drive.GoogleDrive import GoogleDrive
from lib.Shared import Shared
from config.definitions import WEEKLIST_DIR

class PrepareForEAN:
    def __init__(self, week:bool, tvc:bool):
        self.openCM()
        userInput = self.userInput(week, tvc)                
        self.openEANSheet()
        self.openGoogleDrive()        
        self.openLocalTVCFile(userInput)
    
    def userInput(self, week:bool, tvc:bool):
        shared = Shared()
        userInput = shared.userInput(week, tvc)
        return userInput
    
    # Open in CM in Browser
    def openCM(self):        
        shared = Shared()
        shared.openCM()    
    
    # Open EAN Sheet
    def openEANSheet(self):
        url = 'https://docs.google.com/spreadsheets/d/1DZ9HERxsOikz8X48J2nrpeaKDO9xahI7zKiol8lJaZk/edit#gid=0'
        webbrowser.open(url, new=0)
    
    # Open Google Drive
    def openGoogleDrive(self):
        googleDrive = GoogleDrive()
        googleDrive.openChecklistFolder()

    # Open Local TVC File
    def openLocalTVCFile(self, userInput):                
        weekNumber = userInput[0]
        tvcNo = userInput[1]        
        targetDirectory = WEEKLIST_DIR + weekNumber + '/TVC/' + weekNumber + '-' + tvcNo + '-TVC.xls'
        call(["open", targetDirectory])