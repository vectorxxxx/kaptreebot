from commons import property
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
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
gjmj = on_command('经典名句', priority=2)


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


# ============百科题库============
baiketiku = on_command('每日一题', priority=2)


@baiketiku.handle()
async def handle_baiketiku_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数


@baiketiku.got("answer", args_parser='get_baiketiku')
async def handle_baiketiku(bot: Bot, event: Event, state: dict):
    answer = ''
    answer_check = await get_check(answer)
    print(answer_check)
    await baiketiku.finish(answer_check)


answerReal = ''
analyticReal = ''

# 出题


def get_baiketiku():
    url = tianxing_api + 'baiketiku/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += '请听题：' + news['title'] + '\n'
        result += 'A.' + news['answerA'] + '\n'
        result += 'B.' + news['answerB'] + '\n'
        result += 'C.' + news['answerC'] + '\n'
        result += 'D.' + news['answerD'] + '\n'
        answerReal = news['answer']
        analyticReal = news['analytic']
        print(result)
        return result

# 回答


def get_check(answer):
    if answer != answerReal:
        return '回答错误'
    result = '正确答案是：'+answerReal + '\n' + analyticReal
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
