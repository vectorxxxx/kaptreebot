import requests
import json
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event


def get_data():
    url = 'http://www.yezishuju.com/zt/ym/'
    res = requests.get(url)
    print(res.text)
    c = json.loads(res.text)
    ans = c['data']
    print(ans)
    return ans


explain = on_command("王者赛事", priority=2)


@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=get_data()
        )
