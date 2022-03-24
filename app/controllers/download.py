import os
import requests


def download(path, url, name="", types=".jpg"):  # 数据下载
    if name == "":
        data_path = path + url.split("/")[-1]
    else:
        data_path = path + name + types

    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(data_path):
            r = requests.get(url)
            r.raise_for_status()
            # 使用with语句可以不用自己手动关闭已经打开的文件流
            with open(data_path, "wb") as f:  # 开始写文件，wb代表写二进制文件
                f.write(r.content)
            print(data_path + " 下载成功")
        else:
            print("文件已存在")
    except BaseException as e:
        print("Errors: ", e)
