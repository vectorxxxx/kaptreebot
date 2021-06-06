import requests
import json
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
from commons import property
import requests
import json
import os

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_api2 = props.get('tianxing_api2')
tianxing_key = props.get('tianxing_key')

error_info = '没有查询到呢~'

# ============新冠疫情============
epidemic = on_command("新冠疫情", priority=2)


@epidemic.handle()
async def epidemicsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_epidemic()
        )


def get_epidemic():
    url = tianxing_api + 'ncov/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    results = ''
    desc = ''
    foreignStatistics = ''
    globalStatistics = ''
    results += ' ░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
    for news in c['newslist']:
        results += '◎ 国内疫情\n'
        for n in news['news']:
            results += '★' + n['pubDateStr'] + '\n'
            results += '#' + n['title'] + '\n'
            results += n['summary']+'\n'
            results += '@' + n['infoSource'] + '\n'
            results += '――――――――――――――――――――――――――――\n'
        desc = news['desc']
        results += '『累计确诊』 ' + str(desc['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + str(desc['currentConfirmedCount']) + '例\n'
        results += '『[疑似确诊』 ' + str(desc['suspectedCount']) + '例\n'
        results += '『治愈病例』 ' + str(desc['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(desc['deadCount']) + '例\n'
        results += '『无症状感染』 ' + str(desc['seriousCount']) + '例\n'
        results += ' ――――――――――――――――――――――――――――\n'
        if desc['remark1'] != '':
            results += desc['remark1'] + '\n'
        if desc['remark2'] != '':
            results += desc['remark2'] + '\n'
        if desc['remark3'] != '':
            results += desc['remark3'] + '\n'
        if desc['remark4'] != '':
            results += desc['remark4'] + '\n'
        if desc['remark5'] != '':
            results += desc['remark5'] + '\n'
        if desc['note1'] != '':
            results += desc['note1'] + '\n'
        if desc['note2'] != '':
            results += desc['note2'] + '\n'
        if desc['note3'] != '':
            results += desc['note3'] + '\n'
        if desc['generalRemark'] != '':
            results += desc['generalRemark'] + '\n'
        if desc['abroadRemark'] != '':
            results += desc['abroadRemark'] + '\n'
        results += ' ░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        # 海外疫情
        results += '◎ 海外疫情\n'
        foreignStatistics = desc['foreignStatistics']
        results += '『累计确诊』 ' + \
            str(foreignStatistics['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + \
            str(foreignStatistics['currentConfirmedCount']) + '例\n'
        results += '『疑似病例』 ' + \
            str(foreignStatistics['suspectedCount']) + '例\n'
        results += '『治愈病例』 ' + str(foreignStatistics['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(foreignStatistics['deadCount']) + '例\n'
        results += ' ░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
        # 全球疫情
        results += '◎ 全球疫情\n'
        globalStatistics = desc['globalStatistics']
        results += '『累计确诊』 ' + str(globalStatistics['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + \
            str(globalStatistics['currentConfirmedCount']) + '例\n'
        results += '『治愈病例』 ' + str(globalStatistics['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(globalStatistics['deadCount']) + '例\n'
    print(results)
    return results


# ============微信热点============

wxhottopic = on_command('微信热点', priority=2)


@wxhottopic.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_wxhottopic())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_wxhottopic():
    url = tianxing_api + 'wxhottopic/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += 'Top' + str(news['index'] + 1) + '：' + news['word'] + '\n'
    return result


# ============每日简报============
bulletin = on_command('每日简报', priority=2)


@bulletin.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_bulletin())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


def get_bulletin():
    url = tianxing_api2 + 'bulletin/index?key=' + tianxing_key
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += '@' + news['mtime'] + '\n'
        result += '#' + news['title'] + '\n'
        print(result)
    return result
