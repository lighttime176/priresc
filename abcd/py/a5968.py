from DrissionPage import Chromium, ChromiumOptions
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
import os, time,random,base64,logging
from threading import Thread
import ddddocr,requests
import re,pytz
import json
import sys
from datetime import datetime
# 全局变量
# phonenum = os.environ.get("ydyp")
# masked_phone = phonenum[:3] + '****' + phonenum[-4:]
phonenum = '13007665968'
masked_phone = phonenum
log_filename = "logs/a5968.log"

def aliyun(tab, browser):
    
    tab.get('https://account.aliyun.com')
    ele = tab.ele('text=注册')
    time.sleep(0.5)
    ele.click()
    ele = tab.ele(
        'css=#container > div > form > div > div.next-form-item.next-row.biz-form-component-AsyncCheckInput-field-item.mobile_reg > div > div.next-form-item.next-row.async-check-input > div > span > span.next-input.next-input-single.next-input-large > input[type=text]')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='registerLegacy')
    ele = tab.ele(
        'css=#container > div > form > div > div.next-form-item.next-row.biz-form-component-MobileMsgCheckInForm-field-item.mobile_reg > div > div.next-form-item.next-row.mobile-msg-check-in-form > div > span > span > span.next-input-addon.next-input-addon-after > button')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----阿里云{masked_phone}----：{res}')
    except:
        logger.info('阿里云注册失败')
    browser.quit()  # 关闭浏览器


def baidu(tab, browser):
    
    tab.get('https://www.baidu.com/')
    ele = tab.ele('css=#s-top-loginbtn')
    time.sleep(0.5)
    ele.click(by_js=True)
    ele = tab.ele('css=#TANGRAM__PSP_11__changeSmsCodeItem')
    time.sleep(0.5)
    ele.click(by_js=True)
    ele = tab.ele('css=#TANGRAM__PSP_11__smsPhone')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='api/senddpass')
    ele = tab.ele('css=#TANGRAM__PSP_11__smsTimer')
    time.sleep(0.5)
    ele.click(by_js=True)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----百度{masked_phone}----：{res}')
    except:
        logger.info('百度注册失败')
    browser.quit()  # 关闭浏览器


def fenghuang(tab, browser):
    
    tab.get('https://user.ifeng.com/register/')
    ele = tab.ele(
        'css=#root > div > div.index_main_x8Om1.clearfix.w1000 > div.index_formContent_IsGlh > div.index_box_tjcy1 > div.index_formList_miyat > div > div.index_innerWrapper_bc67f > div.index_userName_tlg6E.clearfix > label > div > div > input[type=text]')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='sendsms')
    ele = tab.ele(
        'css=#root > div > div.index_main_x8Om1.clearfix.w1000 > div.index_formContent_IsGlh > div.index_box_tjcy1 > div.index_formList_miyat > div > div.index_innerWrapper_bc67f > div.index_vCode_SojNC.clearfix > div')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----凤凰网{masked_phone}----：{res}')
    except:
        logger.info('凤凰网注册失败')
    browser.quit()  # 关闭浏览器


def ltyp(tab, browser):
    
    tab.get('https://pan.wo.cn/login')
    ele = tab.ele('css=#pane-2 > form > div:nth-child(1) > div > div > input')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='sendMessageCodeBase')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#pane-2 > form > div:nth-child(2) > div > div > div > span > span > div > div:nth-child(1)')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----联通云盘{masked_phone}----：{res}')
    except:
        logger.info('联通云盘注册失败')
    browser.quit()  # 关闭浏览器


def tyyp(tab, browser):
    global phonenum
    tab.get('https://cloud.189.cn/web/login.html')
    time.sleep(0.5)
    ele = tab.ele('css=#tab-pw > span')
    time.sleep(0.5)
    ele.click()
    ele = tab.ele('css=#j-jump-sms')
    time.sleep(0.5)
    ele.click()
    ele = tab.ele('css=#dynamicUserName')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='/sendSmsCode.do')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#j-msg-verifyCode')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----天翼云盘{masked_phone}----：{res}')
    except:
        logger.info('天翼云盘注册失败')
    browser.quit()  # 关闭浏览器

def xhs(tab, browser):
    global phonenum
    tab.get('https://www.xiaohongshu.com/explore')
    time.sleep(10)
    try:
        ele = tab.ele(
            'css=#app > div:nth-child(1) > div > div.login-container > div.right > div.input-container.mt-20px > form > label.phone > input[type=text]')
        ele.input(phonenum)
    except:
        logger.info('小红书输入手机号元素未找到')
    tab.listen.start(targets='send_code?phone')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele(
        'css=#app > div:nth-child(1) > div > div.login-container > div.right > div.input-container.mt-20px > form > label.auth-code > span')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----小红书{masked_phone}----：{res}')
    except:
        logger.info('小红书注册失败')
    browser.quit()  # 关闭浏览器


def xueqiu(tab, browser):
    global phonenum
    tab.get('https://xueqiu.com/')
    time.sleep(0.5)
    ele = tab.ele(
        'css=#modal__login__main > div.newLogin_modal__login__mod_37E > div:nth-child(1) > div.newLogin_modal__login__form_JoE > div > div > form > div:nth-child(1) > input[type=text]')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='/account/sms/')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#modal__login__main > div:nth-child(2) > label > i')
    time.sleep(0.5)
    ele.click()
    ele = tab.ele(
        'css=#modal__login__main > div.newLogin_modal__login__mod_37E > div:nth-child(1) > div.newLogin_modal__login__form_JoE > div > div > form > div:nth-child(2) > span > a')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----雪球{masked_phone}----：{res}')
    except:
        logger.info('雪球注册失败')
    browser.quit()  # 关闭浏览器


def juliang(tab, browser):
    global phonenum
    tab.get('https://business.oceanengine.com/login')
    time.sleep(0.5)
    ele = tab.ele(
        'css=#account-sdk > section > div.account-center-sdk-form > div:nth-child(1) > div > div > span > input')
    time.sleep(0.5)
    ele.input(phonenum)
    tab.listen.start(targets='send_activation_code')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele(
        'css=#account-sdk > section > div.account-center-sdk-form > div.account-center-input-row.account-center-fetch-code-row.ac-input-last-item > div > div > div')
    time.sleep(0.5)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----巨量{masked_phone}---- ：{res}')
    except:
        logger.info('巨量注册失败')
    browser.quit()  # 关闭浏览器


def tuxi(tab, browser):
    global phonenum
    tab.get('https://kdcs.tuxi.com/#/login')
    ele = tab.ele(
        'css=#main > div > div.login-box > div.login-content > div.login-content-right > div.login-content-mode > div:nth-child(2)')
    ele.click()
    ele = tab.ele(
        'css=#main > div > div.login-box > div.login-content > div.login-content-right > form > div:nth-child(1) > div > div > input')
    ele.input(phonenum)
    tab.listen.start(targets='gateway.do')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele(
        'css=#main > div > div.login-box > div.login-content > div.login-content-right > form > div:nth-child(2) > div > div > div > div > p.verify-code-input-btn')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----兔喜{masked_phone}---- ：{res}')
    except:
        logger.info('兔喜注册失败')
    browser.quit()  # 关闭浏览器


def shuidichou(tab, browser):
    global phonenum
    tab.get('https://www.shuidichou.com/')
    ele = tab.ele(
        'css=#__layout > div > div > div.container > div > div > div > div > div > div.user-info > div:nth-child(2) > input[type=number]')
    ele.input(phonenum)
    tab.listen.start(targets='verify-code-send')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele(
        'css=#__layout > div > div > div.container > div > div > div > div > div > div.user-info > div.agreement-wrapper > div > img')
    ele.click()
    time.sleep(0.5)
    ele = tab.ele(
        'css=#__layout > div > div > div.container > div > div > div > div > div > div.user-info > div:nth-child(3) > span')
    time.sleep(0.5)
    ele.click(by_js=True)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----水滴筹{masked_phone}---- ：{res}')
    except:
        logger.info('水滴筹注册失败')
    browser.quit()  # 关闭浏览器
def doubao(tab, browser):
    tab.get('https://www.doubao.com/chat/')
    time.sleep(0.5)

    ele = tab.ele(
        'css=#root > div.flow-web-root-outlet > div > div.containerWrapper-zs8cOO > div.panelWrapper-w47RMk > div.center-full-DCvpXt > div > div > div.header-QmdZVu > div > div > div > div.right-ANm42w > div > button > span')
    time.sleep(0.5)
    ele.click()

    ele = tab.ele(
        'css=#semi-modal-body > div > div > div > div > div.right-hYaO8h > div.common-Zuuqix > div.main-WuxhPQ > div > div.semi-input-wrapper.input-UlJxZ5.semi-input-wrapper-large > input')
    time.sleep(0.5)
    ele.input(phonenum)

    ele = tab.ele('text=下一步')
    time.sleep(0.5)
    ele.click()

    tab.listen.start(targets='send_code')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('text=同意')
    time.sleep(0.5)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----豆包{masked_phone}----：{res}')
    except:
        logger.info('豆包注册失败')
    browser.quit()  # 关闭浏览器


def kye(tab, browser):
    tab.get('https://uc.ky-express.com/#/login/password?sourceFrom=website')
    ele = tab.ele('css=#tab-sms')
    ele.click()
    ele = tab.ele('css=#pane-sms > form > div.el-form-item.phone > div > div > input')
    ele.input(phonenum)

    tab.listen.start(targets='ic-api.ky-express.com')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#pane-sms > form > div.el-form-item.input-full > div > div.smsCodeWrapper > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----KYE{masked_phone}---- ：{res}')
    except:
        logger.info('KYE注册失败')
    browser.quit()  # 关闭浏览器

def webcsdn(tab,browser):
  tab.get('https://webapp.csdn.net/')

  ele = tab.ele('css=#app > div > div > div > div > div.newLogin-mobile > div.newLogin-mobile_phone > input')
  ele.input(phonenum)
  tab.listen.start(targets='sendAppVerifyCode')  # 开始监听，指定获取包含该文本的数据包
  ele = tab.ele('css=#app > div > div > div > div > div.newLogin-mobile > div.newLogin-mobile_passNum > div')
  ele.click()
  time.sleep(1)
  try:
      ele.click()
  except:
      logger.info("")
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----webcsdn学院{masked_phone}----：{res}')
  except:
      logger.info('webcsdn注册失败')
  browser.quit()  # 关闭浏览器


def huoshanyq(tab, browser):
    tab.get('https://console.volcengine.com/auth/signup')
    time.sleep(1)
    ele = tab.ele('css=#Tel_input')
    ele.input(phonenum)

    tab.listen.start(targets='login/sendSignupSms')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#arco-tabs-0-panel-0 > div > div > form > label > span.arco-icon-hover.arco-checkbox-icon-hover.arco-checkbox-mask-wrapper > div')
    ele.click()
    time.sleep(1)
    ele = tab.ele('css=#arco-tabs-0-panel-0 > div > div > form > div.verify-J9zAGM > div:nth-child(2) > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----火山引擎{masked_phone}---- ：{res}')
    except:
        logger.info('火山引擎注册失败')
    browser.quit()  # 关闭浏览器


def juren(tab, browser):
    tab.get('https://reg.ztgame.com/')
    time.sleep(1)

    ele = tab.ele('text=+86')
    # logger.info(ele)
    ele = ele.next()
    # logger.info(ele)
    ele.input(phonenum)
    tab.listen.start(targets='/query?account=')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#reg_form > div:nth-child(8) > input.get-mpcode')
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----巨人网络{masked_phone}---- ：{res}')
    except:
        logger.info('巨人网络注册失败')
    browser.quit()  # 关闭浏览器

def kzxy(tab,browser):
  tab.get('https://ci.cn/grzx#/mobile')
  time.sleep(0.5)
  sr_ele = tab.ele('css=body > oi-import').shadow_root
  #logger.info(sr_ele)
  sr_ele = tab.ele('css=ci-m-2').shadow_root
  #logger.info(sr_ele)
  ele = sr_ele.ele('css=#phone')
  time.sleep(0.5)
  ele.input(phonenum)
  tab.listen.start(targets='/phoneCode')  # 开始监听，指定获取包含该文本的数据包
  ele = sr_ele.ele('css=div > div > div > form > div:nth-child(3) > div > button')
  time.sleep(0.5)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----孔子学院{masked_phone}----：{res}')
  except:
      logger.info('孔子学院注册失败')
  browser.quit()  # 关闭浏览器


def mita(tab, browser):
    tab.get('https://www.xiezuocat.com/')
    ele = tab.ele('css=#app > div.fullscreen.recent-file-page > section > header > div > div:nth-child(2) > div > img')
    ele.click()
    ele = tab.ele('css=#login-wrap > div > div > div.login-content > div > div > div.other-login > div:nth-child(1)')
    ele.click()
    ele = tab.ele('css=#login-wrap > div > div > div.login-content > div > form > div:nth-child(1) > div > div > input')
    ele.input(phonenum)
    tab.listen.start(targets='verify?')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#login-wrap > div > div > div.login-content > div > form > div:nth-child(2) > div > div > div > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----秘塔{masked_phone}----：{res}')
    except:
        logger.info('秘塔注册失败')
    browser.quit()  # 关闭浏览器


def nfby(tab, browser):
    tab.get('https://www.cnppump.ltd/#/CN/login/tel')
    ele = tab.ele('css=#pane-tel > div > button:nth-child(6)')
    ele.click()
    time.sleep(2)
    ele = tab.ele('text=手机号')
    # logger.info(ele.text)
    ele = ele.next().child().child().next().child().child()
    # logger.info(ele)

    ele.click()
    time.sleep(2)
    tab.actions.type(phonenum)
    tab.listen.start(targets='GetTelVerifyCode3')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#app > div > div.forms-container > div > form.el-form.el-form--default.el-form--label-right.sign-up-form.login_form > div > div > div:nth-child(3) > div > div:nth-child(2) > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----南方泵业{masked_phone}----：{res}')
    except:
        logger.info('南方泵业注册失败')
    browser.quit()  # 关闭浏览器

def ydyp(tab, browser):
    tab.get('https://yun.139.com/w/#/')

    ele = tab.ele(
        'css=#app > div.login-base > div.default_box.login-box-position > div:nth-child(3) > div.default_box_phone > input[type=text]:nth-child(4)')
    time.sleep(0.5)
    ele.input(phonenum)

    tab.listen.start(targets='/getSmsVerifyCode')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#app > div.login-base > div.default_box.login-box-position > div:nth-child(3) > div.default_box_phone > span')
    time.sleep(0.5)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----移动云盘{masked_phone}---- ：{res}')
    except:
        logger.info('移动云盘注册失败')
    browser.quit()  # 关闭浏览器


def yiche(tab, browser):
    tab.get('https://i.yiche.com/authenservice/login.html?returnurl=https%3A%2F%2Fwww.yiche.com%2F')

    ele = tab.ele('css=#mobile')
    ele.input(phonenum)

    ele = tab.ele('css=#checkbox')
    ele.click()
    ele = tab.ele('css=#send-code-button')
    ele.click()
    ele = tab.ele('css=#code-seconds-tips')
    time.sleep(2)
    logger.info(f'----易车{masked_phone}----：{ele.text}')
    browser.quit()  # 关闭浏览器
def leyuan233(tab, browser):
    tab.get('https://dev.233leyuan.com/#/login?type=code')
    ele = tab.ele(
        r'css=#app > div > div.flex-1.flex.justify-end.mr-\[88px\] > div > form > div.el-form-item.is-required.asterisk-left.\!mb-8.\!mt-4 > div > div > div')
    ele.click()
    tab.actions.type(phonenum)

    ele = tab.ele(
        r'css=#app > div > div.flex-1.flex.justify-end.mr-\[88px\] > div > form > div:nth-child(2) > div > div > button > span')
    ele.click()
    time.sleep(2)
    ele = tab.ele(
        r'css=#app > div > div.flex-1.flex.justify-end.mr-\[88px\] > div > form > div:nth-child(2) > div > div > button > span')
    logger.info(f'----233乐园{masked_phone}----：验证码倒计时{ele.text}s')
    browser.quit()  # 关闭浏览器
