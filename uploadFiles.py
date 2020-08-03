import dropbox as dp
import os
# Vahin Sharma
class TransferData:
    def __init__(self, aToken):
        self.aToken = aToken
    def uploadFolder(self, fFrom, fTo):
        print("\nUploading, please wait\n")
        for file in os.listdir(fFrom):
            f = open(fFrom+"/"+file, "rb")
            dp.Dropbox(self.aToken).files_upload(f.read(), "/"+fTo+"/"+os.path.basename(fFrom)+"/"+file)
        print("Success! Your folder has been uploaded!")

TransferData(input("Please enter your access token: ")).uploadFolder(input("Please enter the path of the folder to be uploaded: "), input("Please enter the folder to upload the folder to: "))
