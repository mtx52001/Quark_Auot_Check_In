import requests
import os

def quark_sign():
    # 读取你刚才存进Secrets里的Cookie
    cookie = os.environ.get("QUARK_COOKIE")
    if not cookie:
        print("没找到Cookie，请检查Secrets设置！")
        return

    # 👇 就是加了这一句核心魔法！自动洗掉所有不小心沾上的换行符和首尾空格
    cookie = cookie.strip().replace('\n', '').replace('\r', '')

    url = "https://drive.quark.cn/1/clouddrive/capacity/growth/sign"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": cookie
    }
    
    try:
        response = requests.post(url, headers=headers)
        # 尝试把结果转换成更容易看懂的文字
        response.encoding = 'utf-8'
        print("🎉 签到执行完毕，夸克返回结果：", response.text)
    except Exception as e:
        print("❌ 执行出错：", e)

if __name__ == "__main__":
    quark_sign()
