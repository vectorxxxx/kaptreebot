import random
import pandas as pd
import os

from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, PokeNotifyEvent, LuckyKingNotifyEvent, GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.message import Message
from aiocqhttp import MessageSegment

a = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/poke.txt',
                sep=' ', encoding='utf-8')
print(a)

pre = 0
poke = on_notice()
@poke.handle()
async def _(bot: Bot, event: Event):
    if isinstance(event, PokeNotifyEvent):
        if event.is_tome() and event.get_user_id != event.self_id:
            l = len(a)
            k = random.randint(0, l-1)
            while pre == k:
                k = random.randint(0, l-1)
            last = k
            result = a[k]
            print(result)
            await bot.send(
                event=event,
                message=result,
                at_sender=True
            )

b = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui.txt',
                sep=' ', encoding='utf-8')
print(b)

chehui = on_notice()
@chehui.handle()
async def cheh(bot: Bot, event: GroupRecallNoticeEvent):
    if event.get_user_id != event.self_id:
        l = len(b)
        k = random.randint(0, l-1)
        result = b[k]
        print(result)
        await bot.send(
            event=event,
            message=result,
            at_sender=True
        )

regbag = on_notice()
@regbag.handle()
async def redb(bot: Bot, event: LuckyKingNotifyEvent):
    atmsg = MessageSegment.at(event.target_id)
    await bot.send(
        event=event,
        message=atmsg+'恭喜你是运气王',
    )
