from nonebot.permission import SUPERUSER
import random
import os
from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment

lines = on_keyword(["王者语音", '王者台词', '王者音效', "王者荣耀语音", '王者荣耀台词',
                   '王者荣耀音效', "农药语音", '农药台词', '农药音效'], priority=2)


@lines.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        print('args=' + args)
        if args:
            state["heroname"] = args  # 如果用户发送了参数则直接赋值


@lines.got("heroname", prompt="请选择您的英雄")
async def handle_hero(bot: Bot, event: Event, state: dict):
    heroname = state["heroname"]
    hero_voice = await get_hero(heroname)
    await lines.finish(hero_voice)


async def get_hero(heroname: str):
    filepath = os.getcwd()+'/data/wzry/voice/' + heroname
    print('filepath=' + filepath)
    if not os.path.exists(filepath):
        return '一定要说对说全哦，不然人家不知道哒~'
    sample = randomFile(filepath)
    resultpath = 'file:///'+filepath + '/' + sample
    print('resultpath=' + resultpath)
    sst = MessageSegment.record(file=str(resultpath))
    return sst


# 深度学习过程中，需要制作训练集和验证集、测试集
def randomFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    samples = random.sample(pathDir, 1)  # 随机选取picknumber数量的样本图片
    return samples[0]


wzpic = on_keyword(['王者图片', '王者荣耀图片', '农药图片', '王者皮肤',
                   '王者荣耀皮肤', '农药皮肤'], priority=2)


@wzpic.handle()
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
    resultpath = 'file:///'+filepath + '/' + sample
    print(resultpath)
    return resultpath