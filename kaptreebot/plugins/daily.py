from commons import property
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
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
tianxing_key2 = props.get('tianxing_key2')

error_info = '没有查询到呢~'

# ============每日一句============
explain = on_command("每日一句", priority=2)


@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        num = random.randint(0,5)
        msg = ''
        if num==0:
            msg = get_news()
        if num==1:
            msg = get_gjmj()
        if num==2:
            msg = get_mgjuzi()
        if num==3:
            msg = get_mingyan()

        await bot.send(
            event=event,
            message=msg
        )

# ============每日一句============
def get_news():
    url = 'https://v1.hitokoto.cn/'
    res = requests.get(url)
    c = json.loads(res.text)
    ans = c['hitokoto']+'------'+c['from']
    print(ans)
    return ans


# ============古籍名句============
def get_gjmj():
    url = tianxing_api + 'gjmj/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['content'] + '\n------' + news['source']
        print(result)
        return result


# ============民国句子============
def get_mgjuzi():
    url = tianxing_api + 'mgjuzi/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['content'] + '\n------' + news['author']
        print(result)
        return result

# ============名人名言============
def get_mingyan():
    url = tianxing_api + 'mingyan/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['content'] +'------' + news['author'] 
    res = result.replace('<br>','\n').replace('<br/>','\n')
    print(res)
    return res


# ============英语一句话============
ensentence = on_command('每日英语', priority=2)


@ensentence.handle()
async def getensentence_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_ensentence())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_ensentence():
    url = tianxing_api + 'ensentence/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['en'] +'\n' + news['zh'] 
    res = result.replace('<br>','\n').replace('<br/>','\n')
    print(res)
    return res
