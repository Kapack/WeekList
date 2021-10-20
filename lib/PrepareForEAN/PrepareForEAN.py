import webbrowser
from subprocess import call

from lib.Drive.GoogleDrive import GoogleDrive
from lib.Shared import Shared

class PrepareForEAN:
    def __init__(self):
        self.openCM()
        userInput = self.userInput()                
        self.openEANSheet()
        self.openGoogleDrive()        
        self.openLocalTVCFile(userInput)
    
    def userInput(self):        
        shared = Shared()
        userInput = shared.userInput()        
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
        targetDirectory = "/Users/marketing/Documents/Lux-Case/Import Products/Week Lists/" + weekNumber + '/TVC/' + weekNumber + '-' + tvcNo + '-TVC.xls'
        call(["open", targetDirectory])