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
        # 维持苹果手机的伪装身份
        "User-Agent": "Quark/6.9.2.326 (iPhone; iOS 16.5; Scale/3.00)",
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    
    # 👇 重点在这里！这是真正的“点击签到”动作指令
    payload = {"sign_cyclic": True}
    
    try:
        # 把指令一起发送给夸克
        response = requests.post(url, headers=headers, json=payload)
        response.encoding = 'utf-8'
        print("🎉 夸克返回结果：", response.text)
    except Exception as e:
        print("❌ 执行出错：", e)

if __name__ == "__main__":
    quark_sign()
