from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.CreateBasicFolder.CreateFiles.CreateCsv import CreateCsv
from config.const import MAGENTO_ADMIN_FIELDNAMES, MAGENTO_ATTRIBUTES_FIELDNAMES, MAGENTO_CATLOC_FIELDNAMES

class MagentoBaseFolderFile:
    def __init__(self, path:str, week:str, orgFile:str, tvcNo:str):
        self.path = path
        self.week = week
        self.orgFile = orgFile
        self.tvcNo = tvcNo
        
        self.createBaseFolder()
        adminPath = self.adminFolder(path = path)   
        self.adminFile(path = adminPath, week = week)
        imgFolder = self.imgFolder(path)
        self.imgFile(path = imgFolder, week = week)
        pricesFolder = self.pricesFolder(path = path)
        self.pricesFile(path = pricesFolder, week = week)
        translateFolder = self.translateFolder(path)
        self.translateFile(path = translateFolder, week = week)
    
    def createBaseFolder(self) -> str:
        path = self.path
        createFolder = CreateFolder(path = path)
        path = createFolder.folder()
        return path
    
    def adminFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Admin/')
        path = createFolder.folder()    
        return path

    def adminFile(self, path:str, week:str) -> None:
        fieldnames = MAGENTO_ADMIN_FIELDNAMES
        rows = {'supplier_sku' : '', 'ean': '', 'sku': '', 'price': '', 'qty': '',  'description' : '', 'image' : '', 'small_image': '', 'thumbnail': '', 'visibility' : 'Catalog, Search', 'attribute_set_code': 'Migration_Default', 'product_type' : 'simple', 'product_websites' : 'base,se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'weight': '1', 'product_online': '1', 'news_from_date': 'MM/DD/YY', 'options_container': 'Block after Info Column', 'stock_is_in_stock' : '=IF(F2=0;"No";"Yes")'}
        createCsv = CreateCsv(path = path, filename = '1-OnlyAdd-Upload-' + week + '-admin.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()

        # Create Attributes file
        fieldnames = MAGENTO_ATTRIBUTES_FIELDNAMES
        rows = {'sku' : '', 'manufacturer' : '', 'model': '', 'color': '', 'product_type': 'simple'}
        createCsv = CreateCsv(path = path, filename = week + '-admin-attributes.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()

        # Create Category and Location file
        fieldnames = MAGENTO_CATLOC_FIELDNAMES
        rows = {'sku': '', 'categories': '', 'location':'', 'product_type': 'simple'}
        createCsv = CreateCsv(path = path, filename = week + '-admin-cat_loc.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()

    def imgFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Img/')
        path = createFolder.folder()
        return path
    
    # Creates additional image file
    def imgFile(self, path:str, week:str) -> None:        
        fieldnames = ['sku', 'additional_images', 'label', 'position', 'disabled', 'product_type']
        rows = {'sku' : 'LCP-01-24-A0001', 'additional_images': 'LCP-01-24-A0001-A.jpg', 'label': '', 'position': '', 'disabled': '0', 'product_type' : 'simple'}
        createCsv = CreateCsv(path = path, filename = week + '-add-img.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()

    def pricesFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Prices/')
        path = createFolder.folder()
        return path
    
    # Create prices files
    def pricesFile(self, path:str, week:str) -> None:        
        fieldnames = ['sku', 'price', 'store_view_code', 'product_websites', 'product_type']
        rows = {'sku' : 'SKU', 'price': '99', 'store_view_code': 'dk, se, no', 'product_websites': 'dk, se, no', 'product_type': 'simple'}
        createCsv = CreateCsv(path = path, filename = week + '-CO-prices.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()
    
    def translateFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Translate/')
        path = createFolder.folder()
        return path

    def translateFile(self, path:str, week:str) -> None:
        fieldnames = ['sku', 'name', 'description', 'url_key', 'store_view_code', 'product_type']
        rows = {'sku' : '', 'name': '', 'description': '', 'url_key': '', 'store_view_code': '', 'product_type': 'simple'}
        createCsv = CreateCsv(path = path, filename = week + '-CO-Translation.csv', fields = fieldnames, rows = rows)
        createCsv.saveSimpleFile()