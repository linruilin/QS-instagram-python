import csv
import os
import time
from config import ROOT_DIR
from app.controllers.download import download

def csvData(csvData):
    try:
        data_path = ROOT_DIR+"/data/"
        path = ROOT_DIR + "/data/outData.csv"
        
        # filename = os.path.basename(csvData["fileImg"])
        csvText = []
        # print(csvData,"csvData")
        for i in csvData:
            fileImgDate = int(time.time()*1000000)
            download(data_path,i["fileImg"],str(fileImgDate))
            profilePictureDate = int(time.time()*1000000)
            download(data_path,i["profilePicture"],str(profilePictureDate))
            csvText.append([str(fileImgDate)+".jpg",str(profilePictureDate)+".jpg",i["profileName"],i["title"]])
        
        with open(path, 'w') as csvfile:
            
            spamwriter = csv.writer(csvfile,dialect='excel')
            # csv_head = ['fileImg', 'profilePicture', 'profileName', 'title']
            
            csv_head = ["good","bad"]
            spamwriter.writerow(csv_head)
            for x in csvText:
                spamwriter.writerow(x)
        
    except Exception as e:
        print("Errors: ", e)
    