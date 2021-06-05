#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import urllib
import urllib.parse
import urllib.request
import random
import os

from nonebot import on_message, on_command
from nonebot.adapters.cqhttp import Bot, Event, Message, PRIVATE
from commons import property

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/cheat.properties'
# 读取文件
props = property.parse(file_path)


# def get_n(text):
#     if text.find('知酱') != -1:
#         text = text.replace('知酱','')
#         return get_n0(text)
#     if text.find('灵酱') != -1:
#         text = text.replace('灵酱','')
#         return get_n1(text)
#     if text.find('思酱') != -1:
#         text = text.replace('思酱','')
#         return get_n2(text)
#     num = random.randint(0, 2)
#     if num == 0:
#         return get_n0(text)
#     if num == 1:
#         return get_n1(text)
#     if num == 2:
#         return get_n2(text)


# 认知机器人
ren_zhi_url = props.get('ren_zhi_url')
ren_zhi_appid = props.get('ren_zhi_appid')
ren_zhi_appkey = props.get('ren_zhi_appkey')
ren_zhi_ip = props.get('ren_zhi_ip')
ren_zhi_userid = props.get('ren_zhi_userid')


def get_n(text):
    try:
        # 定义请求数据，并且对数据进行赋值
        values = {}
        values['key'] = ren_zhi_appkey
        values['msg'] = text.encode('utf-8')
        values['ip'] = ren_zhi_ip
        values['userid'] = ren_zhi_userid
        values['appid'] = ren_zhi_appid
        # 对请求数据进行编码
        data = urllib.parse.urlencode(values)
        # 将数据与url进行拼接
        req = ren_zhi_url + '?' + data
        print(req)
        r = requests.post(req)
        # 中文编码格式打印数据
        result = r.content.decode('utf-8')
        if result == '亲爱的用户您好。您当天的授权用量已用完(或未升级成会员)，请到平台升级会员，或者等明天可继续使用机器人大脑。有任何疑问，请您登陆官网联系客服服务。www.weilaitec.com。':
            return get_n1(text)
        print('知酱：' + result)
        return result
    except TypeError:
        return '完了完了，突然好难受啊，小知感觉整个人都不好了~~'


# 图灵机器人
tuling_url = props.get('tuling_url')
tuling_apiKey = props.get('tuling_apiKey')
tuling_userId = props.get('tuling_userId')


def get_n1(text_input: str):
    try:
        api_url = tuling_url
        print(api_url)
        req = {
            "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
            "perception":  # 信息参数
            {
                "inputText":  # 文本信息
                {
                    "text": text_input
                },

                "selfInfo":  # 用户参数
                {
                    "location":
                    {
                        "city": "苏州",  # 所在城市
                        "province": "江苏",  # 省份
                        "street": "香山"  # 街道
                    }
                }
            },
            "userInfo":
            {
                "apiKey": tuling_apiKey,  # 改为自己申请的key
                "userId": tuling_userId  # 用户唯一标识(随便填, 非密钥)
            }
        }
        # 将字典格式的req编码为utf8
        req = json.dumps(req).encode('utf8')
        http_post = urllib.request.Request(api_url, data=req, headers={
                                           'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        response_dic = json.loads(response_str)
        intent_code = response_dic['intent']['code']
        results_text = response_dic['results'][0]['values']['text']
        if str(results_text) == '请求次数超限制!':
            return get_n2(text_input)
        print('灵酱：', results_text)
        return str(results_text)
    except KeyError:
        print(KeyError)
        if KeyError == '4003':
            return '今天的智能对话次数用完了呢QAQ,请输入help查看其他玩法叭'
        else:
            return '来大姨妈了，不想理你~'


# 小思机器人
sizhi_url = props.get('sizhi_url')
sizhi_appid = props.get('sizhi_appid')
sizhi_userid = props.get('sizhi_userid')


def get_n2(text):
    try:
        data = {
            "spoken": text,
            "appid": sizhi_appid,
            "userid": sizhi_userid
        }
        r = requests.post(sizhi_url, data=json.dumps(data))
        result = json.loads(r.content)
        message = result['data']['info']['text']
        if 'heuristic' in result['data']['info'] and result['data']['info']['heuristic']:
            for item in result['data']['info']['heuristic']:
                message += ',  ' + item
        print('思酱：', message)
        return message
    except KeyError:
        return '这个问题好头疼呀，问点别的叭'
    except BaseException:
        return '呸！渣男~'


tuling = on_message(priority=5)  # permission= PRIVATE


@tuling.handle()
async def cheatt_(bot: Bot, event: Event):
    if event.is_tome():
        print("YES")
    if event.is_tome() and event.user_id != event.self_id:
        mysay = event.get_message()
        mysay = get_n(str(mysay))
        await bot.send(
            event=event,
            message=mysay
        )
