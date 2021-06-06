from commons import property
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
import requests
import json
import os

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key = props.get('tianxing_key')

error_info = '没有查询到呢~'

# ============每日一句============
explain = on_command("每日一句", priority=2)


@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_news()
        )


def get_news():
    url = 'https://v1.hitokoto.cn/'
    res = requests.get(url)
    c = json.loads(res.text)
    ans = c['hitokoto']+'---->'+c['from']
    print(ans)
    return ans


# ============经典对联============
duilian = on_command('经典对联', priority=2)


@ duilian.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_duilian())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_duilian():
    url = tianxing_api + 'duilian/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['content']
        print(result)
        return result


# ============古籍名句============
gjmj = on_command('古籍名句', priority=2)


@gjmj.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_gjmj())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


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


# ============经典台词============
dialogue = on_command('经典台词', priority=2)


@dialogue.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_dialogue())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_dialogue():
    url = tianxing_api + 'dialogue/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['dialogue'] + '\n'
        result += news['english'] + '\n'
        result += '------' + news['source']
        print(result)
        return result


# ============十万个为什么============

tenwhy = on_command("十万个为什么", priority=2)


@tenwhy.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            state["word"] = args  # 如果用户发送了参数则直接赋值


@tenwhy.got("word", prompt="你想了解什么知识呢~")
async def handle_city(bot: Bot, event: Event, state: dict):
    word = state["word"]
    result = await get_tenwhy(word)
    await tenwhy.finish(result)


async def get_tenwhy(word: str):
    url = tianxing_api + 'dyvideohot/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['title'] + '？\n' + news['content']
        print(result)
    return result


# ============民国句子============
mgjuzi = on_command('民国句子', priority=2)


@mgjuzi.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_mgjuzi())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


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


# ============文化谚语============
proverb = on_command('文化谚语', priority=2)


@proverb.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_proverb())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_proverb():
    url = tianxing_api + 'proverb/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['front'] + '，' + news['behind']
        print(result)
        return result


# ============健康小提示============
healthtip = on_command('健康小提示', priority=2)


@healthtip.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_healthtip())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_healthtip():
    url = tianxing_api + 'healthtip/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['content']
        print(result)
        return result


# ============故事大全============
story = on_command('故事大全', priority=2)


@story.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_story())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_story():
    url = tianxing_api + 'story/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = '『' + news['title'] + '』\n' + news['content']
        print(result)
        return result
