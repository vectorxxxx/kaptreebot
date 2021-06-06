
from nonebot import on_notice, on_command
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


# # 撤回自己的消息
# chehui = on_command('撤回', priority=2)


# @chehui.handle()
# async def chehui_(bot: Bot, event: Event):
#     if event.get_user_id != event.self_id:
#         try:
#             await bot.delete_msg(
#                 message_id=event.self_id
#             )
#         except:
#             await withdraw.finish('撤回失败，可能已超时')
