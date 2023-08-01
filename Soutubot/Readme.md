# Win10 / Win11自动过cloudflare验证

1. 安装WebView2
2. 使用Pywebview模块打开需要过验证的网站
3. 加载函数获取对应的ua和cookie
```python
def read_cookies(window):
    """获取cookie以解决机器人验证"""
    match = re.search(r"cf_clearance=([^;]+)", str(window.get_cookies()[0]))
    if match:
        # 提取匹配到的内容
        cf_clearance_value = match.group(1)
        cookies["cf_clearance"] = cf_clearance_value
        window.destroy()


def js(window):
    """获取ua"""
    headers["user-agent"] = window.evaluate_js("navigator.userAgent")
    read_cookies(window)

window = webview.create_window(title="验证", url="https://soutubot.moe")
webview.start(js, window, private_mode=False)
```