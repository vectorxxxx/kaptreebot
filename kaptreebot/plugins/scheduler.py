import asyncio
from concurrent.futures import ProcessPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from nonebot.adapters.cqhttp import Bot, Event


async def day_limits(bot: Bot, event: Event):
    await bot.send(
        event=event,
        message='好困啊',
        kwargs={'user_id','1402758731'}
    )


if __name__ == "__main__":

    variable = 60

    scheduler = AsyncIOScheduler()
    scheduler.add_job(day_limits, 'cron', hour=1, minute=10,
                      misfire_grace_time=3600, timezone='Asia/Shanghai', kwargs={Bot, Event})

    scheduler.start()

    scheduler.print_jobs()

    executor = ProcessPoolExecutor(1)
    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()

    except (KeyboardInterrupt, Exception):
        loop.stop()
        scheduler.shutdown()
