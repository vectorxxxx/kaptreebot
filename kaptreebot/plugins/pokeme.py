
from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import PokeNotifyEvent

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
        k = (random.randint(1, 10000)) % len(pk)
        result = pk.loc[k]['poke']
        print(result)
        await bot.send(
            event=event,
            message=result,
            at_sender=True
        )
