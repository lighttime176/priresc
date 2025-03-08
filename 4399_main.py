import requests
import time
import execjs
import os
os.environ['no_proxy'] = '*'
cookies = {
    'UM_distinctid': '188a0c2d29571f-0db40565aa8f82-26031d51-144000-188a0c2d2967b1',
    '_4399stats_vid': '16863243194082150',
    'Puser': '26961213',
    'ptusertype': 'dev4399.4399_login',
    'Pnick': '%E7%89%A7%E7%BE%8A%E7%9A%84%E9%97%AE%E5%8F%B7',
    'Qnick': '',
    '_gprp_c': '""',
    'home4399': 'yes',
    'Hm_lvt_334aca66d28b3b338a76075366b2b9e8': '1689671197',
    'USESSIONID': '6cbf2f8f-8f1a-4022-9730-1f751363a5f6',
    'Qauth': 'be75020a-25bf-46dd-a81e-eb63028812e0_1689671377293_6c23f2a1',
    'Hm_lpvt_334aca66d28b3b338a76075366b2b9e8': '1689671740',
    'phlogact': 'l133346',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'UM_distinctid=188a0c2d29571f-0db40565aa8f82-26031d51-144000-188a0c2d2967b1; _4399stats_vid=16863243194082150; Puser=26961213; ptusertype=dev4399.4399_login; Pnick=%E7%89%A7%E7%BE%8A%E7%9A%84%E9%97%AE%E5%8F%B7; Qnick=; _gprp_c=""; home4399=yes; Hm_lvt_334aca66d28b3b338a76075366b2b9e8=1689671197; USESSIONID=6cbf2f8f-8f1a-4022-9730-1f751363a5f6; Qauth=be75020a-25bf-46dd-a81e-eb63028812e0_1689671377293_6c23f2a1; Hm_lpvt_334aca66d28b3b338a76075366b2b9e8=1689671740; phlogact=l133346',
    'Origin': 'https://ptlogin.4399.com',
    'Referer': 'https://ptlogin.4399.com/ptlogin/login.do?v=1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'v': '1',
}

data = {
    'loginFrom': 'uframe',
    'postLoginHandler': 'default',
    'layoutSelfAdapting': 'true',
    'externalLogin': 'qq',
    'displayMode': 'popup',
    'layout': 'vertical',
    'bizId': '',
    'appId': 'www_home',
    'gameId': '',
    'css': '',
    'redirectUrl': '',
    'sessionId': '',
    'mainDivId': 'popup_login_div',
    'includeFcmInfo': 'false',
    'level': '0',
    'regLevel': '4',
    'userNameLabel': '4399用户名',
    'userNameTip': '请输入4399用户名',
    'welcomeTip': '欢迎回到4399',
    'sec': '1',
    'password': 'U2FsdGVkX1+1GAVdoOyJha4SkIUlWIV3RuJ0mNFWt50=',
    'username': '1764682172_2',
    'autoLogin': 'on',
}
if __name__=="__main__":
    jscode = open('./4399_login.js', 'r', encoding='utf-8').read()
    parames = execjs.compile(jscode).call('encryptAES',"123456")
    data['password'] =parames
    response = requests.post('https://ptlogin.4399.com/ptlogin/login.do', params=params, cookies=cookies, headers=headers, data=data)
    print(response.text)