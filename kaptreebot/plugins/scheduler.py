from nonebot import require
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
import os

scheduler = require('nonebot_plugin_apscheduler').scheduler

@scheduler.scheduled_job('cron', hour='* 26 18 * * ?', id='drink_tea', args=[1])
async def run_at_3pm(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        pic = get_picture()
        await bot.send(
            event=event,
            message=MessageSegment.image(pic),
        )

def get_picture():
    filepath = os.getcwd()+'/data/wzry/skin'
    resultpath = 'file:///'+filepath + '/drink_tea.jpb'
    print(resultpath)
    return resultpath


scheduler.add_job('饮茶', "interval", days=1, id="drink_tea")

