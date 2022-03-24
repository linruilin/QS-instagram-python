# encoding=UTF-8
from config import INPUT_DATA
from app.module.statusCode import get_statusCode
import csv


def get_inputData():  # 解析inputDate.csv 返回数据
    try:
        file_inputData = csv.reader(open(INPUT_DATA, "r"))
        inputLen = 0
        inputData = []

        for data in file_inputData:
            if inputLen != 0:
                inputData.append(data[0])
            inputLen += 1

        res = get_statusCode("2000")
        res["data"] = inputData
        return res
    except Exception as e:
        res = get_statusCode("4001")
        res["error"] = e
        return res
