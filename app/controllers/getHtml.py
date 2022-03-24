# encoding=UTF-8
import requests
from app.module.statusCode import get_statusCode

def getHtml(url):  # 读取url地址获取网页文件
    try:
        resHtml = requests.get(
            url, timeout=10)
        res = get_statusCode("2000")
        res["data"] = resHtml
        return res
    except Exception as e:
        res = get_statusCode("4002")
        res["error"] = e
        return res