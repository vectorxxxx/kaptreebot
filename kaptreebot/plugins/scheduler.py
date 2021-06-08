import json
import requests
from commons import property
from nonebot import require
from aiocqhttp import MessageSegment
import nonebot
import os


# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key2 = props.get('tianxing_key2')


scheduler = require('nonebot_plugin_apscheduler').scheduler


# ===========早安===========
@scheduler.scheduled_job('cron', hour='3', minute='30', id='goodmorning')
async def good_morning():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        imgpath = 'file:///'+os.getcwd()+'/data/img/hello.gif'
        msg = '[CQ:at,qq="全体人员"] \n'
        msg += get_zaoan()
        msg += MessageSegment.image(imgpath)
        await bot.send_msg(
            message_type="group",
            group_id=582597352,
            message=msg
        )


def get_zaoan():
    url = tianxing_api + 'zaoan/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return '早上好呀，小哥哥们~'
    result = ''
    for news in c['newslist']:
        result = news['content']
        print(result)
        return result
