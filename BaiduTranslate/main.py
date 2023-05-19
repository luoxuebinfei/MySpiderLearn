import json

import requests
import execjs


def get_sign(eng):
    node = execjs.get()
    with open('getsign.js', encoding='utf-8') as f:
        js_code = f.read()
    ctx = node.compile(js_code, cwd=r'..\node_modules')
    sign = ctx.call('sign', eng)
    return sign


def spider(eng):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Acs-Token": "1684411289159_1684484739109_YtxFClE2ET5IT6QDAQk+CFHu5NwSHGKFWJSBPHPxgLc4kKDJACjZJZAHg9kWwEve5mLsNraqoIgdHVK+rOa2xvAUp41MM7Yr2+saFQ5L1mHMTujpjYilWrJbrCLvrLyacNKhDrHj1MO9R9HARYNviCN2biqRmMcBxuk1/obFUgkpEGxkFjlhqTgSA+2dqM5ufjIZ4h6xLY1of1ThGEJvROAYUvGQ79syg2u3DypkgMzOZltMNpSzIxNjhLF5XIqwrUyGCZ54DMJjiXTEedmEsnaOa+kGg1cxDtHRGz9NGOQjI30xYPMgztTenuI4USaSmMFWqTy++jPIwU4/jhscMKaJTRYkTuyX8UWd/DXlP4t3dSjdJDIX+Ug699wiS6ozCR//3J2VKgpSwblwgMmVGvBfG5PnB7Cg3a9lmqyzOta7KjjfHPKU9u9oAi2yAC7i9RgiirRZ2hQf46Izzp0eEXyYLDODXSBXmU6qllwMC9A=",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Origin": "https://fanyi.baidu.com",
        "Referer": "https://fanyi.baidu.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                      "Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "BAIDUID": "0FDA0DF18AE2D406E98A9EB4E0E7C0A9:FG=1",
        "BAIDUID_BFESS": "0FDA0DF18AE2D406E98A9EB4E0E7C0A9:FG=1",
        "APPGUIDE_10_0_2": "1",
        "REALTIME_TRANS_SWITCH": "1",
        "FANYI_WORD_SWITCH": "1",
        "HISTORY_SWITCH": "1",
        "SOUND_SPD_SWITCH": "1",
        "SOUND_PREFER_SWITCH": "1"
    }
    url = "https://fanyi.baidu.com/v2transapi"
    params = {
        "from": "en",
        "to": "zh"
    }
    data = {
        "from": "en",
        "to": "zh",
        "query": eng,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": get_sign(eng),
        "token": "b97b6fc71550d4fd207e307f71134e08",
        "domain": "common",
        "ts": "1684484739088"
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    res = json.loads(response.text)
    ch = res['trans_result']['data'][0]['dst']
    print("翻译结果：",ch)


if __name__ == '__main__':
    spider(input("请输入要翻译的英文单词："))

