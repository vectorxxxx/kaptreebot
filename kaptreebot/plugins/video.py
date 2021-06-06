from nonebot import on_command
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from commons import property
from lxml import etree
import requests
import json
import os
import re

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
    url = ''
    for news in c['newslist']:
        url = news['shareurl']
        print(url)
    url_video = parse_video(url)
    return url_video


def parse_video(url):
    header = {}
    text = requests.get(url, headers=header).text
    dom = etree.HTML(text)
    url_video = dom.xpath('//div[@id="pageletReflowVideo"]/video/@src')
    print(url_video)
    return url_video
