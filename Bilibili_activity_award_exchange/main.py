import requests

headers = {
    "authority": "api.bilibili.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://www.bilibili.com",
    "referer": "https://www.bilibili.com/blackboard/activity-award-exchange.html?task_id=fcba31d0",
    "sec-ch-ua": "^\\^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
# bili_jct是data中csrf参数
cookies = {

}
url = "https://api.bilibili.com/x/activity/mission/task/reward/receive"
data = {
    "csrf": "",  # 必填项，从cookie中的bili_jct获取
    "act_id": "688",
    "task_id": "2715",
    "group_id": "0",
    "receive_id": "0",
    "receive_from": "missionPage",
    "act_name": "崩坏：星穹铁道1.0创作者激励计划【直播任务】",
    "task_name": "直播间新增1名舰长",
    "reward_name": "星轨通票*3",
    "gaia_vtoken": ""
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)
