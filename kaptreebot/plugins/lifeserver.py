import requests
import json
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event


epidemic = on_command("新冠疫情", priority=2)


@epidemic.handle()
async def epidemicsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_epidemic()
        )


def get_epidemic():
    url = 'http://api.tianapi.com/txapi/ncov/index?key=47db9de470a633072e5c20d93860b434'
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return '没有查询到呢~'
    results = ''
    desc = ''
    foreignStatistics = ''
    globalStatistics = ''
    for news in c['newslist']:
        results += '▶ 国内疫情\n\n'
        for n in news['news']:
            results += '◤' + n['pubDateStr'] + '\n'
            results += n['title'] + '\n'
            results += n['summary']+'\n'
            results += '◣' + n['infoSource'] + '\n'
            results += '\n▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n\n'
        desc = news['desc']
        results += '『累计确诊』 ' + str(desc['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + str(desc['currentConfirmedCount']) + '例\n'
        results += '『[疑似确诊』 ' + str(desc['suspectedCount']) + '例\n'
        results += '『治愈病例』 ' + str(desc['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(desc['deadCount']) + '例\n'
        results += '『无症状感染』 ' + str(desc['seriousCount']) + '例\n'
        results += '\n▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n\n'
        if desc['remark1'] != '':
            results += desc['remark1'] + '\n\n'
        if desc['remark2'] != '':
            results += desc['remark2'] + '\n\n'
        if desc['remark3'] != '':
            results += desc['remark3'] + '\n\n'
        if desc['remark4'] != '':
            results += desc['remark4'] + '\n\n'
        if desc['remark5'] != '':
            results += desc['remark5'] + '\n\n'
        if desc['note1'] != '':
            results += desc['note1'] + '\n\n'
        if desc['note2'] != '':
            results += desc['note2'] + '\n\n'
        if desc['note3'] != '':
            results += desc['note3'] + '\n\n'
        if desc['generalRemark'] != '':
            results += desc['generalRemark'] + '\n\n'
        if desc['abroadRemark'] != '':
            results += desc['abroadRemark'] + '\n\n'
        results += '\n▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n'
        # 海外疫情
        results += '\n▶ 海外疫情\n\n'
        foreignStatistics = desc['foreignStatistics']
        results += '『累计确诊』 ' + \
            str(foreignStatistics['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + \
            str(foreignStatistics['currentConfirmedCount']) + '例\n'
        results += '『疑似病例』 ' + \
            str(foreignStatistics['suspectedCount']) + '例\n'
        results += '『治愈病例』 ' + str(foreignStatistics['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(foreignStatistics['deadCount']) + '例\n'
        # 全球疫情
        results += '\n▶ 全球疫情\n\n'
        globalStatistics = desc['globalStatistics']
        results += '『累计确诊』 ' + str(globalStatistics['confirmedCount']) + '例\n'
        results += '『现存确诊』 ' + \
            str(globalStatistics['currentConfirmedCount']) + '例\n'
        results += '『治愈病例』 ' + str(globalStatistics['curedCount']) + '例\n'
        results += '『死亡病例』 ' + str(globalStatistics['deadCount']) + '例\n'
    print(results)
    return results


# Test
get_epidemic()
