# coding=UTF-8
import os
import platform

# 应用名称
APP_NAME = "QS-instagram-python"

STSTEM_TYPE = platform.system()

# 根目录
ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__))

# 输入数据文件地址
INPUT_DATA = ROOT_DIR + "/inputData.csv"

# 用户版本信息文件
VERSION_TXT = ROOT_DIR + "/version.txt"

# 状态代码文件
STATUS_CODE = ROOT_DIR + "/statusCode.json"

# 开发环境
ENV = "dev"
# 测试环境
# ENV = "test"
# 生产环境
# ENV = "produce"
