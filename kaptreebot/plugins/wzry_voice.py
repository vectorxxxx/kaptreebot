import random
import os
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment

lines = on_command("王者语音", priority=2)


@lines.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            print(args)
            state["hero"] = args  # 如果用户发送了参数则直接赋值


@lines.got("hero", prompt="请选择您的英雄")
async def handle_hero(bot: Bot, event: Event, state: dict):
    hero = state["hero"]
    hero_voice = await get_hero(hero)
    print(hero_voice)
    await lines.finish(hero_voice)


async def get_hero(hero: str):
    path_ = os.getcwd()
    path_ = path_+'\data\wzry\voice'
    mypath = 'file:///'+path_
    filename = randomFile(mypath)
    print(filename)
    if not os.path.exists(mypath + filename):
        return '一定要说全说对哦，不然人家不知道嘛~'
    sst = MessageSegment.record(file=str(filename))
    return sst


# 深度学习过程中，需要制作训练集和验证集、测试集
def randomFile(fileDir):
    pathDir = os.listdir(fileDir.encode("utf-8"))  # 取图片的原始路径
    for fileName in pathDir:
        print(fileName)
    sample = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    print(sample)
    return sample.name
