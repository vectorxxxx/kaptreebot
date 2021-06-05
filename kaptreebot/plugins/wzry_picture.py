from ctypes import Union

from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
import random
import os

wzpic = on_command('王者图片', priority=2)


@ wzpic.handle()
async def wzpic_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        pic = get_picture(event.message)
        await bot.send(
            event=event,
            message=MessageSegment.image(pic),
        )

# 深度学习过程中，需要制作训练集和验证集、测试集


def get_picture(heroname):
    filepath = os.getcwd()+'/data/wzry/skin'
    sample = randomFile(filepath)
    resultpath = filepath + '/' + sample
    print(resultpath)
    return resultpath


def randomFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    sample = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return sample[0]
