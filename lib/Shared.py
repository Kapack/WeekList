from lib.Drive.GoogleDrive import GoogleDrive
from definitions import ROOT_DIR, WEEKLIST_DIR

import webbrowser
import os
import shutil

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
        # userInput[0] = '302'        
        # userInput[1] = 'E21050300001'
        # userInput[1] = '1Kolw1q-mCAGzXv_92v0xgKc8cAsnpPiO'
        return userInput        

    def openCM(self):
        url = 'https://docs.google.com/spreadsheets/d/1TWCdd-HPYJQWlRxknG2EhR1ky2MD1tVl7VSxG1R8hJk/edit#gid=0'
        webbrowser.open(url, new=0)    

    def downloadNewestChecklist(self, week, file_id):
        # download the file from Google Drive
        googleDrive = GoogleDrive()
        serviceToken = googleDrive.token()        
        filename = googleDrive.downloadFile(serviceToken, week, file_id)        
        # Move the downloaded file to local weekfolder  (Current path, NewPath)
        shutil.move(ROOT_DIR + '/' + week + '/' + filename, WEEKLIST_DIR + week + '/' + filename)            
        # delete devWeek
        os.rmdir(ROOT_DIR + '/' + week)