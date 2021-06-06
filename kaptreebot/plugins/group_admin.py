from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import GroupIncreaseNoticeEvent
from nonebot.adapters.cqhttp.event import GroupUploadNoticeEvent
from nonebot.adapters.cqhttp.event import GroupDecreaseNoticeEvent
from nonebot.adapters.cqhttp.event import GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.event import LuckyKingNotifyEvent
from aiocqhttp import MessageSegment

import pandas as pd
import os
import random

chehui_tome = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui_tome.txt',
                          sep=' ', encoding='utf-8')

# 将函数注册为群成员增加通知处理器

# 入群提醒
increase = on_notice()


@increase.handle()
async def increase(bot: Bot, event: GroupIncreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = '哇~是新的rbq！'
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )


# 退群提醒
decrease = on_notice()


@decrease.handle()
async def decrease(bot: Bot, event: GroupDecreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = '离开了，好难过~'
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )

# 上传提醒
upload = on_notice()


@upload.handle()
async def upload(bot: Bot, event: GroupUploadNoticeEvent):
    if event.get_user_id != event.self_id:
        filename = str(event.file.name)
        format = judge_file_format(filename)
        msg = '上传了' + format + '：\n' + filename + '\n好想打开看看呀~'
        print(msg)
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )

img_format = ['bmp', 'jpg', 'png', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd',
              'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw', 'WMF', 'webp', 'avif']

audio_format = ['cd', 'wave', 'aiff', 'mpeg', 'mp3', 'mpeg-4', 'midi',
                'wma', 'ra', 'rm', 'rmx', 'vqf', 'amr', 'ape', 'flac', 'aac']

video_format = ['mpg', 'mlv', 'mpe', 'mpeg', 'm2v', 'avi', 'navi', 'asf', 'mov', 'wmv',
                '3gp', 'rm', 'rmvb', 'flv', 'f4v', 'mp4', 'mkv', 'mtv', 'dat', 'dmv']


def judge_file_format(filename):
    # 文件夹
    dot_index = filename.rindex('.')
    if dot_index == -1:
        return '文件夹'
    # 文件
    subfix = filename[dot_index + 1:len(filename)].lower()
    if subfix in img_format:
        return '图片'
    if subfix in audio_format:
        return '音频'
    if subfix in video_format:
        return '视频'
    if subfix == 'bat' or subfix == 'exe':
        return '可执行文件'
    return subfix


# 撤回提醒
ch = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui.txt',
                 sep=' ', encoding='utf-8')

chehui = on_notice()


@chehui.handle()
async def cheh(bot: Bot, event: GroupRecallNoticeEvent):
    if event.is_tome():
        coin = random.randint(0, 2)
        if 0 == coin:
            k = (random.randint(1, 10000)) % len(chehui_tome)
            coin = random.randint(0, 2)
            word = ''
            if 0 == coin:
                word = chehui_tome.loc[k]['chehui_tome']
                print(word)
            coin = random.randint(0, 2)
            pic = ''
            if 0 == coin:
                pic = get_picture()
            result = word + '\n' + MessageSegment.image(pic)
            if result != None and result != '':
                await bot.send(
                    event=event,
                    message=result
                )
    else:
        k = (random.randint(1, 10000)) % len(ch)
        result = ch.loc[k]['chehui']
        print(result)
        await bot.send(
            event=event,
            message=result,
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


regbag = on_notice()


@regbag.handle()
async def redb(bot: Bot, event: LuckyKingNotifyEvent):
    atmsg = MessageSegment.at(event.target_id)
    await bot.send(
        event=event,
        message=atmsg+'恭喜你是运气王',
    )
