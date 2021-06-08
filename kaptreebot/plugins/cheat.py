#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import urllib
import urllib.parse
import urllib.request
import os

from nonebot import on_message, on_command
from nonebot.adapters.cqhttp import Bot, Event, Message, PRIVATE
from commons import property
from aiocqhttp import MessageSegment


# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/cheat.properties'
# 读取文件
props = property.parse(file_path)


tuling = on_message(priority=10)  # permission= PRIVATE


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

def get_n(text):
    flag = False
    if not flag:
        result = get_ren_zhi(text)
        if '升级会员' in result or '参数有误' in result:
            flag = True
    if flag:
        flag = False
        result = get_tuling(text)
        if str(result) == '请求次数超限制!':
            flag = True
    if flag:
        flag = False
        result = get_tianxing(text)
        if str(result) == '请求次数超限制!':
            flag = True
    if flag:
        result = get_sizhi(text)
    return result    
    


# 认知机器人
ren_zhi_url = props.get('ren_zhi_url')
ren_zhi_appid = props.get('ren_zhi_appid')
ren_zhi_appkey = props.get('ren_zhi_appkey')
ren_zhi_ip = props.get('ren_zhi_ip')
ren_zhi_userid = props.get('ren_zhi_userid')


def get_ren_zhi(text):
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
        print('认知机器人：' + result)
        return result
    except (TypeError, KeyError) as e:
        print('认知机器人异常')
        return get_tuling(text)


# 图灵机器人
tuling_url = props.get('tuling_url')
tuling_apiKey = props.get('tuling_apiKey')
tuling_userId = props.get('tuling_userId')


def get_tuling(text_input: str):
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
        intent_operateState = response_dic['intent']['operateState']
        print(intent_code)
        print(intent_operateState)
        results_text = response_dic['results'][0]['values']['text']
        print('图灵机器人：', results_text)
        return str(results_text)
    except KeyError:
        print('图灵机器人异常')
        return get_sizhi(text_input)


# 小思机器人
sizhi_url = props.get('sizhi_url')
sizhi_appid = props.get('sizhi_appid')
sizhi_userid = props.get('sizhi_userid')


def get_sizhi(text):
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
        print('思知机器人：', message)
        return message
    except KeyError:
        return '这个问题好头疼呀，问点别的叭'
    except BaseException:
        print('思知机器人异常')
        return '呸！渣男~'

# 天行机器人
file_path = os.getcwd() + '/properties/cheat/others.properties'
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key2 = props.get('tianxing_key2')


def get_tianxing(text):
    try:
        url = tianxing_api + '?key=' + tianxing_key2 + '&question=' + text
        r = requests.get(url)
        result = json.loads(r.text)
        data = result['newslist']
        datatype = data['datatype']
        reply = data['reply']
        print('思酱：', reply)
        # 返回类型判断
        if datatype == 'text':
            return reply
        elif datatype == 'image':
            return MessageSegment.image(reply)
        elif datatype == 'video':
            return MessageSegment.video(reply)
        elif datatype == 'sound':
            return MessageSegment.record(reply)     
    except KeyError:
        return '人家不想回答~'
    except BaseException:
        print('天行机器人异常')
        return '呸！渣男~'

