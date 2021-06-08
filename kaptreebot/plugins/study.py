from commons import property
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
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

# ============经典对联============
duilian = on_command('每日对联', priority=2)


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

# ============经典台词============
dialogue = on_command('每日台词', priority=2)


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

tenwhy = on_command("每日百科", priority=2)


@tenwhy.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            state["word"] = args  # 如果用户发送了参数则直接赋值


@tenwhy.got("word", prompt="你想了解什么知识呢，请输入关键字哦~")
async def handle_city(bot: Bot, event: Event, state: dict):
    word = state["word"]
    result = await get_tenwhy(word)
    await tenwhy.finish(result)


async def get_tenwhy(word: str):
    url = tianxing_api + 'dyvideohot/index?key=' + tianxing_key + '&word=' + word
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news.get('title') + '？ \n' + news.get('content')
        print(result)
    return result


# ============文化谚语============
proverb = on_command('每日谚语', priority=2)


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

# ============故事大全============
story = on_command('每日故事', priority=2)


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

# ============歇后语============
xiehou = on_command('歇后语', priority=2)


@xiehou.handle()
async def getxiehou_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_xiehou())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_xiehou():
    url = tianxing_api + 'xiehou/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result = news['quest'] + '——' + news['result']
        print(result)
        return result

# ============简说历史============
pitlishi = on_command('每日历史', priority=2)


@pitlishi.handle()
async def getpitlishi_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_pitlishi())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_pitlishi():
    url = tianxing_api + 'pitlishi/index?key=' + tianxing_key2
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['content'] +'\n'
    res = result.replace('<br>','\n').replace('<br/>','\n')[:-2]    
    print(res)
    return res

# ============唐诗大全============
poetries = on_command('每日唐诗', priority=2)


@poetries.handle()
async def getpoetries_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_poetries())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_poetries():
    url = tianxing_api + 'poetries/index?key=' + tianxing_key2 + '&num=1&page=' + str(random.randint(0, 40000))
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['content'] +'\n'
    res = result.replace('<br>','\n').replace('<br/>','\n').replace('。','。\n')[:-2]    
    print(res)
    return res



# ============健康小提示============
healthtip = on_command('每日健康', priority=2)


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
