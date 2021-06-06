from nonebot import on_command
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from commons import property
from lxml import etree
from urllib import request, parse
import requests
import json
import os
import random

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key = props.get('tianxing_key')

error_info = '没有查询到呢~'


# ============抖音视频榜============
tiktok = on_command('抖音', aliases={'抖音热榜', '抖音视频', '抖音短视频'}, priority=2)


@tiktok.handle()
async def wzpic_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        video = get_tiktok()
        await bot.send(
            event=event,
            message=MessageSegment.video(file=str(video))
        )

# 深度学习过程中，需要制作训练集和验证集、测试集


def get_tiktok():
    url = tianxing_api + 'dyvideohot/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    url_list = []
    for news in c['newslist']:
        url_list.append(news['shareurl'])
    url_random = url_list[random.randint(0, len(url_list))]
    src_video = parse_video(url_random)
    print(src_video)
    return src_video


def parse_video(url):
    # 模拟浏览器
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
    req = request.Request(url=url, headers=header)
    res = request.urlopen(req)
    str_json = res.read().decode('utf-8')
    print('str_json=================================' + str_json)
    # src_video = str_json.xpath('//*[@id="pageletReflowVideo"]//video/@src')
    # str_video = requests.get(src_video).text
    return str_json
