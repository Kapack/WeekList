from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.CreateBasicFolder.CreateFiles.CreateXlsx import CreateXlsx
from config.definitions import STRUCT_FIELDNAMES

class ShopifyBaseFolderFile:
    def __init__(self, path:str, week:str):
        self.path = path
        adminPath = self.createAdminFolder(path = path)
        self.createAdminFile(path = adminPath, week = week)
        transPath = self.createTranslationFolder(path = path)
        self.createTranslationFile(path = transPath, week = week)
        imgPath = self.createImgFolder(path = path)
        self.createImgFile(path = imgPath, week = week)

    def createBaseFolder(self) -> str:
        path = self.path
        createFolder = CreateFolder(path = path)
        path = createFolder.folder()
        return path
    
    def createAdminFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Admin/')
        path = createFolder.folder()    
        return path
    
    def createAdminFile(self, path:str, week:str) -> None:
        createXlsx = CreateXlsx()
        filename = week + '-Struct-Admin.xlsx'        
        fieldnames = STRUCT_FIELDNAMES
        # Creates the xlsx file
        createXlsx.templateFile(path = path + filename, fieldnames = fieldnames)
    
    def createTranslationFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Translation/')
        path = createFolder.folder()    
        return path
        
    def createTranslationFile(self, path:str, week:str) -> None:
        createXlsx = CreateXlsx()
        filename = week + '-Translation.xlsx'        
        fieldnames = ['SKU', 'Name (en-GB)', 'Description (en-GB)', 'Name (da-DK)', 'Description (da-DK)', 'Name (sv-SE)', 'Description (sv-SE)',	'Name (nb-NO)', 'Description (nb-NO)', 'Name (fi-FI)', 'Description (fi-FI)', 'Name (nl-NL)', 'Description (nl-NL)', 'Name (de-DE)', 'Description (de-DE)']                
        createXlsx.templateFile(path = path + filename, fieldnames = fieldnames)

    def createImgFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Img/')
        path = createFolder.folder()    
        return path

    def createImgFile(self, path:str, week:str) -> None:
        createXlsx = CreateXlsx()
        filename = week + '-Gallery.xlsx'        
        fieldnames = ['SKU', 'Gallery']                
        createXlsx.templateFile(path = path + filename, fieldnames = fieldnames)        