# from lib.Shared import Shared
from lib.CreateNewFolder.ReadXls import ReadXls
from lib.CreatePrice.CreatePrice import CreatePrice

from config.definitions import ROOT_DIR, STRUCT_FIELDNAMES
#
import xlwt
from subprocess import call

class Struct:

    def createPrices(self, adminValues:dict) -> dict:
        createPrice = CreatePrice()
        adminValues = createPrice.prices(adminValues = adminValues)
        return adminValues
    
    # 
    def createAdminFromDict(self, adminValues:dict, week:str) -> str:           
        # Creating our work book 
        woorkbook = xlwt.Workbook()
        sheet = woorkbook.add_sheet('Sheet1')    
        
        i = 0
        for adminField in STRUCT_FIELDNAMES:            
            # Create Fieldnames
            sheet.write(0, i, adminField) 
            # If field in ADMIN_FIELDNAMES exists in adminValues.key
            
            if adminField in adminValues.keys():                
                # Remove first from adminValues
                adminValues[adminField].pop(0)
                # Write values
                ii = 1
                for value in adminValues[adminField]:                                        
                    sheet.write(ii, i, value)                
                    ii += 1

            i += 1
        # Save workboook
        filename = week + '-Admin-Struct-Upload.xls'
        woorkbook.save(ROOT_DIR + '/' + week + '/' + filename)
        return filename