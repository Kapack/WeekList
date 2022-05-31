from lib.Shared import Shared
from lib.CreateBasicFolder.CreateFiles.CreateCsv import CreateCsv
from config.const import ROOT_DIR, MAG_ADMIN_DIR
from datetime import date

class Magento:
    def __init__(self, week:str):
        self.shared = Shared()
        self.path = ROOT_DIR + '/' + week + MAG_ADMIN_DIR

    def createAdminFile(self, rows:dict, week:str) -> str:           
        # remove info we don\'t need
        remove_keys = ['Image', 'Cost', 'Material', 'manufacturer', 'Category Id', 'model', 'device_name']                
        rows = self.shared.rmKeyFromDict(remove_keys = remove_keys, orgDict = rows)
        
        # Rename keys
        rows['price'] = rows.pop('Price')
        rows['description'] = rows.pop('Description')
        rows['supplier_sku'] = rows.pop('P/N')        
        rows['qty'] = rows.pop('Q\'ty')
        
        # Adding new keys with values
        rows['visibility'] = 'Catalog, Search'
        rows['attribute_set_code'] = 'Migration_Default'
        rows['product_type'] = 'simple'
        rows['product_websites'] = 'base,se,dk,no,fi,nl,be,uk,ie,de,ch,at'
        rows['weight'] = '1'
        rows['product_online'] = '1'        
        rows['news_from_date'] = date.today().strftime("%m/%d/%y")
        rows['options_container'] = 'Block after Info Column'        
        rows['stock_is_in_stock'] = '=IF(F2=0;"No";"Yes")'        

        # Converting datatypes
        rows['qty'] = map(int, rows['qty'])
        rows['price'] = map(float, rows['price'])
                    
        # Create Csv
        filename = '1-OnlyAdd-Upload-' + week + '-admin.csv'
        createCsv = CreateCsv(path = self.path, filename = filename, rows = rows)
        createCsv.saveFile()

        return MAG_ADMIN_DIR + filename
    
    def createAttrFile(self, rows:dict, week:str) -> str:                
        # remove info we don\'t need
        remove_keys = ['P/N', 'name', 'Image', 'ean', 'device_name', 'Category Id', 'Description', 'Material', 'Price', 'Cost', 'Q\'ty', 'image', 'small_image', 'thumbnail'] 
        rows = self.shared.rmKeyFromDict(remove_keys = remove_keys, orgDict = rows)
        
        # Adding Key
        rows['product_type'] = 'simple'
        filename = week + '-admin-attributes.csv'
        createCsv = CreateCsv(path = self.path, filename = filename, rows = rows)
        createCsv.saveFile()        
        return MAG_ADMIN_DIR + filename

    def createCatLocFile(self, rows:dict, week:str) -> str:                
        # remove info we don\'t need
        remove_keys = remove_keys = ['P/N', 'name', 'manufacturer', 'model', 'Image', 'ean', 'device_name', 'Description', 'Material', 'Price', 'Cost', 'Q\'ty', 'image', 'small_image', 'thumbnail'] 
        rows = self.shared.rmKeyFromDict(remove_keys = remove_keys, orgDict = rows)

        # Rename keys
        rows['categories'] = rows.pop('Category Id')
        
        # Convert float to int
        i = 0
        for cat in rows['categories']:
            if isinstance(cat, float):
                rows['categories'][i] = int(rows['categories'][i])
            i += 1
        
        # Convert to string
        rows['categories'] = map(str, rows['categories'])
        
        # Adding Keys
        rows['location'] = ''
        rows['product_type'] = 'simple'        

        # Create the file
        filename = week + '-admin-cat_loc.csv'    
        createCsv = CreateCsv(path = self.path, filename = filename, rows = rows)
        createCsv.saveFile()
        return MAG_ADMIN_DIR + filename