def qyiliao(tab,browser):
    tab.get(
        'https://ucenter.cn-healthcare.com/rlogin/tologin?redirectUrl=https://www.cn-healthcare.com/articlewm/20221130/content-1475807.html')
    ele = tab.ele('css=#memUserIdSms')
    ele.input(phonenum)
    tab.listen.start(targets='/sendMobile')
    ele = tab.ele('css=#mvalCode')
    ele.click()
    ele = tab.ele('css=#getvcode')
    time.sleep(2)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----q医疗{masked_phone}----：{res}')
    except:
        logger.info('q医疗注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def lmt(tab,browser):
    tab.get('https://lmtw.com/mzw/content/detail/id/175656')
    ele = tab.ele('css=body > div.container-fluid > div.container-right > header > div > span > a:nth-child(2)')
    ele.click()
    ele = tab.ele('css=#reg_mobile')
    ele.input(phonenum)
    tab.listen.start(targets='/ajaxSend')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#mobile-register-form > div:nth-child(2) > span > a')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----指南者{masked_phone}----：{res}')
    except:
        logger.info('指南者注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器

def sd(tab,browser):
    tab.get('https://www.0101ssd.com/')
    ele = tab.ele('css=body > div.headNewH > div.headNewTop > div > div > div.statusStyle > a')
    ele.click()
    ele = tab.ele('css=body > div.headNewH > div.headNewTop > div > div > div.statusStyle > div > a:nth-child(2)')
    ele.click()
    ele = tab.ele('css=#mobileRiste')
    ele.input(phonenum)
    tab.listen.start(targets='https://www.0101ssd.com/user/sendmsg')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#risteSend')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----闪德{masked_phone}----：{res}')
    except:
        logger.info('闪德注册失败')
    browser.quit()  # 关闭浏览器

def sftc(tab,browser):
    tab.get(
        'https://passtc.sf-express.com/ucenter/userlogin?platform=crm&redirect_url=https%3A%2F%2Fshopic.sf-express.com%2Fcrm%2Fcommon%2Frender%2Fproduct%2Fcrm%2Fpage%2Findex%3Fplatform%3D3000818&return_url=https%3A%2F%2Fshopic.sf-express.com%2Fcrm%2Fcommon%2Fsetstoken')

    ele = tab.ele('css=#main > div.login-box > div > div.crm-login-option > div > span')
    ele.click()

    ele = tab.ele('css=#main > div.login-box > div > form > div.login-userphone > div.input-item > input')
    ele.input(phonenum)
    tab.listen.start(targets='https://passtc.sf-express.com/api/websms')

    ele = tab.ele('css=#main > div.login-box > div > form > div.login-num-vcode > div.num-vcode-switch > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----顺丰同城{masked_phone}----：{res}')
    except:
        logger.info('顺丰同城注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def wyyyx(tab,browser):
    tab.get('https://cg.163.com/#/mobile')

    ele = tab.ele('css=#app > div.slide.confirm-shade.popup.landscape > div > button')
    ele.click()
    ele = tab.ele('css=#app > header > div > div > div.nav-con > div.nav-userinfo > div.login-btn > div')
    ele.click()
    ele = tab.ele(
        'css=#app > div.login-confirm.confirm-shade.fadein > div > div.cofirm-cont > div > div > div.login-box.login-phone > div.f14.input > input[type=tel]')
    ele.input(phonenum)
    tab.listen.start(targets='/phone-captchas')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#app > div.login-confirm.confirm-shade.fadein > div > div.cofirm-cont > div > div > div.login-box.login-phone > div.g-Btn.g-Btn-green2')
    ele.click()
    ele = tab.ele('css=body > div.confirm-shade.fadein > div > div > div.cofirm-btns.double > a.g-Btn.g-Btn-green2')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----网易云游戏{masked_phone}----：{res}')
    except:
        logger.info('网易云游戏注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def wjs(tab,browser):
    tab.get('https://www.100ec.cn/Index/dsb-reg.html')

    ele = tab.ele('css=#phone')
    ele.input(phonenum)
    ele = tab.ele('css=#email')
    ele.input('sasafda22@qq.com')
    ele = tab.ele('css=#dsbReg > div:nth-child(7) > p > label > span')
    ele.click()
    ele = tab.ele('css=#register')
    ele.click()
    ele = tab.ele('css=#checkInfo')
    ele.click()
    time.sleep(3)
    try:
        ele = tab.ele('css=#dsbLogin1 > div:nth-child(4) > div')
    except:
        logger.info('')
    if ele.text == '登录':
        logger.info(f'----望京设{masked_phone}----：成功')
    else:
        logger.info(f'----望京设{masked_phone}----：失败')
    browser.quit()  # 关闭浏览器

def ycy(tab,browser):
    tab.get('https://wap.avg.163.com/login')
    ele = tab.ele('css=#avgMobileLoginForm > div.mobile-input.form-input > input')
    ele.input(phonenum)
    tab.listen.start(targets='sms')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#avgMobileLoginForm > div.code-input-line.form-input > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----异次元{masked_phone}----：{res}')
    except:
        logger.info('异次元注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def yun88(tab,browser):
    tab.get('https://www.yun88.com/aboutUs/trial')

    ele = tab.ele(
        'css=#__nuxt > div.trial-container > div.mx-auto > div > div > div.right-section > form > div.t-form__item.t-form-item__phone > div.t-form__controls > div > div > div > input')
    ele.input(phonenum)
    tab.listen.start(targets='/sendCodeForApplyJoin')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#__nuxt > div.trial-container > div.mx-auto > div > div > div.right-section > form > div.t-form__item.t-form-item__code > div.t-form__controls > div > div > span > button > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----云88{masked_phone}----：{res}')
    except:
        logger.info('云88注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def znz(tab,browser):
    tab.get('https://lmtw.com/mzw/content/detail/id/175656')
    ele = tab.ele('css=body > div.container-fluid > div.container-right > header > div > span > a:nth-child(2)')
    ele.click()
    ele = tab.ele('css=#reg_mobile')
    ele.input(phonenum)
    tab.listen.start(targets='/ajaxSend')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#mobile-register-form > div:nth-child(2) > span > a')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----指南者{masked_phone}----：{res}')
    except:
        logger.info('指南者注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def a4(tab,browser):
    tab.get('https://www.aippt.cn/?seller=xmp')

    ele = tab.ele('css=#__nuxt > header > div > div.buttons > button.register-button')
    ele.click()
    ele = tab.ele(
        'css=body > div:nth-child(12) > div > div.ant-modal-wrap.dialog-login-home.ant-modal-centered > div > div.ant-modal-content > div > div > div.dialog-login-content > div.dialog-login-change-group > div:nth-child(1)')
    ele.click()
    time.sleep(1)
    ele = tab.ele('css=#custom-validation_account')

    ele.input(phonenum)

    tab.listen.start(targets='https://www.aippt.cn/users/sms/send')
    ele = tab.ele(
        'css=body > div:nth-child(12) > div > div.ant-modal-wrap.dialog-login-home.ant-modal-centered > div > div.ant-modal-content > div > div > div.dialog-login-content > div.dialog-login-content-inner > form > div:nth-child(2) > div > div > div > button > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----aippt{masked_phone}----：{res}')
    except:
        logger.info('aippt注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def b4(tab,browser):
    tab.get('https://aihaoji.com/zh?utm_source=pidoutv&utm_medium=referral')
    time.sleep(1)
    ele = tab.ele(r'css=body > div > div > header.fixed.top-0.z-40.w-full.bg-background > div.flex.h-16.items-center.w-full.px-\[130px\] > div > div > button.Header_buttonStyle__WagzW')
    ele.click(by_js=True)
    ele = tab.ele('text=验证码登录')
    ele.click()
    
    tab.listen.start(targets='https://aihaoji.com/api/v1/user/mobile/send_sms')
    
    sendele = tab.ele('text=获取验证码')
    ele = sendele.parent().parent().prev().child()
    #logger.info(ele)
    ele.input(phonenum)
    time.sleep(2)
    sendele.click()
    
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----AI好记----：{res}')
    except:
        logger.info('AI好记注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def c4(tab,browser):
    tab.get('https://miao.wondershare.cn/?ref=pidoutv.com')

    ele = tab.ele('css=#getRegisterUrl')
    ele.click(by_js=True)
    time.sleep(1)
    try:
        ele.click(by_js=True)
    except:
        pass

    time.sleep(1)
    ele = tab.ele('css=#pane-verify-code > div > form > div:nth-child(1) > div > div > input')

    ele.input(phonenum)
    ele = tab.ele(
        'css=body > div:nth-child(3) > div.pages > div > div > div.pages_main > div > form > div > div > div > div > div > svg > use')
    ele.click()
    tab.listen.start(targets='https://accounts.wondershare.cn/api/v3/mobile/captcha')

    ele = tab.ele('css=#pane-verify-code > div > form > div:nth-child(2) > div > div > span > span > div > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----万兴{masked_phone}----：{res}')
    except:
        logger.info('万兴注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def d4(tab,browser):
    tab.get('https://member.9game.cn/pages/login/pc?bizId=jiuyou&appCode=JIUYOU_PC')
    ele = tab.ele(
        'css=#root > div > div > div > div.PCLogin--tabContent--OPAtdA0 > div > div.mt-input.mt-input--small.mt-input--normal.components--phoneInput--neZeX9j > div.mt-input-textinput-wrapper > input')

    ele.input(phonenum)

    aele = tab.ele(
        'css=#root > div > div > div > div.PCLogin--tabContent--OPAtdA0 > div > div.mt-input.mt-input--small.mt-input--normal.components--passwordInput--uDpxs0v > div.mt-input-items.mt-input-items--small > div > div')
    aele.click()

    ele = tab.ele(
        'css=#root > div > div.rax-view-v2.Dialog--container--B0AyOJy > div.rax-view-v2.Dialog--dialog--Cb2PY8K > div.rax-view-v2.Dialog--dialog-footer--q6z0Z26 > div.rax-view-v2.Dialog--dialog-right-btn--iakKbwy')
    ele.click()
    time.sleep(3)
    logger.info(f'----九游网{masked_phone}----：验证码剩余时间{aele.text}')
    browser.quit()  # 关闭浏览器

def e4(tab,browser):
    tab.get('https://lightmv.cn/')
    ele = tab.ele('css=body > div.lightmv-layout > header > div > div.lightmv-header__menu > button > span')
    ele.click()
    ele = tab.ele(
        'css=#modals-container > div > div > div.v--modal-box.v--modal > div.lightmv-account > div.lightmv-account__login-switch.is-qrcode-login')
    ele.click()
    ele = tab.ele(
        'css=#modals-container > div > div > div.v--modal-box.v--modal > div.lightmv-account > div.lightmv-account__password-less-login-form > div.lightmv-password-less-login-form > form > div:nth-child(1) > div > div > input')

    ele.input(phonenum)

    tab.listen.start(targets='https://aw.aoscdn.com/base/passport/v1/api/captcha')
    ele = tab.ele(
        'css=#modals-container > div > div > div.v--modal-box.v--modal > div.lightmv-account > div.lightmv-account__password-less-login-form > div.lightmv-password-less-login-form > form > div.el-form-item.el-form-item--feedback.is-required > div > div > div > button > span > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----右糖{masked_phone}----：{res}')
    except:
        logger.info('右糖注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def f4(tab,browser):
    tab.get('https://lightmv.cn/')
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'origin': 'https://www.dmhxm.com',
        'priority': 'u=1, i',
        'referer': 'https://www.dmhxm.com/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    params = {
        'mobile': phonenum,
        'type': '2',
    }

    response = requests.get('https://data.mijiaoyu.cn/service/sms/send', params=params, headers=headers)
    logger.info(f'----大米小米{masked_phone}----：{response.json()}')
    browser.quit()  # 关闭浏览器

    
def g4(tab,browser):
    tab.get('https://login.sina.com.cn/signup/signup?entry=blog&srcuid=2037345837&src=blogicp')
    ele = tab.ele('css=#phone-form > div:nth-child(3) > div.ipt > input')
    ele.input(phonenum)
    ele = tab.ele('css=#phone-form > div:nth-child(4) > div.ipt > input')
    ele.input('abcd1234!aa')
    ele = tab.ele('css=#phone-form > div.info_list.clearfix.fav_tags > div.ipt.checklst > label:nth-child(5) > input')
    ele.click()
    tab.listen.start(targets='https://login.sina.com.cn/signup/ajspn')
    ele = tab.ele('css=#phone-form > div:nth-child(6) > div.ipt.active > a > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----手机新浪{masked_phone}----：{res}')
    except:
        logger.info('手机新浪注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def h4(tab,browser):
    tab.get('https://www.hikvision.com/cn/all-forms/Project-consultation/')
    ele = tab.ele('css=#txtContactPhone')
    ele.input(phonenum)
    tab.listen.start(targets='PhoneValidate&phoneNumber')
    ele = tab.ele('css=#enquiry-form > article > article > div:nth-child(4) > div > a')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----海康威视{masked_phone}----：{res}')
    except:
        logger.info('海康威视注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def i4(tab,browser):
    tab.get('https://grow.163.com/free-try?business=%E6%95%B0%E6%99%BA&title=general')

    ele = tab.ele('css=#phone')
    ele.input(phonenum)
    tab.listen.start(targets='/sendCode')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele(
        'css=#app-react-container > div > div > div > div > div.right-content > form > div:nth-child(4) > div > div > span > div > div.fishd-col-8 > button')

    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----网易数字{masked_phone}----：{res}')
    except:
        logger.info('网易数字注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def j4(tab,browser):
    tab.get('https://www.amishow.com/register')
    ele = tab.ele('css=body > div.content.clearfix > div > div > div > form > div:nth-child(3) > input')
    ele.input(phonenum)

    tab.listen.start(targets='https://www.amishow.com/register_verify')
    ele = tab.ele('css=body > div.content.clearfix > div > div > div > form > div:nth-child(4) > button:nth-child(3)')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----跨境{masked_phone}----：{res}')
    except:
        logger.info('跨境注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器
def a5(tab, browser):
    tab.get('https://www.acfun.cn/reg/')

    ele = tab.ele('css=#reg > div.reg-container > div > div.reg-form-wrapper > form > div:nth-child(1) > span > input')

    ele.input(phonenum)
    tab.listen.start(targets='/sms/send')
    ele = tab.ele(
        'css=#reg > div.reg-container > div > div.reg-form-wrapper > form > div:nth-child(4) > span > div.ac-input-suffix-item > span')
    time.sleep(1)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----acfun{masked_phone}----：{res}')
    except:
        logger.info('acfun注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器


def b5(tab, browser):
    tab.get('https://www.imathtool.com/huaban')
    ele = tab.ele('css=#__layout > div > div.page > header > div > div.headerright > div.userInfo > div.login-btn')
    ele.click()
    ele = tab.ele(
        'css=#__layout > div > div.ui-dialog > div > div > div.dialogs-login > div.login-right > div.other-login > div.other-login-type > div:nth-child(2) > div:nth-child(1)')
    ele.click()
    ele = tab.ele(
        'css=#__layout > div > div.ui-dialog > div > div > div.dialogs-login > div.login-right > div.login-phone > div.sj-input-outer > input')

    ele.input(phonenum)
    tab.listen.start(targets='/sms')
    ele = tab.ele(
        'css=#__layout > div > div.ui-dialog > div > div > div.dialogs-login > div.login-right > div.login-phone > div.input-box.yzm-input-outer > div.input-outer > span')
    time.sleep(1)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----mathtool{masked_phone}----：{res}')
    except:
        logger.info('mathtool注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def c5(tab, browser):
    tab.get('https://baoyueai.com/channel?utm_id=219781#6')

    ele = tab.ele('css=#__next > div > div > div.header > div > div.user_user-box__S0gjJ > div > button')
    ele.click()

    ele = tab.ele(
        'css=body > div:nth-child(6) > div > div.ant-modal-wrap > div > div:nth-child(2) > div > div > div > div.login-row-right > div.other > div.list > div:nth-child(2)')
    ele.click()
    ele = tab.ele(
        'css=body > div:nth-child(6) > div > div.ant-modal-wrap > div > div:nth-child(2) > div > div > div > div.login-row-right > div.form > div:nth-child(2) > div > input')

    ele.input(phonenum)

    tab.listen.start(targets='https://base-api.baoyueai.com/v1/user/sms/login-code')
    ele = tab.ele(
        'css=body > div:nth-child(6) > div > div.ant-modal-wrap > div > div:nth-child(2) > div > div > div > div.login-row-right > div.form > div:nth-child(3) > div > button')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----包月ai{masked_phone}----：{res}')
    except:
        logger.info('包月ai注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def d5(tab, browser):
    tab.get('https://www.cotticoffee.com/cooperation/#express')

    ele = tab.ele('text=获取')
    #logger.info(ele)
    sendele = ele
    ele = ele.parent().parent().parent().parent().prev().child()
    #logger.info(ele)
    tab.listen.start(targets='/smsCode')
    ele.input(phonenum)
    time.sleep(1)
    sendele.click()
    try:
        res = tab.listen.wait(timeout=15).response
        res = res.body
        logger.info(f'----库迪{masked_phone}----：{res}')
    except:
        logger.info('库迪注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def e5(tab, browser):
    tab.get('https://qingtu.co/login')

    ele = tab.ele(
        'css=#login-page-app > div > div > div.login-form > div.login-fields-wrapper > div.login-row > div > input')

    ele.input(phonenum)
    tab.listen.start(targets='/reg_code')
    ele = tab.ele(
        'css=#login-page-app > div > div > div.login-form > div.login-fields-wrapper > div.login-row > div > button')
    time.sleep(1)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----氢图{masked_phone}----：{res}')
    except:
        logger.info('氢图注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def f5(tab, browser):
    tab.get('https://flowus.cn/product')
    ele = tab.ele(
        r'css=#__next > div > div > div > header > div.fixed.w-full.flex.justify-between.items-center.px-12.header-sm\:hidden.h-\[80px\].duration-150.transition-all.bg-white.text-black.border-grey6.top-0 > div:nth-child(5) > span')
    ele.click()
    ele = tab.ele(
        r'css=#__next > div > div > div > div > div > div.fixed.top-1\/2.left-1\/2.-translate-x-1\/2.-translate-y-1\/2.modal-item-fade-enter-done > div > div > div.mt-5 > div > div:nth-child(3) > div.text-t1.mt-3.flex.cursor-pointer.justify-center')
    ele.click()
    time.sleep(1)
    ele = tab.ele(
        r'css=#__next > div > div > div > div > div > div.fixed.top-1\/2.left-1\/2.-translate-x-1\/2.-translate-y-1\/2.modal-item-fade-enter-done > div > div > div.mt-5 > div > div.w-full > div.sm\:px5 > div > input')
    ele.input(phonenum)
    tab.listen.start(targets='/captchas')
    ele = tab.ele(
        r'css=#__next > div > div > div > div > div > div.fixed.top-1\/2.left-1\/2.-translate-x-1\/2.-translate-y-1\/2.modal-item-fade-enter-done > div > div > div.mt-5 > div > div.w-full > div.sm\:px5 > button')
    time.sleep(2)
    ele.click(by_js=True)

    try:
        res = tab.listen.wait(timeout=15).response
        res = res.body
        logger.info(f'----溪流{masked_phone}----：{res}')
    except:
        logger.info('溪流注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def g5(tab, browser):
    tab.get('https://49pic.com/?ref=pidoutv.com')

    ele = tab.ele('css=#ieblock > div.associated-logon > div.no-login > a')
    ele.click()
    ele = tab.ele(
        'css=#log-link-window > div.log-link-window-right.vipback-right > div.log-link > a.qq-login-href.phone')
    #logger.info(ele)
    ele.click(by_js=True)
    time.sleep(1)
    ele = tab.ele('css=#phone-number')

    ele.input(phonenum)

    tab.listen.start(targets='https://49pic.com/user/captcha')
    ele = tab.ele('css=#yan-code')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----演图网{masked_phone}----：{res}')
    except:
        logger.info('演图网注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def h5(tab, browser):
    tab.get('https://ibiling.cn/template?from=xy01&ref=pidoutv.com')

    ele = tab.ele(
        'css=#__next > div.lingo-row.lingo-row-no-wrap.lingo-row-space-between.lingo-row-middle.Header_header_wrapper__kQnKg > div.LoginAndReg_login__eOMme > b')
    ele.click()

    ele = tab.ele('text=手机号登录')
    #logger.info(ele)
    ele.click()
    time.sleep(1)
    ele = tab.ele('css=#normal_login_phone')

    ele.input(phonenum)

    tab.listen.start(targets='https://api.ibiling.cn/captcha/send-phone-code')
    ele = tab.ele(
        'css=#normal_login > div.lingo-row.lingo-row-space-between.PhoneLogin_get_yzm__GOSLT > div:nth-child(2) > button')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----笔灵ai{masked_phone}----：{res}')
    except:
        logger.info('笔灵ai注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def i5(tab, browser):
    tab.get('https://www.doudou.fun/?channel=web_aitool18&ref=pidoutv.com')
    ele = tab.ele('css=#__nuxt > div.app-header.pc-header > div > div.header-right > div:nth-child(6) > div > span')
    ele.click()
    ele = tab.ele(
        'css=#__nuxt > div.app-header.pc-header > div > div.login-dialog-mask > div > div.dialog-content > form > div:nth-child(1) > div.el-form-item__content')
    ele = ele.child().child().child()
    #logger.info(ele)
    ele.input(phonenum)

    tab.listen.start(targets='/send_phone_verification_code')
    ele = tab.ele(
        'css=#__nuxt > div.app-header.pc-header > div > div.login-dialog-mask > div > div.dialog-content > form > div:nth-child(2) > div.el-form-item__content > div > div > span > span > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----豆豆游戏{masked_phone}----：{res}')
    except:
        logger.info('豆豆游戏注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def j5(tab, browser):
    tab.get('https://www.wenxiaobai.com/chat/tourist?forceLogin=true&source=pidoutv&ad_source=pidoutv&ref=pidoutv.com')
    tab.listen.start(targets='https://api-bj.wenxiaobai.com/api/v1.0/user/codes')
    sendele = tab.ele('text=获取验证码')
    ele = sendele.parent().parent().parent().prev().child().child()
    #logger.info(ele)
    ele.input(phonenum)
    time.sleep(2)
    sendele.click()
    
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----问小白----：{res}')
    except:
        logger.info('问小白注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器
def a6(tab, browser):
    tab.get('https://www.jiuma.com/liverecording')

    ele = tab.ele('css=body > div.topbar > div > div.topbar-right > div.login > a')
    ele.click()

    time.sleep(1)
    ele = tab.ele('css=body > div.log-reg-modal > div > div.phone-msgnumber-login > input')

    ele.input(phonenum)

    tab.listen.start(targets='sendSmsCode')
    ele = tab.ele('css=body > div.log-reg-modal > div > div.phone-msgnumber-login > div.verify > button')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----九马{masked_phone}----：{res}')
    except:
        logger.info('九马注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def b6(tab, browser):
    tab.get('https://www.dcbbs.com/reg.aspx')

    ele = tab.ele('css=#Content_txtMobile')

    ele.input(phonenum)

    tab.listen.start(targets='/GetUserSMSCode')

    ele = tab.ele('css=#spansend')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----柏测{masked_phone}----：{res}')
    except:
        logger.info('柏测注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def c6(tab, browser):
    tab.get('https://www.talk-fun.com/')
    try:
        ele = tab.ele('css=body > header > div.popup_bg > div > div.popup_close')
        ele.click()
    except:
        pass
    ele = tab.ele('css=body > header > div.header_container > div.header_trila.free_pop > span')
    ele.click()

    time.sleep(1)
    eles = tab.eles('css=#phone')

    ele = eles[2]
    ele.input(phonenum)
    tab.listen.start(targets='/sms/send')
    eles = tab.eles('css=#captcha')

    ele = eles[1]
    ele.input('aaaa')
    ele.click()
    ele = tab.ele('css=body > div > div.register-container-r > div.center > form > div.code > div > span')
    time.sleep(2)
    ele.click(by_js=True)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----欢拓云{masked_phone}----：{res}')
    except:
        logger.info('欢拓云注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def d6(tab, browser):
    tab.get('https://www.eventwang.cn/')
    ele = tab.ele('css=#container_big_home > div > div > div.header_right > div.avatar.head_right > span')
    ele.click()
    ele = tab.ele(
        'css=body > div.user_login_content > div.el-dialog__wrapper.login_el_dialog > div > div.el-dialog__body > div > div.login_right_cont > div.login_nav1 > div.chk_login.login_check_center.mt28 > div.login_phone > span')
    ele.click()
    time.sleep(1)
    ele = tab.ele(
        'css=body > div.user_login_content > div.el-dialog__wrapper.login_el_dialog > div > div.el-dialog__body > div > div.login_right_cont > div:nth-child(2) > div.login_tabs > div > div:nth-child(2)')
    ele.click()
    time.sleep(1)
    ele = tab.ele(
        'css=body > div.user_login_content > div.el-dialog__wrapper.login_el_dialog > div > div.el-dialog__body > div > div.login_right_cont > div:nth-child(2) > div.regist_cont > div.login_option > div:nth-child(1) > input.pl0')
    ele.input(phonenum)
    tab.listen.start(targets='/getRegistMobileVerify')
    ele = ele.parent().next().child()
    #logger.info(ele)
    ele.click()
    ele = tab.ele(
        'css=body > div.user_login_content > div.el-dialog__wrapper.login_el_dialog > div > div.el-dialog__body > div > div.login_right_cont > div:nth-child(2) > div.regist_cont > div.login_option > div.input_cont_code.mb16 > button')
    time.sleep(2)

    ele.click(by_js=True)
    time.sleep(2)
    try:
        ele.click(by_js=True)
    except:
        pass

    try:
        res = tab.listen.wait(timeout=15).response
        res = res.body
        logger.info(f'----活动汪{masked_phone}----：{res}')
    except:
        logger.info('活动汪注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def e6(tab, browser):
    tab.get('https://www.paikev.com/register.html')

    ele = tab.ele('css=#mobile')

    ele.input(phonenum)
    tab.listen.start(targets='https://www.paikev.com/sendcode.html')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#sendcode')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----派克配音{masked_phone}----：{res}')
    except:
        logger.info('派克配音注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def f6(tab, browser):
    tab.get('https://www.001ppt.com/')
    ele = tab.ele('css=#__layout > div > div.header-container > div > div > div.user-state-item')
    ele = ele.click()
    time.sleep(2)
    ele = tab.ele(
        'css=#__layout > div > div:nth-child(4) > div > div.login > div.login-container > div.login-box > div.login-box-header > div.login-box-header-icon.absolute > img')
    ele.click()
    ele = tab.ele(
        'css=#__layout > div > div:nth-child(4) > div > div.login > div.login-container > div.login-box > div.login-box-body > div:nth-child(1) > div.login-register.custom-el-input.custom-el-checkbox > form > div:nth-child(1) > div > div > div.el-input > input')

    ele.input(phonenum)
    tab.listen.start(targets='sendValidateCode')
    ele = tab.ele(
        'css=#__layout > div > div:nth-child(4) > div > div.login > div.login-container > div.login-box > div.login-box-body > div:nth-child(1) > div.login-register.custom-el-input.custom-el-checkbox > form > div:nth-child(2) > div > div > div.verify-code-btn')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----灵感严选{masked_phone}----：{res}')
    except:
        logger.info('灵感严选注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def g6(tab, browser):
    tab.get('https://pdfjm.com/?ref=pidoutv.com#/login/register')

    ele = tab.ele(
        'css=#app > div > div > div.form-container-view.flex-column-center.form-view-box.ml100 > div.ps-box.flex-column-center.pt42.pb42 > div.form-main > div > div.form-container > div:nth-child(1) > div > input[type=text]')

    ele.input(phonenum)
    tab.listen.start(targets='/sendsms/index')
    ele = tab.ele(
        'css=#app > div > div > div.form-container-view.flex-column-center.form-view-box.ml100 > div.ps-box.flex-column-center.pt42.pb42 > div.form-main > div > div.form-container > div:nth-child(2) > div > span')
    time.sleep(1)
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----笔熊{masked_phone}----：{res}')
    except:
        logger.info('笔熊注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def h6(tab, browser):
    tab.get('https://uc.mk.metcom.com.cn/orga-register/meike')

    ele = tab.ele('css=#register_name')
    ele.input('雷军')

    time.sleep(1)
    ele = tab.ele('css=#register_phone')

    ele.input(phonenum)

    tab.listen.start(targets='/registration')

    ele = tab.ele(
        'css=#register > div.ant-form-item.tCaptcha-item > div > div.ant-col.ant-col-18.ant-form-item-control > div > div > div > div.ant-col.ant-col-6.ant-col-offset-1.tCaptchabtn-col > button > span')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----美即云{masked_phone}----：{res}')
    except:
        logger.info('美即云注册失败')
        res = {"statusCode": -1}

    browser.quit()  # 关闭浏览器


def i6(tab, browser):
    tab.get('https://sou-yun.cn/login.aspx')
    ele = tab.ele('css=body > div.dynamic-tab-pane-control.tab-pane > div.tab-row > span:nth-child(2) > a')
    ele.click()
    time.sleep(1)
    ele = tab.ele('css=#phone')
    ele.input(phonenum)
    tab.listen.start(targets='sendCode')
    ele = tab.ele('css=#sendCode')
    time.sleep(2)
    ele.click()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----诗词{masked_phone}----：{res}')
    except:
        logger.info('诗词注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器


def j6(tab, browser):
    tab.get('https://sdocapp.com/sign')
    ele = tab.ele('css=#phone')
    ele.input(phonenum)

    ele = tab.ele('css=#app > div > div > div.sc-dZoequ.cpvRqw > div > div > form > div.rs-form-group > div > button')
    ele.click()

    time.sleep(1)
    ele = tab.ele(
        'css=#app > div > div > div.sc-dZoequ.cpvRqw > div > div > form > div.sc-bkEOxz.epqYyl > div > div:nth-child(1) > div > button')
    ele.click()

    time.sleep(2)

    logger.info(f'----超级文档{masked_phone}----：{ele.text}')

    browser.quit()  # 关闭浏览器
def a7(tab, browser):
  tab.get('https://www.yiihuu.com/?ref=pidoutv.com')
  ele = tab.ele('css=#gp-closeBtn')
  ele.click()
  ele = tab.ele('css=#home > div.header-content > div.header-wrap-bg > div > div.header-info-wrap > div.header-info-login > div > span.register')
  ele.click()
  ele = tab.ele('css=#J_phone')
  
  ele.input(phonenum)
  tab.listen.start(targets='https://passport.yiihuu.com/js-api.php')
  ele = tab.ele('css=body > div.login-wrap > div.login.clearfixa > div.login-left_box > div.login_Type > div.loginType_dx > label.clearfixa > span')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----翼虎{masked_phone}----：{res}')
  except:
      logger.info('翼虎注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def b7(tab, browser):
  tab.get('https://account.kaola.com/login.html')
  ele = tab.ele('css=#index-netease-com > div.kl-account.kl-account_pc-modal.kl-account_pc-proto2 > table > tbody > tr > td > div > div > div > div > footer > div > button.agree-proto')
  ele.click()
  ele = tab.ele('css=#login > div.corner-icon-view.view-type-sms > i')
  ele.click()
  ele = tab.ele('css=#fm-sms-login-id')
  
  ele.input(phonenum)
  tab.listen.start(targets='send.do')
  ele = tab.ele('css=#login-form > div.fm-field.fm-field-sms > div.send-btn > a')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----考拉{masked_phone}----：{res}')
  except:
      logger.info('考拉注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def c7(tab, browser):
  tab.get('https://www.heimaohui.com/register')
  ele = tab.ele('text=+86')
  ele = ele.parent().next()
  ele.input(phonenum)
  tab.listen.start(targets='/sendCaptcha')
  ele = tab.ele('css=#app > div > div > div.mainBox.greenBgColor > div:nth-child(2) > div.content > form > div:nth-child(2) > div > div > span > span > span > span > span')
  time.sleep(2)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----黑猫会{masked_phone}----：{res}')
  except:
      logger.info('黑猫会注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def d7(tab, browser):
  tab.get('https://www.3cccy.com/register')
  
  ele = tab.ele('css=#phoneInp')
  
  ele.input(phonenum)
  tab.listen.start(targets='register_phone_send')
  ele = tab.ele('css=#phone > form > div:nth-child(3) > div > div > button')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----3C云{masked_phone}----：{res}')
  except:
      logger.info('3C云注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def e7(tab, browser):
  tab.get('https://home.jcloud.sjtu.edu.cn/register/')
  
  ele = tab.ele('css=#phone')
  
  ele.input(phonenum)
  tab.listen.start(targets='/captcha/')
  ele = tab.ele('css=#captcha > div > div')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----交大云{masked_phone}----：{res}')
  except:
      logger.info('交大云注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def f7(tab, browser):
  tab.get('https://cloud.bemfa.com/web/user/index/?r=https://cloud.bemfa.com/tcp/index.html')
  ele = tab.ele('css=#app > main > div:nth-child(2) > div:nth-child(1) > div.v-window.v-theme--light > div > div.v-window-item.v-window-item--active > div > div:nth-child(1) > p:nth-child(4)')
  ele.click()
  ele = tab.ele('css=#input-18')
  
  ele.input(phonenum)
  tab.listen.start(targets='/loginCode')
  ele = tab.ele('css=#app > main > div:nth-child(2) > div:nth-child(1) > div.v-window.v-theme--light > div > div.v-window-item.v-window-item--active > div > div:nth-child(1) > div.v-input.v-input--horizontal.v-input--center-affix.v-input--density-default.v-theme--light.v-locale--is-ltr.v-text-field > div.v-input__append > button > span.v-btn__content')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----八法云----：{res}')
  except:
      logger.info('八法云注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def g7(tab, browser):
  tab.get('https://www.youyan3d.com/login')
  ele = tab.ele('css=#__nuxt > div > div > div.exposed.overflow-y-auto.overflow-x-auto > div > div > div.content-right.relative.justify-center.flex-1.flex-y-center > div > div.login-mode-switcher > iconpark-icon')
  sr_ele = ele.shadow_root
  ele = sr_ele.ele('css=svg')
  #logger.info(ele)
  ele.click()
  
  ele = tab.ele('css=#basic_mobile')
  
  ele.input(phonenum)
  tab.listen.start(targets='send_sms_code')
  ele = tab.ele('css=#basic_remember')
  
  ele.click()
  ele = tab.ele('css=#__nuxt > div > div > div.exposed.overflow-y-auto.overflow-x-auto > div > div > div.content-right.relative.justify-center.flex-1.flex-y-center > div > div.login-form > form > div:nth-child(2) > div > div > div > div > div > button > span')
  time.sleep(1)
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----有言{masked_phone}----：{res}')
  except:
      logger.info('有言注册失败')
      res = {"statusCode": -1}


  browser.quit()  # 关闭浏览器


def h7(tab, browser):
  tab.get('https://ylqx.qgyyzs.net/business/registerinfo.asp')
  
  ele = tab.ele('css=#Mobile')
  ele.input(phonenum)
  tab.listen.start(targets='/SendSmsYzm')
  time.sleep(1)
  ele = tab.ele('css=#sendbutton')
  #logger.info(ele.text)
  ele.click(by_js=True)
  time.sleep(1)
  buttonele = tab.ele('css=#slider > div > div > div > i')
  #sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
  
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----环球医疗{masked_phone}----：{res}')
  except:
      logger.info('环球医疗注册失败')
      res = {'msg': '-1'}


  browser.quit()  # 关闭浏览器


def i7(tab, browser):
  tab.get('https://www.zuiyouliao.com/main/Reg')
  
  ele = tab.ele('css=#Reg > div.main-box.bgwhite > div > div.reg-box > form > div:nth-child(1) > div > div > input')
  
  ele.input(phonenum)
  tab.listen.start(targets='/sendCode')
  ele = tab.ele('css=#Reg > div.main-box.bgwhite > div > div.reg-box > form > div:nth-child(3) > div > button > span')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----最有料{masked_phone}----：{res}')
  except:
      logger.info('最有料注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def j7(tab, browser):
  tab.get('https://www.cttamsc.cn/register')
  
  
  ele = tab.ele('css=#register_form_telephone')
  
  ele.input(phonenum)
  tab.listen.start(targets='/sendMsg')
  ele = tab.ele('css=body > div.app-box > div > div > div > div > div > div.content > div > div > div > div > form > div:nth-child(2) > div > div > span > span > span > span.ant-input-group-addon > button')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----乒协{masked_phone}----：{res}')
  except:
      logger.info('乒协注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器

def a8(tab, browser):
    #0网址
    url = 'https://www.renrendoc.com/renrendoc_v1/User/reg.html'
    #1输入手机号
    phonee = 'css=' + '#Content_txtMobile'
    #2图片验证码ele
    imge = 'css=' + '#captcha'
    #3验证码输入框ele
    inpute = 'css=' + '#Content_PicCode'
    #4发送短信按钮
    sende = 'css=' + '#spansend'
    range = 6
    picname = 'ysw.png'
    #5监听端口
    target = 'sendCode.html'
    #res = {"result": False}
    #成功res
    resleft = 'code'
    resright = 200
    name = '人人文库'
    
    
    
    def char(imgele,inputele,sendele,range,picname):
        inputele.clear()
        imgele.click()
        time.sleep(1)
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        #logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click(by_js=True)
    
    tab.get(url)
    phoneele = tab.ele(phonee)
    phoneele.click()
    phoneele.input(phonenum)
    
    imgele = tab.ele(imge)
    inputele = tab.ele(inpute)
    sendele = tab.ele(sende)
    sendele.click()
    tab.listen.start(targets=target)
    char(imgele,inputele,sendele,range,picname)
    res = {}
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----{name}{masked_phone}----：{res}')
    except:
        logger.info(f'{name}注册失败')
        res[resleft] = 11
    
    
    attempts = 0
    
    while res[resleft] != resright:
        tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele,inputele,sendele,range,picname)
    
        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----{name}{masked_phone}----：{res}')
        except:
            logger.info(f'{name}注册失败')
            res[resleft] = 11
        attempts += 1
        if attempts == 5:
            logger.info(f'{name}5次错误')
            break
    browser.quit()  # 关闭浏览器


def b8(tab, browser):
    url = 'https://gapc.com.cn/register_ps.aspx'
    phoneele = 'css=' + '#mobile'
    sendele = 'css=' + '#form1 > div.loginbox.clearfix > div.check_form > div > div:nth-child(11) > div.code'
    target = '/submit_ajax.ashx'
    name = '广州心理协会'
    
    tab.get(url)
    ele = tab.ele(phoneele)
    ele.input(phonenum)
    ele = tab.ele(sendele)
    tab.listen.start(targets=target)
    ele.click()
    
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----{name}{masked_phone}----：{res}')
    except:
        logger.info(f'{name}注册失败')
        res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器


def c8(tab, browser):
    tab.get('https://passport.fanli.com/reg?action=yes&go_url=https%3A%2F%2Fwww.fanli.com')

    ele = tab.ele('css=#J_reg_img_box > div.reg-info-r.clearfix > div > img')
    ele.get_screenshot(name='fanli.png')
    # bytes_str = ele.get_screenshot(as_bytes='png')  # 返回截图二进制文本
    ele = tab.ele('css=#J_reg_tel_number')
    ele.input(phonenum)
    ele = tab.ele('css=#J_reg_img_code')
    ocr = ddddocr.DdddOcr(show_ad=False)
    image = open("fanli.png", "rb").read()
    ocr.set_ranges(6)
    result = ocr.classification(image, probability=True)
    s = ""
    for i in result['probability']:
        s += result['charsets'][i.index(max(i))]

    # logger.info(s)
    ele.input(s)
    tab.listen.start(targets='https://passport.fanli.com')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#J_reg_get_ver')
    ele.click()
    res = tab.listen.wait(timeout=30).response
    res = res.body
    # logger.info(res)

    # 提取 `{}` 部分
    json_str = res

    # 使用正则提取 JSON 部分
    match = re.search(r'\((\{.*\})\)', json_str)

    if match:
        json_str = match.group(1)  # 提取 JSON 字符串
        json_data = json.loads(json_str)  # 解析 JSON
        status_value = json_data.get("status")
        # logger.info("status:", status_value)
    else:
        logger.info("未找到 JSON 数据")
    if int(status_value) == 1:
        logger.info(f'----返利网{masked_phone}---- ：{res}')
    againtimes = 0
    while int(status_value) != 1:
        ele = tab.ele('css=#J_reg_img_box > div.reg-info-r.clearfix > div > img')
        ele.click()
        ele.get_screenshot(name='fanli.png')
        # bytes_str = ele.get_screenshot(as_bytes='png')  # 返回截图二进制文本
        ele = tab.ele('css=#J_reg_tel_number')
        ele.input(phonenum)
        ele = tab.ele('css=#J_reg_img_code')
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open("fanli.png", "rb").read()
        ocr.set_ranges(6)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]

        # logger.info(s)
        ele.input(s)
        tab.listen.start(targets='https://passport.fanli.com')  # 开始监听，指定获取包含该文本的数据包
        ele = tab.ele('css=#J_reg_get_ver')
        ele.click()
        res = tab.listen.wait(timeout=30).response
        res = res.body
        # logger.info(res)

        # 提取 `{}` 部分
        json_str = res

        # 使用正则提取 JSON 部分
        match = re.search(r'\((\{.*\})\)', json_str)

        if match:
            json_str = match.group(1)  # 提取 JSON 字符串
            json_data = json.loads(json_str)  # 解析 JSON
            status_value = json_data.get("status")
            # logger.info("status:", status_value)
        else:
            logger.info("未找到 JSON 数据")
        if int(status_value) == 1:
            logger.info(f'----返利网{masked_phone}---- ：{res}')
        againtimes = againtimes + 1
        if againtimes == 5:
            logger.info('返利网5次验证码错误')
            break;
    # 文件路径
    file_path = 'fanli.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def d8(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        #logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://account.lifevc.com/Account/Register')

    ele = tab.ele('css=#inpMobile')
    ele.input(phonenum)
    tab.listen.start(targets='https://account.lifevc.com/account/SendRegisterSmsVerifyCode')  # 开始监听，指定获取包含该文本的数据包

    imgele = tab.ele('css=#verifyCodeV2')
    inputele = tab.ele('css=#validation')
    sendele = tab.ele('css=#registerLayer2 > div > div.tab_form > div > ul > li:nth-child(4) > span')
    char(imgele, inputele, sendele, 6, 'lfjj.png')

    # ele = tab.ele('css=#registerLayer2 > div > div.tab_form > div > ul > li:nth-child(4) > span')

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----丽芙家居{masked_phone}----：{res}')
    except:
        logger.info('丽芙家居注册失败')
        res = {"Status": 2}

    attempts = 0
    while res['Status'] != 1:
        tab.listen.start(targets='https://account.lifevc.com/account/SendRegisterSmsVerifyCode')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, 6, 'lfjj.png')

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----丽芙家居{masked_phone}----：{res}')
        except:
            logger.info('丽芙家居注册失败')
            res = {"Status": 2}
        attempts += 1
        if attempts == 5:
            logger.info('丽芙家居5次错误')
            break
    # 文件路径
    file_path = 'lfjj.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def e8(tab, browser):
    def char(imgele, ele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        ele.clear()
        ele.input(s)

    tab.get('https://passport.qyer.com/register/mobile?ref=https%3A%2F%2Fwww.qyer.com%2F')
    ele = tab.ele(
        'css=#app > div > div.q-container > div > div.login-wrapper > div.login-section > div > div.q-login-form > div:nth-child(1) > div.input-group > input')
    ele.input(phonenum)
    tab.listen.start(targets='/register/mobile/')  # 开始监听，指定获取包含该文本的数据包
    imgele = tab.ele(
        'css=#app > div > div.q-container > div > div.login-wrapper > div.login-section > div > div.q-login-form > div:nth-child(2) > div.input-group > img')
    ele = tab.ele(
        'css=#app > div > div.q-container > div > div.login-wrapper > div.login-section > div > div.q-login-form > div:nth-child(2) > div.input-group > input')

    char(imgele, ele, 0, 'qiongyou.png')
    ele = tab.ele(
        'css=#app > div > div.q-container > div > div.login-wrapper > div.login-section > div > div.q-login-form > div:nth-child(3) > div.input-group > button > span:nth-child(1)')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----穷游网{masked_phone}----：{res}')
    except:
        logger.info('穷游网注册失败')
        res = {"result": 'error'}

    attempts = 0
    while res['result'] == 'error':
        tab.listen.start(targets='/register/mobile/')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, ele, 0, 'qiongyou.png')
        ele = tab.ele(
            'css=#app > div > div.q-container > div > div.login-wrapper > div.login-section > div > div.q-login-form > div:nth-child(3) > div.input-group > button > span:nth-child(1)')
        ele.click()
        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----穷游网{masked_phone}----：{res}')
        except:
            logger.info('穷游网注册失败')
            res = {"result": 'error'}
        attempts += 1
        if attempts == 5:
            logger.info('穷游网5次错误')
            break
    # 文件路径
    file_path = 'qiongyou.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def f8(tab, browser):
    tab.get('https://maker.haier.net/')
    ele = tab.ele(
        'css=body > div.social_home_box_202206 > div.top_video_box > div.social_header.home_header > div.nav_list.cb-f-r > span.action_btns > a:nth-child(2)')
    ele.click()
    ele = tab.ele(
        'css=body > div:nth-child(18) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > a')
    ele.click()
    ele = tab.ele('css=#userName')
    ele.input(phonenum)
    tab.listen.start(targets='sendVerifyCode')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#code > img')
    ele.get_screenshot(name='haier.png')
    bytes_str = ele.get_screenshot(as_bytes='png')  # 返回截图二进制文本
    ocr = ddddocr.DdddOcr(show_ad=False)
    image = open("haier.png", "rb").read()
    ocr.set_ranges(3)
    result = ocr.classification(image, probability=True)
    s = ""
    for i in result['probability']:
        s += result['charsets'][i.index(max(i))]
    #logger.info(s)
    ele = tab.ele('css=#imageCode')

    ele.input(s)
    ele = tab.ele('css=#code > span')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----海尔{masked_phone}----：{res}')
    except:
        logger.info('海尔注册失败')
        res = {'resultMsg': '-1'}

    result_msg = res['resultMsg']
    logger.info(result_msg)  # 输出: success
    attempts = 0
    while result_msg != 'success':
        tab.listen.start(targets='sendVerifyCode')  # 开始监听，指定获取包含该文本的数据包

        ele = tab.ele('css=#code > img')
        ele.click()
        time.sleep(1)
        ele.get_screenshot(name='haier.png')
        bytes_str = ele.get_screenshot(as_bytes='png')  # 返回截图二进制文本
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open("haier.png", "rb").read()
        ocr.set_ranges(3)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        ele = tab.ele('css=#imageCode')
        ele.clear()
        ele.input(s)
        ele = tab.ele('css=#code > span')
        ele.click()
        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----海尔{masked_phone}----：{res}')
        except:
            logger.info('海尔注册失败')
        result_msg = res['resultMsg']
        #logger.info(result_msg)  # 输出: success
        attempts += 1
        if(attempts == 5):
            logger.info('海尔五次错误')
            break
    # 文件路径
    file_path = 'haier.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    browser.quit()  # 关闭浏览器


def g8(tab, browser):
    def __ease_out_expo(sep):
        if sep == 1:
            return 1
        else:
            return 1 - pow(2, -10 * sep)

    def get_slide_track(distance):
        """
        根据滑动距离生成滑动轨迹
        :param distance: 需要滑动的距离
        :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
            x: 已滑动的横向距离
            y: 已滑动的纵向距离, 除起点外, 均为0
            t: 滑动过程消耗的时间, 单位: 毫秒
        """

        if not isinstance(distance, int) or distance < 0:
            raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
        # 初始化轨迹列表
        slide_track = [
            [random.randint(-50, -10), random.randint(-50, -10), 0],
            [0, 0, 0],
        ]
        # 共记录count次滑块位置信息
        count = 30 + int(distance / 2)
        # 初始化滑动时间
        t = random.randint(50, 100)
        # 记录上一次滑动的距离
        _x = 0
        _y = 0
        for i in range(count):
            # 已滑动的横向距离
            x = round(__ease_out_expo(i / count) * distance)
            # 滑动过程消耗的时间
            t += random.randint(10, 20)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        del slide_track[0]
        del slide_track[0]
        return slide_track

    tab.get('https://erp.abiz.com/register?source=&mobile=')
    ele = tab.ele('css=#mobilePhone')
    ele.input(phonenum)
    tab.listen.start(targets='sendMobileCodeV2')  # 开始监听，指定获取包含该文本的数据包

    ele = tab.ele('css=#sendMobileCode')
    ele.click()
    time.sleep(2)
    ele = tab.ele('css=#fcaptchaBackImgDiv > img')
    ele.save(name='bd_background.png', rename=False)

    ele = tab.ele(
        'css=#fcaptchaDiv > div > div > div.fcaptcha-verifybox-bottom > div > div.fcaptcha-verify-bar-area > div > div > div > img')
    ele.save(name='bd_slider.png', rename=False)

    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('bd_background.png', 'rb') as f:
        background_bytes = f.read()
    with open('bd_slider.png', 'rb') as f:
        target_bytes = f.read()
    result = det.slide_match(target_bytes, background_bytes)

    # logger.info(result)
    distance = result["target"][0]
    tab.actions.hold(
        'css:#fcaptchaDiv > div > div > div.fcaptcha-verifybox-bottom > div > div.fcaptcha-verify-bar-area > div > div')
    temp_track = 0
    temp_time = 0
    for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
        now_track = track[0] - temp_track
        now_time = track[2] - temp_time
        tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
        # logger.info("now_track:", now_track)
        # time.sleep(track[2]/1000)
        # logger.info("now_time:", now_time / 1000)
        temp_track = track[0]
        temp_time = track[2]
    tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    time.sleep(0.1)
    tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    time.sleep(0.1)
    tab.actions.release()

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----百卓{masked_phone}----：{res}')
    except:
        logger.info('百卓注册失败')
        res = {'retCode': '-1'}
    attempts = 0
    while res['retCode'] != '0':
        ele = tab.ele(
            'css=#fcaptchaDiv > div > div > div.fcaptcha-verifybox-bottom > div > div.fcaptcha-verify-img-out > div > div.fcaptcha-verify-refresh')
        ele.click()
        tab.listen.start(targets='sendMobileCodeV2')  # 开始监听，指定获取包含该文本的数据包

        time.sleep(2)
        ele = tab.ele('css=#fcaptchaBackImgDiv > img')
        ele.save(name='bd_background.png', rename=False)

        ele = tab.ele(
            'css=#fcaptchaDiv > div > div > div.fcaptcha-verifybox-bottom > div > div.fcaptcha-verify-bar-area > div > div > div > img')
        ele.save(name='bd_slider.png', rename=False)

        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        with open('bd_background.png', 'rb') as f:
            background_bytes = f.read()
        with open('bd_slider.png', 'rb') as f:
            target_bytes = f.read()
        result = det.slide_match(target_bytes, background_bytes)

        # logger.info(result)
        distance = result["target"][0]
        tab.actions.hold(
            'css:#fcaptchaDiv > div > div > div.fcaptcha-verifybox-bottom > div > div.fcaptcha-verify-bar-area > div > div')
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----百卓{masked_phone}----：{res}')
        except:
            logger.info('百卓注册失败')
            res = {'retCode': '-1'}

        attempts += 1
        if attempts == 5:
            logger.info('百卓错误5次')
            break

    # 文件路径
    file_path = 'bd_slider.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    file_path = 'bd_background.pn'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass


    browser.quit()  # 关闭浏览器


def h8(tab, browser):
    def base64_to_image(base64_string, image_path):
        base64_data = base64_string.encode("utf-8")
        image_data = base64.b64decode(base64_data)
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

    def slide(ele):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        distance = result["target"][0]
        # logger.info(distance)
        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()

    tab.set.when_download_file_exists('overwrite')
    tab.get('https://www.guhai.com.cn/register.html')
    ele = tab.ele('css=#mobile')
    ele.input(phonenum)

    ele = tab.ele(
        'css=#captcha > div > div.geetest_btn > div.geetest_radar_btn > div.geetest_radar_tip > span.geetest_radar_tip_content',
        timeout=30)
    tab.listen.start(targets='/slice/')  # 开始监听，指定获取包含该文本的数据包
    ele.click()
    time.sleep(1)

    res = tab.listen.wait(timeout=10).response
    # logger.info(res.url)
    url = res.url
    file_name = os.path.basename(url)
    # logger.info(file_name)
    tab.download(res.url)

    # ele = tab.ele('css=body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_div_img.geetest_absolute > div.geetest_slicebg.geetest_absolute > div.geetest_div_bg.geetest_absolute')
    # ele.get_screenshot(name='guhai.png')
    ele = tab.ele(
        'css=body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute')
    background = ele.run_js("return arguments[0].toDataURL('image/png').substring(21);", ele)
    base64_to_image(background, 'guhai_background.png')
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open(file_name, 'rb') as f:
        target_bytes = f.read()
    with open('guhai_background.png', 'rb') as f:
        background_bytes = f.read()

    result = det.slide_match(target_bytes, background_bytes)

    # logger.info(f"ddddres:{result}")

    ele = tab.ele(
        'css=body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_slider.geetest_ready > div.geetest_slider_button')
    slide(ele)
    time.sleep(3)
    tab.listen.start(targets='/sendsmscodepc')  # 开始监听，指定获取包含该文本的数据包
    ele = tab.ele('css=#smsCodeBtn')
    ele.click()
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----股海{masked_phone}----：{res}')
    except:
        logger.info('股海注册失败')
        res = {'msg': '-1'}

    # 文件路径
    file_path = file_name
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    # 文件路径
    file_path = 'guhai_background.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    browser.quit()  # 关闭浏览器


def i8(tab, browser):
    def slide(ele, result):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        distance = result["target"][0] + 12
        #logger.info(distance)
        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()

    tab.set.when_download_file_exists('overwrite')
    tab.get('https://daas.todesk.com/console/#/login?redirect=%2FdesktopControl&registryChannel=web')

    ele = tab.ele('css=#phone#phone')
    ele.input(phonenum)

    ele = tab.ele('css=#loginFrom > div.form-item-cont.message > form > div:nth-child(2) > div > div.sendMsg > p')
    ele.click()
    time.sleep(1)
    ele = tab.ele('css=#img')
    ele.save(name='todesk_background.png', rename=False)
    ele = tab.ele('css=#app > section > div > div > div.vue-slider-captcha > div.vue-slider-captcha-panel > div > img')
    ele.save(name='todesk_slide.png', rename=False)
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    with open('todesk_background.png', 'rb') as f:
        background_bytes = f.read()
    with open('todesk_slide.png', 'rb') as f:
        target_bytes = f.read()
    result = det.slide_match(target_bytes, background_bytes)
    ele = tab.ele(
        'css=#app > section > div > div > div.vue-slider-captcha > div.vue-slider-captcha-control > div.vue-slider-captcha-slider > i')
    tab.listen.start(targets='/getphonecode')  # 开始监听，指定获取包含该文本的数据包
    slide(ele, result)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----todesk{masked_phone}----：{res}')
    except:
        logger.info('todesk注册失败')
        res = {"statusCode": -1}

    attempts = 0
    while res['statusCode'] != 200:
        time.sleep(1)
        ele = tab.ele('css=#img')
        ele.save(name='todesk_background.png', rename=False)
        ele = tab.ele(
            'css=#app > section > div > div > div.vue-slider-captcha > div.vue-slider-captcha-panel > div > img')
        ele.save(name='todesk_slide.png', rename=False)
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        with open('todesk_background.png', 'rb') as f:
            background_bytes = f.read()
        with open('todesk_slide.png', 'rb') as f:
            target_bytes = f.read()
        result = det.slide_match(target_bytes, background_bytes)
        ele = tab.ele(
            'css=#app > section > div > div > div.vue-slider-captcha > div.vue-slider-captcha-control > div.vue-slider-captcha-slider > i')
        tab.listen.start(targets='/getphonecode')  # 开始监听，指定获取包含该文本的数据包
        slide(ele, result)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----todesk{masked_phone}----：{res}')
        except:
            logger.info('todesk注册失败')
            res = {"statusCode": -1}

        attempts += 1
        if attempts == 5:
            logger.info('todesk五次错误')
            break
    # 文件路径
    file_path = 'todesk_background.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    # 文件路径
    file_path = 'todesk_slide.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def j8(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://service.zol.com.cn/user/login.php')
    ele = tab.ele('css=#J_LoginPhone')
    ele.input(phonenum)

    tab.listen.start(targets='quickSendCodeV2')  # 开始监听，指定获取包含该文本的数据包
    time.sleep(1)
    imgele = tab.ele('css=#quickimgverifycode')
    inputele = tab.ele('css=#phoneloginpicverifycode')
    sendele = tab.ele('css=#get-anicode')
    range = 6
    picname = 'zol.png'

    char(imgele, inputele, sendele, range, picname)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----zol{masked_phone}----：{res}')
    except:
        logger.info('zol注册失败')
        res = {"info": 'error'}

    attempts = 0
    while res['info'] != 'ok':
        imgele.click()
        tab.listen.start(targets='quickSendCodeV2')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----zol{masked_phone}----：{res}')
        except:
            logger.info('zol注册失败')
            res = {"info": 'error'}
        attempts += 1
        if attempts == 5:
            logger.info('zol5次错误')
            break
    # 文件路径
    file_path = 'zol.png'
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    browser.quit()  # 关闭浏览器

def a9(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        time.sleep(1)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://www.onezh.com/reg/login.asp')
    ele = tab.ele('css=body > div.login > div.login_R > div.login_R_top > span:nth-child(3)')
    ele.click()
    ele = tab.ele('css=#mobile')
    ele.input(phonenum)
    tab.listen.start(targets='reg')
    imgele = tab.ele('css=#login_staff > div.account > div:nth-child(2) > img')
    inputele = tab.ele('css=#fiCode')
    sendele = tab.ele('css=#gaincode')
    range = 0
    picname = 'hzzx.png'

    char(imgele, inputele, sendele, range, picname)

    try:
        res = tab.listen.wait(timeout=15).response
        res = res.body
        logger.info(f'----第一会展{masked_phone}----：{res}')
    except:
        logger.info('第一会展注册失败')
        res = {"states": '2'}
    time.sleep(1)
    attempts = 0
    while res['states'] != 'ok':
        tab.listen.start(targets='reg')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----第一会展{masked_phone}----：{res}')
        except:
            logger.info('第一会展注册失败')
            res = {"states": '2'}
        attempts += 1
        if attempts == 5:
            logger.info('第一会展5次错误')
            break
    # 文件路径
    file_path = picname
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def b9(tab, browser):
    def slide(ele, sendele, distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        time.sleep(2)
        sendele.click()

    tab.get('https://www.sonystyle.com.cn/content/sonyclub/index.html')
    ele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.login_title > div.OTP_register')
    ele.click()
    ele = tab.ele('css=#loginCode')
    ele.input(phonenum)
    tab.listen.start(targets='https://www.sonystyle.com.cn/eSolverOmniChannel/account/sendOTP.do')
    buttonele = tab.ele('css=#nc_2_n1z')
    sendele = tab.ele(
        'css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
    slide(buttonele, sendele, 280)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----索尼中国{masked_phone}----：{res}')
    except:
        logger.info('索尼中国注册失败')
        res = {'msg': '-1'}

    browser.quit()  # 关闭浏览器


def c9(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://login.alo7.com/#/teacher')
    ele = tab.ele('css=#app > div > div.content > div > form > div.no-account.dl > div.signup.dd.text-r > span')
    ele.click()
    ele = tab.ele('css=#app > div > div.content > div > form > div:nth-child(2) > div.input-group > input.tel-num')
    ele.input(phonenum)

    tab.listen.start(targets='/sms_verify_code')  # 开始监听，指定获取包含该文本的数据包
    time.sleep(1)
    imgele = tab.ele('css=#app > div > div.content > div > form > div:nth-child(3) > div.input-group > img')
    inputele = tab.ele('css=#app > div > div.content > div > form > div:nth-child(3) > div.input-group > input')
    sendele = tab.ele('css=#app > div > div.content > div > form > div:nth-child(4) > div.input-group > button')
    range = 6
    picname = 'alq.png'

    char(imgele, inputele, sendele, range, picname)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        res = 'suss'
        logger.info(f'----爱乐奇{masked_phone}----：{res}')

    except:
        logger.info('爱乐奇注册失败')
        res = {'s'}

    attempts = 0
    while res != 'suss':
        imgele.click()
        tab.listen.start(targets='/sms_verify_code')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----爱乐奇{masked_phone}----：{res}')
        except:
            logger.info('爱乐奇注册失败')
            res = {'s'}
        attempts += 1
        if attempts == 5:
            logger.info('爱乐奇5次错误')
            break
    # 文件路径
    file_path = picname
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def d9(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://www.hstong.com/passport/login?target=https://www.hstong.com/news/detail/25022021154285218')
    ele = tab.ele('css=#app > div > form > ul > li:nth-child(1) > input[type=tel]')
    ele.input(phonenum)
    ele = tab.ele('css=#js-login-sms-agreements')
    ele.click()
    tab.listen.start(targets='/login/sms/code')  # 开始监听，指定获取包含该文本的数据包
    time.sleep(1)
    imgele = tab.ele('css=#captchaWrapper > img')
    inputele = tab.ele('css=#app > div > form > ul > li:nth-child(2) > div > input[type=text]')
    sendele = tab.ele('css=#app > div > form > ul > li:nth-child(3) > a')
    range = 6
    picname = 'hst.png'

    char(imgele, inputele, sendele, range, picname)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----花生同{masked_phone}----：{res}')
    except:
        logger.info('花生同注册失败')
        res = {"success": 'error'}

    attempts = 0
    while res['success'] != True:
        imgele.click()
        tab.listen.start(targets='/login/sms/code')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----花生同{masked_phone}----：{res}')
        except:
            logger.info('花生同注册失败')
            res = {"success": 'error'}
        attempts += 1
        if attempts == 5:
            logger.info('花生同5次错误')
            break
    # 文件路径
    file_path = picname
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass
    browser.quit()  # 关闭浏览器


def e9(tab, browser):
    def slide(ele, sendele, distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        time.sleep(2)
        sendele.click()

    tab.get('https://ibaotu.com/sy/?spm=xmpdh&ref=pidoutv.com')

    ele = tab.ele(
        'css=body > div.refactor-modal-wrapper.channel-login.reg-pop.login-pop > div > div.refactor-login-modal-body > div.form-item-method-list > a.form-item-method-item.form-item-method-iphone.btn-social-login-item.phone-login-sub.btn-social-login-item')
    ele.click()
    ele = tab.ele('css=#refactor-phone-input')
    ele.input(phonenum)
    tab.listen.start(targets='https://ibaotu.com/?m=login&a=sendOutCodeNew')
    buttonele = tab.ele('css=#nc_1_n1z')
    sendele = tab.ele('css=#refactor-code-click')
    slide(buttonele, sendele, 400)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----包图{masked_phone}----：{res}')
    except:
        logger.info('包图注册失败')
        res = {'msg': '-1'}

    browser.quit()  # 关闭浏览器


def f9(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://lunwen.168096.com/pc/?user_sn=97271970&ref=pidoutv.com')
    ele = tab.ele(
        r'css=#__nuxt > div.app > section > section > section > header > header > div.header-contain > div.flex-none.ml-\[10px\] > div > button > span')
    ele.click()
    time.sleep(1)
    try:
        ele.click()
    except:
        logger.info('')
    ele = tab.ele('css=#pane-2 > div > div > form > div.flex > div > button > span')
    ele.click()

    ele = tab.ele('css=#pane-2 > div > div > form > div:nth-child(1) > div > div')
    ele = ele.child().next().child()
    # logger.info(ele)
    ele.input(phonenum)
    # ele.click()
    time.sleep(1)
    # tab.actions.type(phonenum)
    imgele = tab.ele('css=#pane-2 > div > div > form > div:nth-child(2) > div > div > div > span > span > div > img')
    ele = tab.ele('css=#pane-2 > div > div > form > div:nth-child(2) > div')
    inputele = ele.child().child().child()
    # logger.info(inputele)

    sendele = tab.ele(
        'css=#pane-2 > div > div > form > div:nth-child(3) > div > div > div > span > span > div > button > span')
    range = 6
    picname = 'moyanai.png'
    tab.listen.start(targets='https://lunwen.168096.com/api/index/sendSms')  # 开始监听，指定获取包含该文本的数据包
    char(imgele, inputele, sendele, range, picname)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----莫言ai{masked_phone}----：{res}')
    except:
        logger.info('莫言ai注册失败')
        res = {"msg": 2}

    attempts = 0
    while res['msg'] != '成功':
        tab.listen.start(targets='https://lunwen.168096.com/api/index/sendSms')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----莫言ai{masked_phone}----：{res}')
        except:
            logger.info('莫言ai注册失败')
            res = {"msg": 2}
        attempts += 1
        if attempts == 5:
            logger.info('莫言ai5次错误')
            break
    # 文件路径
    file_path = picname
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    browser.quit()  # 关闭浏览器


def g9(tab, browser):
    def slide(ele, distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        # time.sleep(2)
        # sendele.click()

    tab.get('https://user.mockplus.cn/signup')

    ele = tab.ele('css=#captcha-phone')
    ele.input(phonenum)
    tab.listen.start(targets='/alismsVerify')
    ele = tab.ele('css=#phone-register-first-button')
    ele.click()
    buttonele = tab.ele('css=#aliyunCaptcha-sliding-slider')
    # sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
    time.sleep(2)
    slide(buttonele, 320)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----慕客{masked_phone}----：{res}')
    except:
        logger.info('慕客注册失败')
        res = {'msg': '-1'}

    browser.quit()  # 关闭浏览器


def h9(tab, browser):
    def char(imgele, inputele, sendele, range, picname):
        imgele.click()
        time.sleep(1)
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        # logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click()

    tab.get('https://www.mad-men.com/')
    ele = tab.ele(
        'css=#__layout > div > div.header.container > div > div.header-user > div > div.regLogin > span:nth-child(1)')
    ele.click()
    ele = tab.ele('css=#__layout > div > div.loginBox > div > div.logins > form > div:nth-child(1) > input[type=text]')
    ele.input(phonenum)
    tab.listen.start(targets='/sendRegisterCode')  # 开始监听，指定获取包含该文本的数据包

    imgele = tab.ele('css=#__layout > div > div.loginBox > div > div.logins > form > div:nth-child(2) > img')
    inputele = tab.ele(
        'css=#__layout > div > div.loginBox > div > div.logins > form > div:nth-child(2) > input[type=text]')
    sendele = tab.ele('css=#__layout > div > div.loginBox > div > div.logins > form > div:nth-child(3) > button > span')
    range = 6
    picname = 'ggkr.png'
    char(imgele, inputele, sendele, range, picname)

    # ele = tab.ele('css=#registerLayer2 > div > div.tab_form > div > ul > li:nth-child(4) > span')

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----广告狂人{masked_phone}----：{res}')
    except:
        logger.info('广告狂人注册失败')
        res = {"code": '60003'}

    attempts = 0
    while res['code'] != '10000':
        tab.listen.start(targets='/sendRegisterCode')  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele, inputele, sendele, range, picname)

        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----广告狂人{masked_phone}----：{res}')
        except:
            logger.info('广告狂人注册失败')
            res = {"code": '2'}
        attempts += 1
        if attempts == 5:
            logger.info('广告狂人5次错误')
            break

    # 文件路径
    file_path = picname
    # 删除文件
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

    browser.quit()  # 关闭浏览器


def i9(tab, browser):
    def slide(ele, distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 8.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 6.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 8.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 4.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        # time.sleep(2)
        # sendele.click()

    tab.get('https://www.feemoo.com/login')
    ele = tab.ele(
        'css=#app > div > div.downContent > div:nth-child(1) > div.rightBox > div.step1 > div.rtop1 > div:nth-child(2)')
    ele.click()
    ele = tab.ele(
        'css=#app > div > div.downContent > div:nth-child(1) > div.rightBox > div.step1 > div.loginMethodFlag1 > div.userBox > div > div > div > input')
    ele.input(phonenum)

    time.sleep(1)
    ele = tab.ele(
        'css=#app > div > div.downContent > div:nth-child(1) > div.rightBox > div.step1 > div.loginMethodFlag1 > div.userBox > div > button > span')

    ele.click(by_js=True)
    time.sleep(1)
    buttonele = tab.ele('css=#aliyunCaptcha-sliding-slider')
    tab.listen.start(targets='/phoneLoginCode')
    # sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
    slide(buttonele, 800)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----feemoo{masked_phone}----：{res}')
    except:
        logger.info('feemoo注册失败')
        res = {'msg': '-1'}

    browser.quit()  # 关闭浏览器


def j9(tab, browser):
    def slide(ele, distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """

            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)

            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track

        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 8.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 6.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 8.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 4.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        # time.sleep(2)
        # sendele.click()

    tab.get('https://sspai.com/login')

    ele = tab.ele('css=#root > div.page__login > div > div.phone__input__wrapper.comp__PhoneInput > input')
    ele.input(phonenum)

    time.sleep(1)
    ele = tab.ele('css=#root > div.page__login > div > div.code__input__wrapper > button')

    ele.click(by_js=True)
    time.sleep(1)
    buttonele = tab.ele('css=#nc_1_n1z')
    tab.listen.start(targets='/code/send')
    # sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
    slide(buttonele, 400)

    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----spai{masked_phone}----：{res}')
    except:
        logger.info('spai注册失败')
        res = {'msg': '-1'}

    browser.quit()  # 关闭浏览器

def a10(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://my.cnki.net/Register/CommonRegister.html')
  ele = tab.ele('css=#txtMobile')
  
  ele.input(phonenum)
  
  tab.listen.start(targets='/send_verify_code')
  
  buttonele = tab.ele('css=#nc_2_n1z')
  slide(buttonele,300)
  time.sleep(3)
  ele = tab.ele('css=#smsbtn')
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----cnki{masked_phone}----：{res}')
  except:
      logger.info('cnki注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def b10(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click()
  tab.get('https://www.idcyq.cn/register')
  
  ele = tab.ele('css=#phoneInp')
  ele.input(phonenum)
  
  
  
  imgele = tab.ele('css=#allow_register_phone_captcha')
  inputele = tab.ele('css=#captcha_allow_register_phone_captcha')
  sendele = tab.ele('css=#phone > form > ul > li:nth-child(4) > button')
  range = 6
  picname = 'yq.png'
  tab.listen.start(targets='/register_phone_send')
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----云群{masked_phone}----：{res}')
      res = {"status": 200}
  except:
      logger.info('云群注册失败')
      res = {"status": 400}
  
  
  attempts = 0
  while res['status'] != 200:
  
      tab.listen.start(targets='/register_phone_send')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----云群{masked_phone}----：{res}')
          flag = 1
      except:
          logger.info('云群注册失败')
          res = {"return_code": '-1'}
      attempts += 1
      if attempts == 5:
          logger.info('云群5次错误')
          break
  
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass

  browser.quit()  # 关闭浏览器


def c10(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click()
  tab.get('https://console.jfbym.com/register/?domain=https%3A%2F%2Fwww.jfbym.com')
  
  ele = tab.ele('css=#phone')
  ele.input(phonenum)
  
  
  
  imgele = tab.ele('css=#imgVer')
  inputele = tab.ele('css=#imgCode')
  sendele = tab.ele('css=#sentCode')
  range = 6
  picname = 'ym.png'
  tab.listen.start(targets='/sentCode')
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----云码{masked_phone}----：{res}')
      flag = 1
  except:
      logger.info('云码注册失败')
      flag = 0
  
  attempts = 0
  while flag == 0:
  
      tab.listen.start(targets='/sentCode')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----云码{masked_phone}----：{res}')
          flag = 1
      except:
          logger.info('云码注册失败')
          res = {"return_code": '-1'}
      attempts += 1
      if attempts == 5:
          logger.info('云码5次错误')
          break
  
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass

  browser.quit()  # 关闭浏览器


def d10(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      # logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click()
  tab.get('https://www.onezh.com/reg/login.asp')
  ele = tab.ele('css=body > div.login > div.login_R > div.login_R_top > span:nth-child(3)')
  ele.click()
  ele = tab.ele('css=#mobile')
  ele.input(phonenum)
  tab.listen.start(targets='https://www.onezh.com/reg/getstaffcode.asp')
  imgele = tab.ele('css=#login_staff > div.account > div:nth-child(2) > img')
  inputele = tab.ele('css=#fiCode')
  sendele = tab.ele('css=#gaincode')
  range = 0
  picname = 'cp.png'
  
  char(imgele,inputele,sendele,range,picname)
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----创配----：{res}')
  except:
      logger.info('创配注册失败')
      res = {"states": 2}
  
  attempts = 0
  while res['states'] != 'ok':
      tab.listen.start(targets='https://www.onezh.com/reg/getstaffcode.asp')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----创配----：{res}')
      except:
          logger.info('创配注册失败')
          res = {"states": 2}
      attempts += 1
      if attempts == 5:
          logger.info('创配5次错误')
          break
    # 文件路径
  file_path = picname
    # 删除文件
  if os.path.exists(file_path):
      os.remove(file_path)
  else:
      pass
  browser.quit()  # 关闭浏览器


def e10(tab, browser):
    def slide(ele,distance):
        def get_slide_track(distance):
            """
            根据滑动距离生成滑动轨迹
            :param distance: 需要滑动的距离
            :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
                x: 已滑动的横向距离
                y: 已滑动的纵向距离, 除起点外, 均为0
                t: 滑动过程消耗的时间, 单位: 毫秒
            """
            def __ease_out_expo(sep):
                if sep == 1:
                    return 1
                else:
                    return 1 - pow(2, -10 * sep)
            if not isinstance(distance, int) or distance < 0:
                raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
            # 初始化轨迹列表
            slide_track = [
                [random.randint(-50, -10), random.randint(-50, -10), 0],
                [0, 0, 0],
            ]
            # 共记录count次滑块位置信息
            count = 30 + int(distance / 2)
            # 初始化滑动时间
            t = random.randint(50, 100)
            # 记录上一次滑动的距离
            _x = 0
            _y = 0
            for i in range(count):
                # 已滑动的横向距离
                x = round(__ease_out_expo(i / count) * distance)
                # 滑动过程消耗的时间
                t += random.randint(10, 20)
                if x == _x:
                    continue
                slide_track.append([x, _y, t])
                _x = x
            slide_track.append(slide_track[-1])
            del slide_track[0]
            del slide_track[0]
            return slide_track
        tab.actions.hold(ele)
        temp_track = 0
        temp_time = 0
        for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
            now_track = track[0] - temp_track
            now_time = track[2] - temp_time
            tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
            # logger.info("now_track:", now_track)
            # time.sleep(track[2]/1000)
            # logger.info("now_time:", now_time / 1000)
            temp_track = track[0]
            temp_time = track[2]
        tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
        time.sleep(0.1)
        tab.actions.release()
        # time.sleep(2)
        # sendele.click()
    tab.get('https://js.design/login?type=register&by=phone')
    
    ele = tab.ele('css=#root > div > div > new-root > div > div > div.main-wrap > div.card-wrap > div > main > div.loginCardForm__3jjSi > div.sc-eIcdZJ.btipml > div.sc-gweoQa.ilXARf.form.form1-show > div > div > div:nth-child(1) > div > div > div > div > input[type=text]')
    ele.input(phonenum)
    tab.listen.start(targets='/sms')
    time.sleep(1)
    ele = tab.ele('css=#root > div > div > new-root > div > div > div.main-wrap > div.card-wrap > div > main > div.loginCardForm__3jjSi > div.sc-eIcdZJ.btipml > div.sc-gweoQa.ilXARf.form.form1-show > div > div > div.input-item.show-input-item > div > div > span > span')
    #logger.info(ele)
    ele.click()
    
    time.sleep(1)
    ele.click(by_js=True)
    buttonele = tab.ele('css=#nc_2_n1z')
    #sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
    slide(buttonele,380)
    
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----及时设计----：{res}')
    except:
        logger.info('及时设计注册失败')
        res = {'msg': '-1'}


    browser.quit()  # 关闭浏览器


def f10(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://passport.jlc.com/register?appId=JLC_OSHWHUB&backCode=1&redirectUrl=https%3A%2F%2Foshwhub.com')
  ele = tab.ele('css=#__layout > div > div > div > main > div > div > div > div.text-center > div.flex.justify-center > button:nth-child(1) > div.icon')
  ele.click()
  ele = tab.ele('css=#__layout > div > div > div > main > div > div > div > div.wrapper > form > div:nth-child(1) > div > div > div > input')
  ele.input(phonenum)
  
  tab.listen.start(targets='/send-security-code')
  
  buttonele = tab.ele('css=#nc_1_n1z')
  slide(buttonele,380)
  time.sleep(3)
  ele = tab.ele('css=#__layout > div > div > div > main > div > div > div > div.wrapper > form > div.el-form-item.my-20 > div > label > span.el-checkbox__input > span')
  ele.click()
  ele = tab.ele('css=#__layout > div > div > div > main > div > div > div > div.wrapper > form > div:nth-child(3) > div > div > button > span')
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----嘉立创{masked_phone}----：{res}')
  except:
      logger.info('嘉立创注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def g10(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://bbs.elecfans.com/member.php?referer=https%3A%2F%2Fbbs.elecfans.com%2F&siteid=4&scene=&account=&fromtype=undefined&mod=reg')
  
  ele = tab.ele('css=#regist_form > div.icon_form_item.mobile_form_item > input')
  ele.input(phonenum)
  
  tab.listen.start(targets='/regsms')
  
  buttonele = tab.ele('css=#nc_1_n1z')
  slide(buttonele,380)
  time.sleep(3)
  ele = tab.ele('css=#smscode_btn')
  ele.click()
  # ele = tab.ele('css=#__layout > div > div > div > main > div > div > div > div.wrapper > form > div:nth-child(3) > div > div > button > span')
  # ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----电子发烧友{masked_phone}----：{res}')
  except:
      logger.info('电子发烧友注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def h10(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click()
  tab.get('https://www.niaogebiji.com/')
  ele = tab.ele('css=body > div.page_top.mobileHide > div.top-bar > div > div.right > ul > div > div > p.down-text > a')
  ele.click()
  ele = tab.ele('css=body > div.page_top.mobileHide > div.login_modal > div.login_content > div.acc_item > div.login_type > div.login_toSms')
  ele.click()
  ele = tab.ele('css=#login_phone')
  ele.input(phonenum)
  ele = tab.ele('css=body > div.page_top.mobileHide > div.login_modal > div.login_content > div.loginbox-top > img')
  ele.click()
  time.sleep(1)
  
  imgele = tab.ele('css=body > div.page_top.mobileHide > div.login_modal > div.login_content > div.login_item > div.forget_item_sms > div > img')
  inputele = tab.ele('css=#login_pic_code')
  sendele = tab.ele('css=body > div.page_top.mobileHide > div.login_modal > div.login_content > div.login_item > div.login_item_password > div')
  range = 6
  picname = 'ngbj.png'
  tab.listen.start(targets='/dx')
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----鸟哥笔记----：{res}')
  except:
      logger.info('鸟哥笔记注册失败')
      res = {"return_code": '-1'}
  
  attempts = 0
  while res['return_code'] != '200':
      ele = tab.ele('css=body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div > button')
      ele.click()
      imgele.click()
      tab.listen.start(targets='/dx')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----鸟哥笔记----：{res}')
      except:
          logger.info('鸟哥笔记注册失败')
          res = {"return_code": '-1'}
      attempts += 1
      if attempts == 5:
          logger.info('鸟哥笔记5次错误')
          break
  # 文件路径
  file_path = 'rr.png'
  # 删除文件
  if os.path.exists(file_path):
      os.remove(file_path)
  else:
      pass
  browser.quit()  # 关闭浏览器


def i10(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://paper.tuanjiewang.cn/')
  ele = tab.ele('css=body > div > div > div > ul.layui-nav.layui-layout-right > li > a')
  ele.click()
  ele = tab.ele('css=body > div.box_outer.fleft > div.box_right > div.layui-tab.layui-tab-brief > ul > li:nth-child(3)')
  ele.click()
  ele = tab.ele('css=#phone')
  ele.input(phonenum)
  tab.listen.start(targets='/SMSHandler.ashx')
  time.sleep(1)
  ele = tab.ele('css=#send_code')
  #logger.info(ele.text)
  ele.click(by_js=True)
  time.sleep(1)
  buttonele = tab.ele('css=#slider > div > div > div > i')
  #sendele = tab.ele('css=#header-index > div:nth-child(3) > div > div.ldr.fl > div > div.m_register > div.register_m_t > div > div > div > div.valid_z.valid_z2.clearfix > div > div.vlid_img.fl > div.huoqu.reg_huoquclub1 > a')
  slide(buttonele,300)
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----团结{masked_phone}----：{res}')
  except:
      logger.info('团结注册失败')
      res = {'msg': '-1'}

  browser.quit()  # 关闭浏览器


def j10(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://passport.zcool.com.cn/regPhone.do')
  ele = tab.ele('css=#mobilephone')
  
  ele.input(phonenum)
  
  tab.listen.start(targets='/phoneSendcodeNew.do')
  
  buttonele = tab.ele('css=#nc_1_n1z')
  slide(buttonele,300)
  time.sleep(3)
  ele = tab.ele('css=#veribtn')
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----站库{masked_phone}----：{res}')
  except:
      logger.info('站库注册失败')
      res = {"statusCode": -1}


  browser.quit()  # 关闭浏览器
def a11(tab, browser):
  tab.get('https://accounts.wondershare.cn/web/login_cn')
  
  ele = tab.ele('css=#pane-verify-code > div > form > div:nth-child(1) > div > div > input')
  
  ele.input(phonenum)
  tab.listen.start(targets='/mobile/captcha')
  ele = tab.ele('css=body > div:nth-child(3) > div.pages > div > div > div.pages_main > div > form > div > div > div > div.checkou-box-container > div > svg > use')
  
  ele.click()
  ele = tab.ele('css=#pane-verify-code > div > form > div:nth-child(2) > div > div > span > span > div > span')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----万兴科技{masked_phone}----：{res}')
  except:
      logger.info('万兴科技注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def b11(tab, browser):
  tab.get('https://www.edrawsoft.cn/mindmaster/')
  ele = tab.ele('css=#loginBtn > span:nth-child(2)')
  
  ele.click(by_js=True)
  ele = tab.ele('css=body > div > div:nth-child(2) > div > div.app-body--wrapper.app-smallbody--right > div.sign-up > div.el-row.is-justify-space-around.el-row--flex > form > div.el-form-item.is-required.is-no-asterisk > div > div > div > div.el-input.el-input--small.el-input--suffix > input')
  
  ele.input(phonenum)
  time.sleep(2)
  tab.listen.start(targets='/send?mobile=')
  ele = tab.ele('css=body > div > div:nth-child(2) > div > div.app-body--wrapper.app-smallbody--right > div.sign-up > div.el-row.is-justify-space-around.el-row--flex > form > div:nth-child(4) > div > div > img')
  
  ele.click()
  
  ele = tab.ele('css=body > div > div:nth-child(2) > div > div.app-body--wrapper.app-smallbody--right > div.sign-up > div.el-row.is-justify-space-around.el-row--flex > form > div:nth-child(3) > div > div > div.verify-code > div > span > span > span')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----亿图{masked_phone}----：{res}')
  except:
      logger.info('亿图注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def c11(tab, browser):
  tab.get('https://www.cmdi.org.cn/cmdi/registerMember/toRegister.do')
  
  ele = tab.ele('css=#mobile')
  
  ele.input(phonenum)
  tab.listen.start(targets='/sms/getCode.do')
  ele = tab.ele('css=#memberForm > ul > li.yxyzm > span.hqyzm')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----医疗器械{masked_phone}----：{res}')
  except:
      logger.info('医疗器械注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def d11(tab, browser):
  url = 'https://dxs-new.u2.hep.com.cn/login'
  phoneele = 'css=#emailRegister_identify'
  sendele = 'css=#emailRegister > div:nth-child(2) > div > div > div > div > div > div.authing-ant-col.authing-ant-col-8.authing-ant-col-offset-1 > button > span'
  target = '/sms/send'
  name = '大学生在线'
  
  tab.get(url)
  ele = tab.ele('css=#root > section > div.guardContainer > div > div > div > div > div:nth-child(2) > div.g2-tips-line > span > button > span')
  ele.click()
  ele = tab.ele('css=#rc-tabs-1-tab-phone-code')
  ele.click()
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def e11(tab, browser):
  url = 'https://club.yonghongtech.com/member.php?mod=register'
  phoneele = 'css=#phone_reg'
  sendele = 'css=#sendseccoderegbtn > a'
  target = 'sendseccode'
  name = '永洪'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info('{万兴科技}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def f11(tab, browser):
  tab.get('https://prm.sangfor.com/register')
  
  ele = tab.ele('css=#app > el-config-provider > div > div.card > div > div > form > div:nth-child(8) > div > div > input')
  
  ele.input(phonenum)
  tab.listen.start(targets='sendMobileCaptchaRegister')
  ele = tab.ele('css=#app > el-config-provider > div > div.card > div > div > form > div.el-form-item.is-required.el-form-item--small.auto-code > div > button')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----深信服{masked_phone}----：{res}')
  except:
      logger.info('深信服注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def g11(tab, browser):
  tab.get('https://modao.cc/')
  ele = tab.ele('css=body > header > nav > div > div > div.modao-navbar-collapse > ul:nth-child(3) > li.modao-navbar-item.wondershare-user-panel.nav-md-login-btn.px-xxl-4.log-out > div > a.modao-navbar-btnregister.font-weight-medium')
  
  ele.click()
  ele = tab.ele('css=#auth-box > div > div.aboveContent > div.styles__StyledNewMain-sc-1jr0jyp-0.cXlgsi.isWebMain.feature-main.is-modal > ul > div > div > div.login-way-icon.tel > svg')
  ele.click()
  ele = tab.ele('css=#auth-box > div > div.aboveContent > div.styles__StyledNewMain-sc-1jr0jyp-0.cXlgsi.isWebMain.feature-main.is-modal > div.newCommon__StyledNewCommon-sc-kv0lgn-0.NewSignPage__StyledNewSignPage-sc-1wh7g84-0.hcTCZZ.gzuYbf.sign-page > div > div.entry-input.emailPhone > input')
  
  ele.input(phonenum)
  tab.listen.start(targets='/sendCaptcha')
  ele = tab.ele('css=#auth-box > div > div.aboveContent > div.styles__StyledNewMain-sc-1jr0jyp-0.cXlgsi.isWebMain.feature-main.is-modal > div.newCommon__StyledNewCommon-sc-kv0lgn-0.NewSignPage__StyledNewSignPage-sc-1wh7g84-0.hcTCZZ.gzuYbf.sign-page > div > div.entry-input.custom-entry-input.verifyCode > div > button')
  
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----磨刀{masked_phone}----：{res}')
  except:
      logger.info('磨刀注册失败')
      res = {"statusCode": -1}


  browser.quit()  # 关闭浏览器


def h11(tab, browser):
  url = 'https://www.doudou.fun/'
  phoneele = 'css=#el-id-1024-11'
  sendele = 'css=#__nuxt > div.app-header.pc-header > div > div.login-dialog-mask > div > div.dialog-content > form > div:nth-child(2) > div.el-form-item__content > div > div > span > span > span'
  target = 'send_phone_verification_code'
  name = '逗逗游戏伙伴'
  
  tab.get(url)
  ele = tab.ele('css=#__nuxt > div.app-header.pc-header > div > div.header-right > div:nth-child(6) > div > span')
  ele.click()
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}



  browser.quit()  # 关闭浏览器


def i11(tab, browser):
    url = 'https://yuewen.cn/chats/new'
    
    phoneele = 'css=' + 'body > div.yuewen-modal.mask > div > div.login_main__tilO0 > div.input_container__0yW3j.login_mobileInput__ffFID.input_fill__s005N.input_middle__UGzxk > input'
    sendele = 'css=' + 'body > div.yuewen-modal.mask > div > div.login_main__tilO0 > div:nth-child(2) > button > span'
    target = '/SendVerifyCode'
    name = '阶跃ai'
    
    tab.get(url)
    ele = tab.ele('text=请登录')
    ele.click()
    # ele = tab.ele('css=body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div > span > div > div:nth-child(2) > span')
    # ele.click()
    ele = tab.ele(phoneele)
    ele.input(phonenum)
    ele = tab.ele(sendele)
    tab.listen.start(targets=target)
    ele.click()
    
    try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
    except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
    browser.quit()  # 关闭浏览器


def j11(tab, browser):
  url = 'https://www.hhax.org/user/reg'
  phoneele = 'css=#phone2'
  sendele = 'css=#sendSmsBtn'
  target = '/smscode'
  name = '韩红'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def a12(tab, browser):
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get('https://web.ccf.org.cn/CCF/regTo.action?flag=0&url=')
  ele = tab.ele('css=#person > div > label:nth-child(2) > input[type=radio]')
  ele.click()
  ele = tab.ele('css=#phone')
  
  ele.input(phonenum)
  
  tab.listen.start(targets='user!sendAuthCodePhone.action?')
  
  buttonele = tab.ele('css=#verify-wrap > span.drag-btn.dragBtn')
  slide(buttonele,420)
  time.sleep(3)
  ele = tab.ele('css=#phoneCode')
  ele.click()
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----ccf{masked_phone}----：{res}')
  except:
      logger.info('ccf注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def b12(tab, browser):
  #0网址
  url = 'https://www.ilovezuan.com/'
  #1输入手机号
  phonee = 'css=' + '#r_username'
  #2图片验证码ele
  imge = 'css=' + '#r_captcha_code > img'
  #3验证码输入框ele
  inpute = 'css=' + '#r_captchacode'
  #4发送短信按钮
  sende = 'css=' + '#reg_get_code'
  range = 6
  picname = 'ysw.png'
  #5监听端口
  target = '?act=captchas'
  #res = {"result": False}
  #成功res
  resleft = 'code'
  resright = 200
  name = '钻石网'
  
  
  
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  
  tab.get(url)
  ele = tab.ele('css=body > div.top:nth-child(1) > div.web_nav.w1280.clearfix > div.fr.clearfix > div.fr.tel:nth-child(1) > h3 > div.login_wrap.fr:nth-child(1) > span > a:nth-child(2)')
  ele.click()
  phoneele = tab.ele(phonee)
  phoneele.input(phonenum)
  imgele = tab.ele(imge)
  inputele = tab.ele(inpute)
  sendele = tab.ele(sende)
  tab.listen.start(targets=target)
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res[resleft] = 11
  
  
  attempts = 0
  
  while res[resleft] != resright:
      tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----{name}{masked_phone}----：{res}')
      except:
          logger.info(f'{name}注册失败')
          res[resleft] = 11
      attempts += 1
      if attempts == 5:
          logger.info(f'{name}5次错误')
          break
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass


  browser.quit()  # 关闭浏览器


def c12(tab, browser):
  #0网址
  url = 'https://www.iyunshu.com/cregis.html'
  #1输入手机号
  phonee = 'css=' + '#cregis-page > form > div:nth-child(4) > div > input'
  #2图片验证码ele
  imge = 'css=' + '#vicode'
  #3验证码输入框ele
  inpute = 'css=' + '#cregis-page > form > div.form-group.ng-scope > div > input'
  #4发送短信按钮
  sende = 'css=' + '#sms-btn'
  range = 6
  picname = 'ysw.png'
  #5监听端口
  target = '/sendCaptchas.do'
  #res = {"result": False}
  #成功res
  resleft = 'code'
  resright = '0'
  name = '云书网'
  
  
  
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  
  tab.get(url)
  phoneele = tab.ele(phonee)
  phoneele.input(phonenum)
  imgele = tab.ele(imge)
  inputele = tab.ele(inpute)
  sendele = tab.ele(sende)
  tab.listen.start(targets=target)
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = 11
  
  
  attempts = 0
  
  while res[resleft] != resright:
      tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----{name}{masked_phone}----：{res}')
      except:
          logger.info(f'{name}注册失败')
          res = {"result": False}
      attempts += 1
      if attempts == 5:
          logger.info(f'{name}5次错误')
          break
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass

  browser.quit()  # 关闭浏览器


def d12(tab, browser):
    #0网址
    url = 'https://www.tjbb.com/user.php?act=register'
    #1输入手机号#mobile_phone
    phonee = 'css=' + '#mobile_phone'
    #2图片验证码elebody.bg-ligtGary > div.register:nth-child(1) > div.container:nth-child(2) > div.w.w1200 > div.register-wrap > div.register-form:nth-child(2) > div.form.form-other > form > div.item:nth-child(2) > div.item-info:nth-child(2) > img.captcha_img.fl
    imge = 'css=' + 'body.bg-ligtGary > div.register:nth-child(1) > div.container:nth-child(2) > div.w.w1200 > div.register-wrap > div.register-form:nth-child(2) > div.form.form-other > form > div.item:nth-child(2) > div.item-info:nth-child(2) > img.captcha_img.fl'
    #3验证码输入框ele#captcha
    inpute = 'css=' + '#captcha'
    #4发送短信按钮
    sende = 'css=' + '#zphone'
    range = 6
    picname = 'tt.png'
    #5监听端口
    target = '=register'
    #res = {"result": False}
    #成功res
    resleft = 'code'
    resright = 2
    name = '天天'
    
    
    
    def char(imgele,inputele,sendele,range,picname):
        inputele.clear()
        imgele.click()
        time.sleep(1)
        imgele.get_screenshot(name=picname)
        ocr = ddddocr.DdddOcr(show_ad=False)
        image = open(picname, "rb").read()
        ocr.set_ranges(range)
        result = ocr.classification(image, probability=True)
        s = ""
        for i in result['probability']:
            s += result['charsets'][i.index(max(i))]
        #logger.info(s)
        inputele.clear()
        inputele.input(s)
        sendele.click(by_js=True)
    
    tab.get(url)
    phoneele = tab.ele(phonee)
    phoneele.input(phonenum)
    imgele = tab.ele(imge)
    inputele = tab.ele(inpute)
    sendele = tab.ele(sende)
    tab.listen.start(targets=target)
    char(imgele,inputele,sendele,range,picname)
    try:
        res = tab.listen.wait(timeout=10).response
        res = res.body
        logger.info(f'----{name}{masked_phone}----：{res}')
        try:
            if res['msg'] == '验证码有误':
                res[resleft] = False
        except:
            pass
    except:
        logger.info(f'{name}注册失败')
        res[resleft] = False
    
    
    attempts = 0
    
    while res[resleft] != resright:
        tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
        time.sleep(2)
        char(imgele,inputele,sendele,range,picname)
    
        try:
            res = tab.listen.wait(timeout=10).response
            res = res.body
            logger.info(f'----{name}{masked_phone}----：{res}')
            try:
                if res['msg'] == '验证码有误':
                    res[resleft] = False
            except:
                pass
        except:
            logger.info(f'{name}注册失败')
            res = {"result": False}
        attempts += 1
        if attempts == 5:
            logger.info(f'{name}5次错误')
            break

    browser.quit()  # 关闭浏览器


def e12(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click()
  tab.get('https://m.ydl.com/login')
  ele = tab.ele('css=#agree_agreement')
  ele.click()
  ele = tab.ele('css=#number')
  
  ele.input(phonenum)
  
  imgele = tab.ele('css=#loginCaptcha')
  inputele = tab.ele('css=#captcha')
  sendele = tab.ele('css=body > div > div > div:nth-child(2) > div:nth-child(3)')
  range = 6
  picname = 'xl.png'
  
  char(imgele,inputele,sendele,range,picname)
  ele = tab.ele('css=#sendChkCode')
  logger.info(f'----心理{masked_phone}----：{ele.text}')
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass


  browser.quit()  # 关闭浏览器


def f12(tab, browser):
  #0网址
  url = 'https://www.bacaoo.com/user/register/index'
  #1输入手机号
  phonee = 'css=' + '#phone'
  #2图片验证码ele
  imge = 'css=' + 'body > div.container > div > form > div:nth-child(2) > div:nth-child(3) > img'
  #3验证码输入框ele
  inpute = 'css=' + '#register_verify_code'
  #4发送短信按钮
  sende = 'css=' + 'body > div.container > div > form > div:nth-child(3) > div:nth-child(3) > button'
  range = 6
  picname = 'bc.png'
  #5监听端口
  target = '/getcode'
  #res = {"result": False}
  #成功res
  resleft = 'error'
  resright = 0
  name = '拔草'
  
  
  
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  
  tab.get(url)
  phoneele = tab.ele(phonee)
  phoneele.input(phonenum)
  imgele = tab.ele(imge)
  inputele = tab.ele(inpute)
  sendele = tab.ele(sende)
  tab.listen.start(targets=target)
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = 11
  
  
  attempts = 0
  
  while res[resleft] != resright:
      tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----{name}{masked_phone}----：{res}')
      except:
          logger.info(f'{name}注册失败')
          res = {"result": False}
      attempts += 1
      if attempts == 10:
          logger.info(f'{name}5次错误')
          break
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass

  browser.quit()  # 关闭浏览器


def g12(tab, browser):
  url = 'https://login.bce.baidu.com/new-reg?tpl=bceplat&from=portal'
  phonee = 'css=' + '#register_mobile'
  sende = 'css=' + '#register > div:nth-child(5) > div > div > div > div > div > span > span > button > span'
  buttone = 'css=' + '#vcode-slide-button708'
  target = '/send'
  name = '百度智能云'
  
  def slide(ele,distance):
      def get_slide_track(distance):
          """
          根据滑动距离生成滑动轨迹
          :param distance: 需要滑动的距离
          :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
              x: 已滑动的横向距离
              y: 已滑动的纵向距离, 除起点外, 均为0
              t: 滑动过程消耗的时间, 单位: 毫秒
          """
          def __ease_out_expo(sep):
              if sep == 1:
                  return 1
              else:
                  return 1 - pow(2, -10 * sep)
          if not isinstance(distance, int) or distance < 0:
              raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
          # 初始化轨迹列表
          slide_track = [
              [random.randint(-50, -10), random.randint(-50, -10), 0],
              [0, 0, 0],
          ]
          # 共记录count次滑块位置信息
          count = 30 + int(distance / 2)
          # 初始化滑动时间
          t = random.randint(50, 100)
          # 记录上一次滑动的距离
          _x = 0
          _y = 0
          for i in range(count):
              # 已滑动的横向距离
              x = round(__ease_out_expo(i / count) * distance)
              # 滑动过程消耗的时间
              t += random.randint(10, 20)
              if x == _x:
                  continue
              slide_track.append([x, _y, t])
              _x = x
          slide_track.append(slide_track[-1])
          del slide_track[0]
          del slide_track[0]
          return slide_track
      tab.actions.hold(ele)
      temp_track = 0
      temp_time = 0
      for track in get_slide_track(distance):  # 使鼠标相对当前位置移动若干距离page.actions.move(offset_x=track,
          now_track = track[0] - temp_track
          now_time = track[2] - temp_time
          tab.actions.move(offset_x=now_track, offset_y=0, duration=now_time / 1000)
          # logger.info("now_track:", now_track)
          # time.sleep(track[2]/1000)
          # logger.info("now_time:", now_time / 1000)
          temp_track = track[0]
          temp_time = track[2]
      tab.actions.move(offset_x=5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.move(offset_x=-3, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-2, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      tab.actions.move(offset_x=-5, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
      time.sleep(0.1)
      tab.actions.release()
      # time.sleep(2)
      # sendele.click()
  tab.get(url)
  ele = tab.ele('css=body > header > div > div.cloud-header-default > div.cloud-right-wrapper > div.login-wrapper > ul > li.nav-register > a')
  ele.click()
  
  ele = tab.ele(phonee)
  
  ele.input(phonenum)
  
  tab.listen.start(targets=target)
  ele = tab.ele('css=body > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(3) > div > form > div:nth-child(5) > div > div > div > div > div > span > span > span')
  ele.click()
  buttonele = tab.ele(buttone)
  slide(buttonele,380)
  #time.sleep(3)
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}





  browser.quit()  # 关闭浏览器


def h12(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  tab.get('https://www.ziyimall.com/v2/login/index.html')
  ele = tab.ele('css=#phone')
  ele.input(phonenum)
  
  imgele = tab.ele('css=#captcha-img')
  inputele = tab.ele('css=#verifyCode')
  sendele = tab.ele('css=#getCaptchaBtn')
  range = 6
  picname = 'zy.png'
  tab.listen.start(targets='/verify/sms.html')
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----紫衣{masked_phone}----：{res}')
  except:
      logger.info('紫衣注册失败')
      res = {"code": 1}
  
  attempts = 0
  while res['code'] != 0:
  
      tab.listen.start(targets='/verify/sms.html')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----紫衣{masked_phone}----：{res}')
      except:
          logger.info('紫衣注册失败')
          res = {"code": 1}
      attempts += 1
      if attempts == 5:
          logger.info('紫衣5次错误')
          break
  
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass


  browser.quit()  # 关闭浏览器


def i12(tab, browser):
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  tab.get('http://membernew.yundasys.com:15116/member.website/hywz/login.html?type=register')
  ele = tab.ele('css=body > div:nth-child(1) > div > div:nth-child(3) > p > span:nth-child(1)')
  ele.click()
  ele = tab.ele('css=body > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(1) > div > p:nth-child(1) > input')
  ele.input(phonenum)
  imgele = tab.ele('css=#msg_img_code')
  
  inputele = tab.ele('css=body > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(1) > div > p:nth-child(3) > input')
  
  sendele = tab.ele('css=body > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(1) > div > div > p > span')
  
  range = 6
  picname = 'yd.png'
  tab.listen.start(targets='/sendMessageValidImage')
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----韵达{masked_phone}----：{res}')
  except:
      logger.info('韵达注册失败')
      res = {"result": False}
  
  attempts = 0
  while res['result'] == False:
  
      tab.listen.start(targets='/sendMessageValidImage')  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----韵达{masked_phone}----：{res}')
      except:
          logger.info('韵达注册失败')
          res = {"result": False}
      attempts += 1
      if attempts == 5:
          logger.info('韵达5次错误')
          break
  
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass


  browser.quit()  # 关闭浏览器


def j12(tab, browser):
  #0网址
  url = 'https://www.fila.com.cn/fila/passport/reg'
  #1输入手机号
  phonee = 'css=' + '#user'
  #2图片验证码ele
  imge = 'css=' + '#captcha-img'
  #3验证码输入框ele
  inpute = 'css=' + '#captcha-code'
  #4发送短信按钮
  sende = 'css=' + '#submit_button'
  range = 6
  picname = 'ysw.png'
  #5监听端口
  target = 'https://www.fila.com.cn/fila/passport/regCheck1'
  #res = {"result": False}
  #成功res
  resleft = 'status'
  resright = 0
  name = '飞乐'
  
  
  
  def char(imgele,inputele,sendele,range,picname):
      inputele.clear()
      imgele.click()
      time.sleep(1)
      imgele.get_screenshot(name=picname)
      ocr = ddddocr.DdddOcr(show_ad=False)
      image = open(picname, "rb").read()
      ocr.set_ranges(range)
      result = ocr.classification(image, probability=True)
      s = ""
      for i in result['probability']:
          s += result['charsets'][i.index(max(i))]
      #logger.info(s)
      inputele.clear()
      inputele.input(s)
      sendele.click(by_js=True)
  
  tab.get(url)
  ele = tab.ele('css=#agree-check')
  ele.click()
  phoneele = tab.ele(phonee)
  phoneele.input(phonenum)
  imgele = tab.ele(imge)
  inputele = tab.ele(inpute)
  sendele = tab.ele(sende)
  tab.listen.start(targets=target)
  char(imgele,inputele,sendele,range,picname)
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res[resleft] = 11
  
  
  attempts = 0
  
  while res[resleft] != resright:
      tab.listen.start(targets=target)  # 开始监听，指定获取包含该文本的数据包
      time.sleep(2)
      char(imgele,inputele,sendele,range,picname)
  
      try:
          res = tab.listen.wait(timeout=10).response
          res = res.body
          logger.info(f'----{name}{masked_phone}----：{res}')
      except:
          logger.info(f'{name}注册失败')
          res = {"result": False}
      attempts += 1
      if attempts == 5:
          logger.info(f'{name}5次错误')
          break
  
  
  file_path = picname
  
  if os.path.exists(file_path):  # 先检查文件是否存在
      os.remove(file_path)
  else:
      pass

  browser.quit()  # 关闭浏览器

def a13(tab, browser):
  url = 'https://passport.58.com/reg/'
  phoneele = 'css=' + '#mask_body_item_phonenum'
  sendele = 'css=' + '#mask_body_item_getcode'
  target = '/passport.58.com/58'
  name = '58同城'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def b13(tab, browser):
  url = 'https://www.bookschina.com/RegUser/Register.aspx'
  phoneele = 'css=' + '#phone'
  sendele = 'css=' + '#getPhoneCode'
  target = '/ashx/RegisterApi.ashx'
  name = '中图网'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele('css=#password')
  ele.click()
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def c13(tab, browser):
  url = 'https://passport.yougou.com/register.jhtml?redirectURL=https://www.yougou.com/'
  phoneele = 'css=' + '#reg_mobile_'
  sendele = 'css=' + '#getMsgSpan'
  target = '/getMobileCode.jhtml'
  name = '优购'
  
  tab.get(url)
  ele = tab.ele('css=#layui-layer1 > div.layui-layer-btn.layui-layer-btn-c > a.layui-layer-btn1')
  ele.click()
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def d13(tab, browser):
  url = 'https://mdkd.pinduoduo.com/login'
  phoneele = 'css=' + '#root > div > div.login-container > div.login-bottom > div.right > div > div.station-tabs.station-tabs-pure.station-medium.login-tabs > div.station-tabs-content > div > div > form > div:nth-child(1) > div > span > input'
  sendele = 'css=' + '#root > div > div.login-container > div.login-bottom > div.right > div > div.station-tabs.station-tabs-pure.station-medium.login-tabs > div.station-tabs-content > div > div > form > div:nth-child(1) > div > button'
  target = 'sendVerifyCode'
  name = '多多买菜'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def e13(tab, browser):
  url = 'https://www.kongfz.com/'
  phoneele = 'css=' + '#phone'
  sendele = 'css=' + '#register > ul > li:nth-child(3) > div.input_box > a'
  target = '/replaceSemiangleByUsername'
  name = '孔夫子旧书网'
  
  tab.get(url)
  ele = tab.ele('css=#nickName > span:nth-child(3)')
  ele.click()
  ele = tab.ele('css=#loginWin > div > div.register-btn')
  ele.click()
  ele = tab.ele(phoneele)
  ele.click()
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def f13(tab, browser):
  url = 'https://www.95bd.com/passport-signup.html'
  phoneele = 'css=' + '#mobile'
  sendele = 'css=' + '#resend'
  target = '/passport-sendsmscode.html'
  name = '酒窝'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}

  browser.quit()  # 关闭浏览器


def g13(tab, browser):
  url = 'https://www.ahm.cn/Account/Login?backUrl=http://www.ahm.cn/'
  phoneele = 'css=' + '#phonenumber'
  sendele = 'css=' + '#sendCode'
  target = 'phone'
  name = '安徽博物院'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}


  browser.quit()  # 关闭浏览器


def h13(tab, browser):
  url = 'https://reg.xcar.com.cn/register.php'
  phoneele = 'css=' + '#mobile'
  sendele = 'css=' + '#codePrompt'
  target = 'https://reg.xcar.com.cn/base/check.php'
  name = '爱卡'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def i13(tab, browser):
  url = 'https://www.hua.com/Passport/Register/'
  phoneele = 'css=' + '#phone'
  sendele = 'css=' + '#getcode'
  target = '/SendV3'
  name = '花礼网'
  
  tab.get(url)
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器


def j13(tab, browser):
  url = 'https://www.meifeiyi.com/'
  phoneele = 'css=' + '#phone_id'
  sendele = 'css=' + '#huoqu'
  target = 'https://www.meifeiyi.com/'
  name = '美非遗'
  
  tab.get(url)
  ele = tab.ele('css=body > div:nth-child(3) > div.cont_div > div.x_top_kj012.x_fr > ul > li:nth-child(3) > a')
  ele.click()
  ele = tab.ele(phoneele)
  ele.input(phonenum)
  ele = tab.ele(sendele)
  tab.listen.start(targets=target)
  ele.click()
  
  try:
      res = tab.listen.wait(timeout=10).response
      res = res.body
      logger.info(f'----{name}{masked_phone}----：{res}')
  except:
      logger.info(f'{name}注册失败')
      res = {"statusCode": -1}
      res = {"statusCode": -1}
  browser.quit()  # 关闭浏览器
def create_browser():
    """创建一个新的浏览器实例"""
    co = ChromiumOptions().auto_port()
    #co.no_imgs(True).mute(True)
    co.incognito()
    co.set_argument('--disable-gpu')  # 禁用GPU，提高加载速度
    browser = Chromium(addr_or_opts=co)
    return browser
  
class BeijingFormatter(logging.Formatter):
    """ 自定义 Formatter，强制使用北京时间 """
    def formatTime(self, record, datefmt=None):
        beijing_tz = pytz.timezone("Asia/Shanghai")
        dt = datetime.fromtimestamp(record.created, beijing_tz)
        return dt.strftime(datefmt or "%Y-%m-%d %H:%M:%S")

def setup_logger(log_filename=log_filename, log_level=logging.DEBUG):
    """
    设置日志记录器，支持输出到控制台和文件，确保中文字符正常显示，时间强制使用北京时间。
    """
    # 确保 logs 目录存在
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    # 重新配置 sys.stdout 确保 UTF-8 支持
    sys.stdout.reconfigure(encoding="utf-8")

    # 避免 logger 重复创建多个处理器
    logger = logging.getLogger('my_logger')
    if logger.hasHandlers():
        return logger  # 如果已经设置了 handler，直接返回

    logger.setLevel(log_level)

    # 创建控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    # 创建文件处理器（追加模式）
    file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
    file_handler.setLevel(log_level)

    # 设置日志格式
    formatter = BeijingFormatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 绑定处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
  
def safe_execute(func):
    global phonenum
    """ 封装函数执行，捕获异常，确保每次都重启浏览器 """
    try:
        browser = create_browser()  # 每次执行时创建一个新的浏览器实例
        tab = browser.latest_tab
        tab.set.window.max()
        tab.set.auto_handle_alert()
        func(tab, browser)  # 调用传入的函数，并传递浏览器对象
    except Exception as e:
        logger.info(f"执行 {func.__name__} 失败: {e}")

def clear():
    directory = "."  # 当前目录
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file.lower().endswith(".png"):
            try:
                os.remove(file_path)
                logger.info(f"Deleted: {file_path}")
            except Exception as e:
                logger.info(f"Error deleting {file_path}: {e}")
    
    logger.info("All PNG images deleted.")

    
if __name__ == '__main__':
    logger = setup_logger()
    sys.stdout.reconfigure(encoding="utf-8")
    safe_execute(aliyun)
    safe_execute(baidu)
    safe_execute(fenghuang)
    safe_execute(ltyp)
    safe_execute(tyyp)
    safe_execute(xueqiu)
    safe_execute(juliang)
    safe_execute(tuxi)
    safe_execute(shuidichou)
    safe_execute(xhs)
    safe_execute(doubao)
    safe_execute(kye)
    safe_execute(yiche)
    safe_execute(ydyp)
    safe_execute(nfby)
    safe_execute(mita)
    safe_execute(kzxy)
    safe_execute(juren)
    safe_execute(huoshanyq)
    safe_execute(webcsdn)
    safe_execute(leyuan233)
    safe_execute(qyiliao)
    safe_execute(lmt)
    safe_execute(sd)
    safe_execute(sftc)
    safe_execute(znz)
    safe_execute(yun88)
    safe_execute(wjs)
    safe_execute(ycy)
    safe_execute(wyyyx)
    safe_execute(a4)
    safe_execute(b4)
    safe_execute(c4)
    safe_execute(d4)
    safe_execute(e4)
    safe_execute(f4)
    safe_execute(g4)
    safe_execute(h4)
    safe_execute(i4)
    safe_execute(j4)
    safe_execute(a5)
    safe_execute(b5)
    safe_execute(c5)
    safe_execute(d5)
    safe_execute(e5)
    safe_execute(f5)
    safe_execute(g5)
    safe_execute(h5)
    safe_execute(i5)
    safe_execute(j5)
    safe_execute(a6)
    safe_execute(b6)
    safe_execute(c6)
    safe_execute(d6)
    safe_execute(e6)
    safe_execute(f6)
    safe_execute(g6)
    safe_execute(h6)
    safe_execute(i6)
    safe_execute(j6)
    safe_execute(a7)
    safe_execute(b7)
    safe_execute(c7)
    safe_execute(d7)
    safe_execute(e7)
    safe_execute(f7)
    safe_execute(g7)
    safe_execute(h7)
    safe_execute(i7)
    safe_execute(j7)
    safe_execute(a8)
    safe_execute(b8)
    safe_execute(c8)
    safe_execute(d8)
    safe_execute(e8)
    safe_execute(f8)
    safe_execute(g8)
    safe_execute(h8)
    safe_execute(i8)
    safe_execute(j8)
    safe_execute(a9)
    safe_execute(b9)
    safe_execute(c9)
    safe_execute(d9)
    safe_execute(e9)
    safe_execute(f9)
    safe_execute(g9)
    safe_execute(h9)
    safe_execute(i9)
    safe_execute(j9)
    safe_execute(a10)
    safe_execute(b10)
    safe_execute(c10)
    safe_execute(d10)
    safe_execute(e10)
    safe_execute(f10)
    safe_execute(g10)
    safe_execute(h10)
    safe_execute(i10)
    safe_execute(j10)
    safe_execute(a11)
    safe_execute(b11)
    safe_execute(c11)
    safe_execute(d11)
    safe_execute(e11)
    safe_execute(f11)
    safe_execute(g11)
    safe_execute(h11)
    safe_execute(i11)
    safe_execute(j11)
    safe_execute(a12)
    safe_execute(b12)
    safe_execute(c12)
    safe_execute(d12)
    safe_execute(e12)
    safe_execute(f12)
    safe_execute(g12)
    safe_execute(h12)
    safe_execute(i12)
    safe_execute(j12)
    safe_execute(a13)
    safe_execute(b13)
    safe_execute(c13)
    safe_execute(d13)
    safe_execute(e13)
    safe_execute(f13)
    safe_execute(g13)
    safe_execute(h13)
    safe_execute(i13)
    safe_execute(j13)
    clear()
