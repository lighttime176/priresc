import requests
import time
import execjs
import os


os.environ['no_proxy'] = '*'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'portal-sign': 'cc7b689db72ac5ecc3f3e610cc594dab',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'type': '12',
    'IS_IMPORT': 1,
    'pageSize': 3,
    'ts': 1689406293409,
}

if __name__=="__main__":
    jscode = open('./fjgov_data.js', 'r', encoding='utf-8').read()
    parames = execjs.compile(jscode).call('main_1')
    print(parames)
    headers['portal-sign'] = parames['portal_sig']
    print(headers['portal-sign'])
    timestamp = time.time()
    print(timestamp)
    json_data['ts'] = parames['ts']
    response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Article/PageList', headers=headers, json=json_data).json()
    print(response)
