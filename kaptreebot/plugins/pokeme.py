import random
from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, PokeNotifyEvent, LuckyKingNotifyEvent, GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.message import Message
from aiocqhttp import MessageSegment

import pandas as pd
import os

pk = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/poke.txt',
                sep=' ', encoding='utf-8')
print(pk)

pre = 0
poke = on_notice()
@poke.handle()
async def _(bot: Bot, event: Event):
    print("11111111111111")
    if isinstance(event, PokeNotifyEvent):
        print("22222222222222") 
        if event.is_tome() and event.get_user_id != event.self_id:
            k = (random.randint(1,10000))%len(pk)                
            result = pk.loc[k]['poke']
            print(result)
            await bot.send(
                event=event,
                message=result,
                at_sender=True
            )

ch = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui.txt',
                sep=' ', encoding='utf-8')
print(ch)

chehui = on_notice()
@chehui.handle()
async def cheh(bot: Bot, event: GroupRecallNoticeEvent):
    print(event.get_user_id + "===="+event.self_id)
    if event.get_user_id != event.self_id:
        k = (random.randint(1,10000))%len(ch)                
        result = ch.loc[k]['chehui']
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
