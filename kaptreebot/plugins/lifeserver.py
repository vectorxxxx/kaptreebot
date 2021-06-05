import requests
import json
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event


epidemic = on_command("国内疫情", priority=2)


@epidemic.handle()
async def epidemicsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_news()
        )


def get_news():
    url = 'http://api.tianapi.com/txapi/ncov/index?key=47db9de470a633072e5c20d93860b434'
    res = requests.get(url)
    c = json.loads(res.text)
    print(c)
    if c['code'] != 200:
        return '没有查询到呢~'
    results = ''
    for news in c['newslist']:
        for n in news['news']:
            results += '[glow=255,gray,1]' + n['pubDateStr'] + '[/glow]\n'
            results += '[B][glow=255,black,3]'+n['title'] + '[/glow][/B]\n'
            results += n['summary']+'\n'
            results += '[glow=255,gray,1]' + n['infoSource'] + '[/glow]\n'
            results += '---------------------------\n'
    print(results)
    return results
