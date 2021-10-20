import webbrowser

class Shared:
    def userInput(self):        
        weekNumber = raw_input("Week number?: ")        
        tvcNo = raw_input("Enter the TVC no?: ")
        file_id = raw_input("Enter the file id to download: ")

        # TESTING FILES 
        # weekNumber = '001'
        # file_id = '1IpyptKbfEvDK2z6hVdOxvImuJzryE5jZ'
        # tvcNo = 'E20031500001'
        return [weekNumber, tvcNo, file_id]

    def openCM(self):
        url = 'https://docs.google.com/spreadsheets/d/1TWCdd-HPYJQWlRxknG2EhR1ky2MD1tVl7VSxG1R8hJk/edit#gid=0'
        webbrowser.open(url, new=0)