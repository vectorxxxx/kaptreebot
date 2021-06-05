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
            state["heroname"] = args  # 如果用户发送了参数则直接赋值


@lines.got("heroname", prompt="请选择您的英雄")
async def handle_hero(bot: Bot, event: Event, state: dict):
    heroname = state["heroname"]
    hero_voice = await get_hero(heroname)
    await lines.finish(hero_voice)


async def get_hero(heroname: str):
    filepath = os.getcwd()+'/data/wzry/voice/' + heroname
    if not os.path.exists(filepath):
        return '一定要说对说全哦，不然人家不知道哒~'
    sample = randomFile(filepath)
    resultpath = filepath + '/' + sample
    print(resultpath)
    sst = MessageSegment.record(file=str(resultpath))
    return sst


# 深度学习过程中，需要制作训练集和验证集、测试集
def randomFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    samples = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return samples[0]
