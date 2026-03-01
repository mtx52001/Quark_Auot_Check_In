import requests
import os

def quark_sign():
    cookie = os.environ.get("QUARK_COOKIE")
    if not cookie:
        print("没找到Cookie！")
        return

    # 自动清理可能多余的空格和换行
    cookie = cookie.strip().replace('\n', '').replace('\r', '')

    url = "https://drive.quark.cn/1/clouddrive/capacity/growth/sign?pr=ucpro&fr=pc&s=fe"
    headers = {
        # 核心魔法：在这里伪装成苹果手机的夸克App，骗过服务器！
        "User-Agent": "Quark/6.9.2.326 (iPhone; iOS 16.5; Scale/3.00)",
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    
    try:
        response = requests.post(url, headers=headers)
        response.encoding = 'utf-8'
        print("🎉 夸克返回结果：", response.text)
    except Exception as e:
        print("❌ 执行出错：", e)

if __name__ == "__main__":
    quark_sign()
