import requests
import os
import execjs



os.environ['no_proxy'] = '*'
cookies = {
    'btoken': '2EU7BXVVQ5GXYME92RTSQ7I1NBD88C3A',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1689388039',
    'hy_data_2020_id': '189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%22189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1689388080',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'btoken=2EU7BXVVQ5GXYME92RTSQ7I1NBD88C3A; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1689388039; hy_data_2020_id=189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%22189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%22189575fbc116f6-00bca70548982a-26031d51-1327104-189575fbc121025%22%7D; sajssdk_2020_cross_new_user=1; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1689388080',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBc3V0I6ZGB6bXsxTCQnPRBuBhgbPj1fJDpwd2R1Tw==',
    'sig': '49AF9D32DA6AA7E5B32214EC011FE0B7',
    'v': 1,
}





if __name__=="__main__":
    jscode = open('./xiniu.js', 'r', encoding='utf-8').read()
    parames = execjs.compile(jscode).call('main_1')
    json_data['payload'] = parames['payload']
    json_data['sig'] = parames['sig']
    print(json_data['payload'])
    print(json_data['sig'])
    response = requests.post(
        'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).json()
    text = response['d']
    #print(response)
    jscode = open('./xiniu_data.js', 'r', encoding='utf-8').read()
    parames = execjs.compile(jscode).call('main_2',text)
    print(parames)