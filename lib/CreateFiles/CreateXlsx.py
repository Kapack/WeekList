import xlsxwriter

class CreateXlsx:
    # Creates a file with only headers 
    def templateFile(self, path:str, fieldnames:list) -> None:						
        # Creating our work book 
        workbook = xlsxwriter.Workbook(path)
        # Add Sheet
        worksheet = workbook.add_worksheet()
        # Writing Header
        row = 0
        column = 0
        for field in fieldnames:
            worksheet.write(row, column, field)
            column += 1					
        workbook.close()
    
    def createAdditionalImages(self, filepath:str, fieldnames:list, values:dict) -> None:
        # Creating workbook
        workbook = xlsxwriter.Workbook(filepath)
        # Add Sheet
        worksheet = workbook.add_worksheet()

        # Writing Header
        row = 0
        columnIteration = 0
        
        for field in fieldnames:
            # Writing Header
            worksheet.write(row, columnIteration, field)
            columnIteration += 1	

        # # Write Values
        i = 1    
        for sku in values:
            images = str(', '.join(values[sku]))
            # Write skus             
            worksheet.write(i, 0, sku)          
            # Write images
            worksheet.write(i, 1, images)            
            i += 1
        
        workbook.close()
