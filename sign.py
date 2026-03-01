import requests
import os

def quark_sign():
    # 读取你刚才存进Secrets里的Cookie
    cookie = os.environ.get("QUARK_COOKIE")
    if not cookie:
        print("没找到Cookie，请检查Secrets设置！")
        return

    url = "https://drive.quark.cn/1/clouddrive/capacity/growth/sign"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie
    }
    
    try:
        response = requests.post(url, headers=headers)
        print("🎉 签到执行完毕，返回结果：", response.text)
    except Exception as e:
        print("❌ 执行出错：", e)

if __name__ == "__main__":
    quark_sign()
