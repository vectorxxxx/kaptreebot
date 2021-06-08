from nonebot import on_command, on_keyword
from nonebot import rule
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from requests_html import HTMLSession
from commons import property
import requests
import random
import json
import os

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key = props.get('tianxing_key')
tianxing_key2 = props.get('tianxing_key2')


def get_qinhua():
    url = 'https://api.lovelive.tools/api/SweetNothings/1/Serialization/Text?genderType=M'
    res = requests.get(url)
    print('情话:', res.text)
    return str(res.text)


def get_lvcha():
    url = 'https://api.lovelive.tools/api/SweetNothings/1/Serialization/Text?genderType=F'
    res = requests.get(url)
    print('绿茶:', res.text)
    return str(res.text)


def get_news():
    url = 'https://api.ixiaowai.cn/tgrj/index.php'
    res = requests.get(url)
    b = res.text
    c = b.replace('*', '')
    print('情感语录1:', c)
    return c


def get_new2():
    url = 'https://du.liuzhijin.cn/dog.php'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    r = session.get(url, headers=headers)
    sel = '#text'
    s = r.html.find(sel)
    str1 = s[0].text
    print('情感语录2:', str1)
    return str1


exlpain = on_command('每日必舔', priority=2)


@exlpain.handle()
async def slove(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = ''
        if random.randint(0, 2) == 0:
            str1 = get_new2()
        else:
            str1 = get_news()
        await bot.send(
            event=event,
            message=str1,
            at_sender=True
        )

qinghua = on_command('每日情话', priority=2)


@qinghua.handle()
async def qinghua_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_qinhua()
        )

lvcha = on_command('每日绿茶', priority=2)


@lvcha.handle()
async def lvcha_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_lvcha()
        )


# ============古代情诗============
error_info = '没有查询到呢~'

qingshi = on_command('每日情诗', priority=2)


@qingshi.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_qingshi())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_qingshi():
    url = tianxing_api + 'qingshi/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['content'] + '\n'
        result += '---《' + news['source'] + '》' + news['author']
        print(result)
        return result

# ============土味情话============

saylove = on_command('每日土味', priority=2)


@saylove.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_saylove())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_saylove():
    url = tianxing_api + 'saylove/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['content']
        res = result.replace('<br>','\n').replace('<br/>','\n')
        print(res)
        return res
