from lib.CreateBasicFolder.CreateFolder import CreateFolder
from lib.ReadFiles.ReadXls import ReadXls
from lib.CreateBasicFolder.CreateFiles.CreateXls import CreateXls

class StockFolder:
    def __init__(self, path:str, week:str, orgFile:str, tvcNo:str, shippingNo:str) -> None:
        """
        Creates all Stock folders and their files

        :param str path: The initial path folders are placed. (Later it gets moved into a final folder; lib.CreateBasicFolder.moveParentFolder)
        :param str week: Which weeklist number we are working with - Used for file naming
        :param str orgFile: The path for the file downloaded from Google Drive
        :param str tvcNo: The TVC Number - Used for file naming
        :param str shippingNo: The Shipping number - Used for file naming
        """

        self.path = path
        self.week = week
        self.orgFile = orgFile
        self.tvcNo = tvcNo
        self.shippingNo = shippingNo
        
        TVCFolder = self.TVCFolder(path = path)
        self.TVCFile(path = TVCFolder, week = week, orgFile = orgFile, tvcNo = tvcNo)
        wePackFolder = self.wePackFolder(path)
        self.wePackFile(path = wePackFolder, week = week, tvcNo = tvcNo, shippingNo = shippingNo)
        self.wePackLocationFolder(path)

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
    
    def wePackFile(self, path:str, week:str, tvcNo:str, shippingNo:str) -> None:
        fieldnames = ['P/N', 'Image', 'sku', 'name', 'manufacturer', 'model', 'Description', 'Q\'ty']    
        CreateXls(path + week + '-' + tvcNo + '-(' + shippingNo + ')-' + 'Checklist.xls', fieldnames)
    
    def wePackLocationFolder(self, path:str) -> None:
        createFolder = CreateFolder(path = path + '/WePack/Location/')
        path = createFolder.folder() 