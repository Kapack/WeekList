from lib.CreateFiles.CreateXlsx import CreateXlsx
from config.const import ROOT_DIR
import os

class Shopify:
    def consolidateField(self, dataDict:dict) -> dict:
        # Creating a list with all the skus
        skus = []        
        for headers in dataDict:
            if headers.lower() == 'sku':
                for sku in dataDict[headers]:
                    skus.append(dataDict[headers][sku])                    
        
        # Removing duplicates from skus[], and make them to dict keys
        images = dict.fromkeys(skus)
        # Giving a list as value
        for sku in images:
            images[sku] = list()

        # Appending Images
        for headers in dataDict:
            if headers.lower() == 'image_url':
                # Looping trough each image_url
                for image in dataDict[headers]:
                    # looping through each sku
                    for sku in images.keys():
                        # image_url without -X.jpg. If that matches sku
                        if dataDict[headers][image].rsplit('-', 1)[0] == sku:
                            # Append to dict
                            images[sku].append(dataDict[headers][image])
        # Return
        return images

    def createXls(self, values:dict, week:str) -> str:
        filename = week + '-Gallery.xlsx'     
        path = ROOT_DIR + '/' + week + '/Shopify/Img/'        
        if not os.path.exists(path):
            os.makedirs(path)            
        filepath = path + filename

        create = CreateXlsx()
        create.createAdditionalImages(filepath = filepath, fieldnames = ['SKU', 'Gallery'], values = values)
        return '/Shopify/Img/' + filename