from typing import Any

import requests
import base64
import time
import os.path


def ocr(img_path: str) -> list[Any] | str:
    """
    根据图片路径，将图片转为文字，返回识别到的字符串列表
    """
    # 请求头
    headers = {
        'Host': 'cloud.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76',
        'Accept': '*/*',
        'Origin': 'https://cloud.baidu.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://cloud.baidu.com/product/ocr/general',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    # 打开图片并对其使用 base64 编码
    with open(img_path, 'rb') as f:
        img = base64.b64encode(f.read())
    data = {
        'image': 'data:image/jpeg;base64,' + str(img)[2:-1],
        'image_url': '',
        'type': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
        'detect_direction': 'false'
    }
    # 开始调用 ocr 的 api
    response = requests.post(
        'https://cloud.baidu.com/aidemo', headers=headers, data=data)

    # 设置一个空地列表，后面用来存储识别到的字符串
    ocr_text = []
    result = response.json()['data']
    if not result.get('words_result'):
        return []

    # 将识别的字符串添加到列表里面
    for r in result['words_result']:
        text = r['words'].strip()
        ocr_text.append(text)
        # 返回字符串列表
    last_result = "".join(ocr_text)
    return last_result


def pic_save():
    pic_name = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())) + '.png'
    pic_path = os.path.abspath('..') + '\\screenshot\\'
    pic = pic_path + pic_name
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    return pic

# '''
# img_path 里面填图片路径,这里分两种情况讨论:
# 第一种:假设你的代码跟图片是在同一个文件夹，那么只需要填文件名,例如 test1.jpg (test1.jpg 是图片文件名)
# 第二种:假设你的图片全路径是 D:/img/test1.jpg ,那么你需要填 D:/img/test1.jpg
# '''
# img_path = 'G:\\pythonProject\\WEB_UI_TEST\\screenshot\\2023-03-13-10-43-47.png'
# # # content 是识别后得到的结果
# print(ocr(img_path))

