# encoding=UTF-8
import os
import pdb
import urllib

import json

from app.controllers.inputData import get_inputData
from app.controllers.getHtml import getHtml
from app.controllers.getData import getData
from app.controllers.csvData import csvData


def main():  # 应用入口
    try:
        inputDataList = get_inputData()
        print(inputDataList)
        if inputDataList["code"] == "2000":
            csvDatas = []
            for url in inputDataList["data"]:
                resHtml = getHtml(url)
                if resHtml["code"] == "2000":
                    resData = getData(resHtml["data"])
                    if resData["code"] == "2000":
                        csvDatas.append(resData["data"])
                    else:
                        print("getData Error:", resData["msg"], url)
                else:
                    print("getHtml Error:", resHtml["msg"], url)
            resCsv = csvData(csvDatas)
            print(resCsv)
        else:
            print("get_inputData Error:", inputDataList["msg"])
    except Exception as e:
        print(e, "main error")
