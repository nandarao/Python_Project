import configparser

config = configparser.RawConfigParser()
config.read(".\\Configration\\config.ini", encoding=None)

class ReadConfigFile:
    
    @staticmethod
    def getDataFilePath():
        filePath = config.get("Excel file Path","excel_file_path")
        return filePath
            
    @staticmethod
    def getBrowserType():
        BrowserType =config.get("Select Browser Type","BrowserType")
        return BrowserType    
    
    @staticmethod
    def getApplicationURL():
        URL =config.get("Reusable values", "url")
        return URL
    
    @staticmethod
    def getApplicationUserID():
        UserID =config.get("Reusable values", "userID")
        return UserID
    
    @staticmethod
    def getApplicationPassword():
        Password =config.get("Reusable values", "password")
        return Password