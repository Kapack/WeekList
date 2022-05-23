from pandas_ods_reader import read_ods

class ReadOds:
    def valuesToDict(self, filepath:str, sheet_index:int) -> dict:
        base_path = filepath
        sheet_index = 1
        # Reading ods
        dataFrame = read_ods(base_path, sheet_index)
        # convert to dict
        dataDict = dataFrame.to_dict()

        return dataDict