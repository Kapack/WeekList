from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.CreateBasicFolder.CreateFiles.CreateCsv import CreateCsv
from lib.CreateBasicFolder.ReadXls import ReadXls
from lib.CreateBasicFolder.CreateFiles.CreateXls import CreateXls

class MagentoBaseFolderFile:
    def __init__(self, path:str, week:str, orgFile:str, tvcNo:str):
        self.path = path
        self.week = week
        self.orgFile = orgFile
        self.tvcNo = tvcNo

        adminPath = self.adminFolder(path = path)   
        self.adminFile(path = adminPath, week = week)
        imgFolder = self.imgFolder(path)
        self.imgFile(path = imgFolder, week = week)
        pricesFolder = self.pricesFolder(path = path)
        self.pricesFile(path = pricesFolder, week = week)
        translateFolder = self.translateFolder(path)
        self.translateFile(path = translateFolder, week = week)
        TVCFolder = self.TVCFolder(path = path)
        self.TVCFile(path = TVCFolder, week = week, orgFile = orgFile, tvcNo = tvcNo)
        wePackFolder = self.wePackFolder(path)
        self.wePackFile(path = wePackFolder, week = week, tvcNo = tvcNo)
        self.wePackLocationFolder(path)
    
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
        fieldnames = ['supplier_sku', 'ean', 'sku', 'name', 'price', 'qty', 'description', 'image', 'small_image', 'thumbnail', 'visibility', 'attribute_set_code', 'product_type', 'product_websites', 'weight', 'product_online', 'news_from_date', 'options_container', 'stock_is_in_stock']
        rows = {'supplier_sku' : '', 'ean': '', 'sku': '', 'price': '', 'qty': '',  'description' : '', 'image' : '', 'small_image': '', 'thumbnail': '', 'visibility' : 'Catalog, Search', 'attribute_set_code': 'Migration_Default', 'product_type' : 'simple', 'product_websites' : 'base,se,dk,no,fi,nl,be,uk,ie,de,ch,at', 'weight': '1', 'product_online': '1', 'news_from_date': 'MM/DD/YY', 'options_container': 'Block after Info Column', 'stock_is_in_stock' : '=IF(F2=0;"No";"Yes")'}
        CreateCsv(path = path, fileName = '1-OnlyAdd-Upload-' + week + '-admin.csv', fields = fieldnames, rows = rows)

        # Create Attributes file
        fieldnames = ['sku', 'manufacturer', 'model', 'color', 'product_type']
        rows = {'sku' : '', 'manufacturer' : '', 'model': '', 'color': '', 'product_type': 'simple'}
        CreateCsv(path = path, fileName = week + '-admin-attributes.csv', fields = fieldnames, rows = rows)

        # Create Category and Location file
        fieldnames = ['sku', 'categories', 'location', 'product_type']
        rows = {'sku': '', 'categories': '', 'location':'', 'product_type': 'simple'}
        CreateCsv(path = path, fileName = week + '-admin-cat_loc.csv', fields = fieldnames, rows = rows)

    def imgFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Img/')
        path = createFolder.folder()
        return path
    
    # Creates additional image file
    def imgFile(self, path:str, week:str) -> None:        
        fieldnames = ['sku', 'additional_images', 'label', 'position', 'disabled', 'product_type']
        rows = {'sku' : 'LCP-01-24-A0001', 'additional_images': 'LCP-01-24-A0001-A.jpg', 'label': '', 'position': '', 'disabled': '0', 'product_type' : 'simple'}
        CreateCsv(path, week + '-add-img.csv', fieldnames, rows)

    def pricesFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Prices/')
        path = createFolder.folder()
        return path
    
    # Create prices files
    def pricesFile(self, path:str, week:str) -> None:        
        fieldnames = ['sku', 'price', 'store_view_code', 'product_websites', 'product_type']
        rows = {'sku' : 'SKU', 'price': '99', 'store_view_code': 'dk, se, no', 'product_websites': 'dk, se, no', 'product_type': 'simple'}
        CreateCsv(path, week + '-CO-prices.csv', fieldnames, rows)
    
    def translateFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/Translate/')
        path = createFolder.folder()
        return path

    def translateFile(self, path:str, week:str) -> None:
        fieldnames = ['sku', 'name', 'description', 'url_key', 'store_view_code', 'product_type']
        rows = {'sku' : '', 'name': '', 'description': '', 'url_key': '', 'store_view_code': '', 'product_type': 'simple'}
        CreateCsv(path, week + '-CO-Translation.csv', fieldnames, rows)        
    
    def TVCFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/TVC/')
        path = createFolder.folder()
        return path

    def TVCFile(self, path:str, week:str, orgFile:str, tvcNo:str) -> None:
        # Which fields we want from org file
        fieldnames = ['P/N', 'ean', 'sku', 'Q\'ty']

        # Getting values from xls
        xls = ReadXls()
        fileColumns = xls.getValues(orgFile, fieldnames)

        # Changing columns according to TVC requirements
        fileColumns['SKUS'] = fileColumns.pop('sku')
        fieldnames[2] = 'SKUS'

        # Create Xls. 
        CreateXls(path + week + '-' + tvcNo + '-TVC.xls', fieldnames, fileColumns)
    
    def wePackFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/WePack/')
        path = createFolder.folder()
        return path
    
    def wePackFile(self, path:str, week:str, tvcNo:str) -> None:
        fieldnames = ['P/N', 'Image', 'sku', 'name', 'manufacturer', 'model', 'Description', 'Q\'ty']
        CreateXls(path + week + '-' + tvcNo + '-Checklist.xls', fieldnames)
    
    def wePackLocationFolder(self, path:str) -> str:
        createFolder = CreateFolder(path = path + '/WePack/Location/')
        path = createFolder.folder()
        return path