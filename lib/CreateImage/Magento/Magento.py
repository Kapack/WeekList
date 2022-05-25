import os
from config.const import ROOT_DIR
from lib.CreateBasicFolder.CreateFiles.CreateCsv import CreateCsv

class Magento:
    def createAdditionalImageFile(self, dataDict:dict, week:str) -> str:        
        path = ROOT_DIR + '/' + week + '/Magento/Img/'        
        if not os.path.exists(path):
            os.makedirs(path)
        filename = week + '_ADDITIONAL_week_import_list.csv'
        # filepath = path + filename

        # Rename keys
        dataDict['sku'] = dataDict.pop('Sku')
        dataDict['additional_images'] = dataDict.pop('image_url')
        
        # Add Keys with val
        dataDict['label'] = ''
        dataDict['position'] = ''
        dataDict['disabled'] = 0
        dataDict['product_type'] = 'simple'

        createCsv = CreateCsv(path=path, filename=filename, rows=dataDict)
        createCsv.saveFile()
        
        return '/Magento/Img/' + filename