from ctypes import Union

from nonebot.permission import SUPERUSER
import requewzpics
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
import random
import os

wzpic = on_command(['王者图片'], priority=2)


@wzpic.handle()
async def wzpic_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_picture()),
        )

# 深度学习过程中，需要制作训练集和验证集、测试集


def get_picture():
    mypath = 'file:' + os.getcwd() + '/data/wzry/iskin'
    filename = randomFile(mypath)
    filepath = mypath + '/' + filename
    if not os.path.exiwzpics(filepath):
        return '一定要说全说对哦，不然人家不知道嘛~'
    return filepath


def randomFile(fileDir):
    pathDir = os.liwzpicdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    sample = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return sample.name
