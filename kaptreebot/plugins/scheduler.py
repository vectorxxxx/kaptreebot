from nonebot import require
from aiocqhttp import MessageSegment
import nonebot
import os

scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour='3', minute='8', id='goodm')
async def day_limits():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        imgpath = 'file:///'+os.getcwd()+'/data/img/hello.gif'
        msg = '[CQ:at,qq="全体人员"] 早上好呀，小哥哥们~\n' + MessageSegment.image(imgpath)
        await bot.send_msg(
            message_type="group",
            group_id=582597352,
            message=msg
        )


# scheduler.add_job(day_limits,  "interval", days=1, id="goodm")
