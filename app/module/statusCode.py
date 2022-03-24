from MF_StatusCode import StatusCode
from config import STATUS_CODE

statusCode = StatusCode()
statusCode.add_status_code(STATUS_CODE)


def get_statusCode(code):  # 状态码管理
    return statusCode.get_code(code)
