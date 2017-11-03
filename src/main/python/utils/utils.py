import platform
import os
class Utils():
   
    @staticmethod
    def getPlatform():
        ostype = platform.system()
        return ostype

    @staticmethod
    def GetFileSize(fullName):
        fileSize = os.path.getsize(fullName)
        return fileSize

    @staticmethod
    def GetFilePath(fullName):
        filePath = os.path.abspath(fullName)
        return filePath
