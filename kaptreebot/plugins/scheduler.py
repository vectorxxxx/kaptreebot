from nonebot import require
import nonebot

scheduler = require('nonebot_plugin_apscheduler').scheduler


@scheduler.scheduled_job('cron', hour='2', minute='25', id='drink_tea')
async def day_limits():
    (bot,) = nonebot.get_bots().values()
    if bot is not None:
        await bot.send_msg(
            message_type="private", user_id='1402758731', message='好困啊~'
        )

scheduler.add_job(day_limits,  "interval", days=1, id="xxx")
