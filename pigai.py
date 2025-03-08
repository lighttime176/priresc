import requests
import os
os.environ['no_proxy'] = '*'
cookies = {
    'old': '2012',
    'PHPSESSID': '0a7djvl5rgjbdjras19u8a88b7',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'old=2012; PHPSESSID=0a7djvl5rgjbdjras19u8a88b7',
    'Origin': 'http://pigai.org',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://pigai.org/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
    'a': 'login',
}

data = {
    'username': '111111111',
    'password': '',
    'checkhash': '',
    'password_encrypt': 'SyTcBdd2bgSnL8hw0HggMIH931+Y8VJkKJcIFieHHN10j3sKAHcENOzQVYImzyosmKjoQsAV0yeuXM73EeBamv4MkuvU8sTz+55/wdiugovboDt7fOewLxrKQk0PwfmQlgX49m4l/JmBuCRfBKDgewXIMno4rrTLMSTspRiKH+w=',
}

response = requests.post('http://pigai.org/index.php', params=params, cookies=cookies, headers=headers, data=data, verify=False)
print(response.text)