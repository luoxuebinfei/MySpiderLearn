import json

# 解决decode_data函数中ctx.call的'NoneType' object has no attribute 'replace'报错问题
# import subprocess
# from functools import partial
#
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

# 第二种方法
import subprocess


class MySubprocessPopen(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(encoding="utf-8", *args, **kwargs)


subprocess.Popen = MySubprocessPopen

import execjs
import requests


def get_sign():
    node = execjs.get()
    with open("get_sign.js", encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd=r'..\node_modules')
    sign = ctx.call("run")
    return sign[0], sign[1]


def decode_data(data: str):
    node = execjs.get()
    with open("decode.js", encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code, cwd=r'..\node_modules')
    text = ctx.call("run", data)
    return text


def spider(k):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "DNT": "1",
        "Origin": "https://fanyi.youdao.com",
        "Referer": "https://fanyi.youdao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "OUTFOX_SEARCH_USER_ID": "-1070197359@10.105.137.202",
        "OUTFOX_SEARCH_USER_ID_NCOO": "371334273.2126965"
    }
    url = "https://dict.youdao.com/webtranslate"
    sign, t = get_sign()
    data = {
        "i": k,
        "from": "auto",
        "to": "",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": t,
        "keyfrom": "fanyi.web"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    # print(response.text)
    return response.text


if __name__ == '__main__':
    word = input("请输入英文：")
    x = spider(word)
    json_text = json.loads(decode_data(x))["dictResult"]["ec"]["word"]["trs"]
    print("翻译结果：")
    for i in json_text:
        print(i["tran"])
