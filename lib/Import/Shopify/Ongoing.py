import xlwt
from config.const import ROOT_DIR, ONGOING_FIELDNAMES

class Ongoing:
    
    def createOngoingFromDict(self, adminValues:dict, week:str):
        # Creating our work book 
        woorkbook = xlwt.Workbook()
        sheet = woorkbook.add_sheet('Sheet1')    
        
        i = 0
        for field in ONGOING_FIELDNAMES:
            sheet.write(0, i, field)

            if field.lower() in adminValues.keys():                                
                # Remove first from adminValues / Key
                adminValues[field.lower()].pop(0)
                # Write Values
                ii = 1            
                for value in adminValues[field.lower()]:
                    sheet.write(ii, i, value)
                    ii += 1
            
            if field.lower() == 'article number':
                adminValues['sku'].pop(0)
                ii = 1
                for sku in adminValues['sku']:
                    sheet.write(ii, i, sku)                    
                    ii += 1
                            
            if field.lower() == 'barcode':
                adminValues['ean'].pop(0)
                ii = 1
                for ean in adminValues['ean']:
                    sheet.write(ii, i, ean)                    
                    ii += 1
            
            if field.lower() == 'supplier article no.':
                adminValues['P/N'].pop(0)
                ii = 1
                for pn in adminValues['P/N']:
                    sheet.write(ii, i, pn)                    
                    ii += 1

            if field.lower() == 'number of items':
                adminValues['Q\'ty'].pop(0)
                ii = 1
                for qty in adminValues['Q\'ty']:
                    sheet.write(ii, i, qty)                    
                    ii += 1
            
            i += 1

        # # # Save workboook
        filename = week + '-Admin-Ongoing-Upload.xls'
        woorkbook.save(ROOT_DIR + '/' + week + '/' + filename)
        return filename