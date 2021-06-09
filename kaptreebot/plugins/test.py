#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nonebot.adapters.cqhttp import Bot, Event
from nonebot import on_command
import json
import requests
import os
import random
from prettytable import PrettyTable

url = 'https://v1.hitokoto.cn/?c=j&c=k'
res = requests.get(url)
c = json.loads(res.text)
ans = c['hitokoto']+'---->'+c['from']
print(ans)
# url='https://chp.shadiao.app/api.php'
# headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
#     }
# t = requests.get(url,headers=headers)
#
# print(t.text)
# print('朋友圈文案+',str1)
#
# url ='https://v1.hitokoto.cn/'
# res = requests.get(url)
# c = json.loads(res.text)
# ans = c['hitokoto']+'---->'+c['from']
# print(ans)

# import json
# import urllib.request
# while 1:
#     try:
#         api_url = "http://openapi.tuling123.com/openapi/api/v2"
#         text_input = input('Mangata：')
#         if text_input == 'exit':
#             break
#         req = {
#             "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
#             "perception":  # 信息参数
#             {
#                 "inputText":  # 文本信息
#                 {
#                     "text": text_input
#                 },
#
#                 "selfInfo":  # 用户参数
#                 {
#                     "location":
#                     {
#                         "city": "南充",  # 所在城市
#                         "province": "四川",  # 省份
#                         "street": "顺庆区"  # 街道
#                     }
#                 }
#             },
#             "userInfo":
#             {
#                 "apiKey": "92f3cf04b7444a00a543e8cff93c6a13",  # 改为自己申请的key
#                 "userId": "0001"  # 用户唯一标识(随便填, 非密钥)
#             }
#         }
#         # print(req)
#         # 将字典格式的req编码为utf8
#         req = json.dumps(req).encode('utf8')
#         # print(req)
#         http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
#         response = urllib.request.urlopen(http_post)
#         response_str = response.read().decode('utf8')
#         # print(response_str)
#         response_dic = json.loads(response_str)
#         # print(response_dic)
#         intent_code = response_dic['intent']['code']
#         results_text = response_dic['results'][0]['values']['text']
#         print('kaptree：', results_text)
#         # print('code：' + str(intent_code))
#     except KeyError:
#         print('出错啦~~, 下次别问这样的问题了')


# mypath = os.getcwd()+'/data/wzry/voice/妲己'
# pathDir = os.listdir(mypath)  # 取图片的原始路径
# sample = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
# print(sample[0])

# 菜单
table = PrettyTable(['序号', '命令', '示例'])
table.add_row(['1', '句子', '每日一句'])
table.add_row(['2', '天气', '天气 成都'])
table.add_row(['3', '翻译', '翻译 中出'])
table.add_row(['4', '戳一戳', '戳头像'])
table.add_row(['5', '图片', 'R18'])
table.add_row(['6', '抱抱', '我要抱抱'])
table.add_row(['7', '语录', '开始网抑'])
table.add_row(['8', '王者', '王者图片/语音'])
table.add_row(['9', '注意', '群聊@我或/'])
table.add_row(['10', '更多', '请体验触发'])
print(str(table))