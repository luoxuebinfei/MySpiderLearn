import json
import re
import requests

headers = {
    "authority": "cangku.moe",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "dnt": "1",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                  "Safari/537.36"
}
# 抓包获取
cookies = {
    "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "",
    "XSRF-TOKEN": "",
    "cangku_laravel_session": ""
}
url = "https://cangku.moe/api/v1/user/unreadNotificationCount"
session = requests.session()
response = session.get(url, headers=headers, cookies=cookies)

for i in response.headers["set-cookie"].split(";"):
    if "XSRF-TOKEN" in i:
        a = i.split("=")[1]
        cookies["XSRF-TOKEN"] = a
        headers["X-XSRF-TOKEN"] = a
    if "cangku_laravel_session" in i:
        b = re.findall(r".*?cangku_laravel_session=(.*)/?", i)[0]
        cookies["cangku_laravel_session"] = b

# 签到url
url = "https://cangku.moe/api/v1/user/signin"
res = requests.post(url, headers=headers, cookies=cookies)
# json_res = json.loads(res.text)
# print(json_res["message"])
print(res.text)
print(res)

# {"code":0,"data":{"continuous_signin":110,"exp":10,"point":5},"message":"\u7b7e\u5230\u6210\u529f","status_code":"200"}
# <Response [200]>

# {"code":1,"message":"\u4eca\u65e5\u5df2\u7b7e\u5230","status_code":400}
# <Response [400]>
