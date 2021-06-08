from concurrent.futures import ProcessPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from nonebot.adapters.cqhttp import Bot, Event
import asyncio
import nonebot


async def day_limits():
    (bot,) = nonebot.get_bots().values()
    await bot.send_msg(
        message_type="private", user_id='1402758731', message='好困啊~'
    )


scheduler = AsyncIOScheduler()
scheduler.add_job(day_limits, 'cron', hour=2, minute=5,
                  misfire_grace_time=3600, timezone='Asia/Shanghai')

scheduler.start()

scheduler.print_jobs()

executor = ProcessPoolExecutor(1)
loop = asyncio.get_event_loop()

try:
    loop.run_forever()

except (KeyboardInterrupt, Exception):
    loop.stop()
    scheduler.shutdown()
