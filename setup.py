# encoding=UTF-8
from app.main import main
from MF_Version import Version
from config import ENV, VERSION_TXT

version = Version()

if __name__ == '__main__':
    if ENV == "dev":  # 判断开发环境
        version.set_version_path(VERSION_TXT)
        version.set_version()
    main()
