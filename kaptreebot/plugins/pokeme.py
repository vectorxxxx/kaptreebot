
from nonebot import on_notice, on_command
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import PokeNotifyEvent
from aiocqhttp import MessageSegment
import pandas as pd
import os
import random

pk = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/poke.txt',
                 sep=' ', encoding='utf-8')

pre = 0
poke = on_notice()


@poke.handle()
async def _(bot: Bot, event: PokeNotifyEvent):
    if event.is_tome() and event.get_user_id != event.self_id:
        msg = ''
        ran_int = random.randint(0, 1)
        if ran_int == 0:
            k = (random.randint(1, 10000)) % len(pk)
            msg = pk.loc[k]['poke']
            print(msg)
            await bot.send(
                event=event,
                message=msg,
                at_sender=True
            )
        else:
            msg = '[CQ:poke,qq=' + event.get_user_id + ']'
            await bot.send(
                event=event,
                message=msg
            )