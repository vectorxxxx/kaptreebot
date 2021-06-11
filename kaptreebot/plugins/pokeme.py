
from nonebot import on_notice, on_command
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import PokeNotifyEvent
from aiocqhttp import MessageSegment
import pandas as pd
import os
import random

pk = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/poke.txt',
                 sep=' ', encoding='utf-8')
chehui_tome = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui_tome.txt',
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
        else:
            msg = MessageSegment.image(get_picture())
        print(msg)
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )    


def get_picture():
    filepath = os.getcwd()+'/data/img/chehui_tome'
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print(resultpath)
    return resultpath                


# 深度学习过程中，需要制作训练集和验证集、测试集
def randomFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    samples = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return samples[0]    