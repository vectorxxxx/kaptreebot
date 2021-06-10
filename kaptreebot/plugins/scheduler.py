import json
import random
import os
import nonebot
import requests
import base64
import io
from aiocqhttp import MessageSegment
from nonebot import require
from commons import property

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_api2 = props.get('tianxing_api2')
tianxing_key = props.get('tianxing_key')
tianxing_key2 = props.get('tianxing_key2')

# 定时任务配置
scheduler_path = os.getcwd() + '/properties/cheat/scheduler.properties'
scheduler_props = property.parse(scheduler_path)
group_id_greetings_list = scheduler_props.get('group_id_greetings_list')


# 深度学习过程中，需要制作训练集和验证集、测试集
def randomFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    samples = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return samples[0]


scheduler = require('nonebot_plugin_apscheduler').scheduler


# ===========早安===========
@scheduler.scheduled_job('cron', hour='8', minute='0', id='goodmorning')
async def good_morning():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        msg = '[CQ:at,qq="全体人员"] \n'
        msg += get_zaoan_img() + '\n'
        msg += get_zaoan()
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_zaoan_img():
    filepath = os.getcwd()+'/data/img/zaoan'
    if not os.path.exists(filepath):
        return ''
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print('resultpath=' + resultpath)
    sst = MessageSegment.image(file=str(resultpath))
    return sst


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


# ===========早报===========
@scheduler.scheduled_job('cron', hour='8', minute='30', id='dailynews')
async def daily_news():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        dailynews = get_daily_news()
        if daily_news == '':
            return
        msg = '早报速递：\n' + dailynews
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_daily_news():
    url = tianxing_api2 + 'bulletin/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return ''
    result = ''
    for i,val in enumerate(c['newslist']):
        result += 'Top ' + str(i + 1) + '：' + val['title'] + '\n'
    res = result.replace('<br>', '\n').replace('<br/>', '\n')[:-2]
    print(res)
    return res


# ===========干饭===========
@scheduler.scheduled_job('cron', hour='12', minute='00', id='eatlunch')
async def eat_lunch():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        lunchimg = get_lunch_img()
        if lunchimg == '':
            return
        msg = '[CQ:at,qq="全体人员"]\n' + lunchimg
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_lunch_img():
    filepath = os.getcwd()+'/data/img/lunch'
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print(resultpath)
    return resultpath

# ===========饮茶===========


@scheduler.scheduled_job('cron', hour='15', minute='00', id='drink_tea')
async def drink_tea():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        msg = '[CQ:at,qq="全体人员"] \n'
        msg += '喂！三点几啦！饮茶先~\n'
        msg += get_drink_tea_img()
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_drink_tea_img():
    filepath = os.getcwd()+'/data/img/drinktea'
    if not os.path.exists(filepath):
        return ''
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print('resultpath=' + resultpath)
    sst = MessageSegment.image(file=str(resultpath))
    return sst


# ===========放工===========


@scheduler.scheduled_job('cron', hour='17', minute='30', id='offduty')
async def off_duty():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        msg = '[CQ:at,qq="全体人员"] \n' + get_offduty_img() 
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_offduty_img():
    filepath = os.getcwd()+'/data/img/offduty'
    if not os.path.exists(filepath):
        return ''
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print('resultpath=' + resultpath)
    sst = MessageSegment.image(file=str(resultpath))
    return sst


# ===========晚安===========


@scheduler.scheduled_job('cron', hour='22', minute='0', id='goodnight')
async def good_night():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        msg = '[CQ:at,qq="全体人员"] \n'
        msg += get_wanan_img() + '\n'
        msg += get_wanan()
        for group_id in group_id_greetings_list.split(','):
            await bot.send_msg(
                message_type="group",
                group_id=int(group_id),
                message=msg
            )


def get_wanan_img():
    filepath = os.getcwd()+'/data/img/wanan'
    if not os.path.exists(filepath):
        return ''
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print('resultpath=' + resultpath)
    sst = MessageSegment.image(file=str(resultpath))
    return sst


def get_wanan():
    url = tianxing_api + 'wanan/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return '晚安~'
    result = ''
    for news in c['newslist']:
        result = news['content']
        print(result)
        return result
