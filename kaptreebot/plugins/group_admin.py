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
import requests
import json

chehui_tome = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui_tome.txt',
                          sep=' ', encoding='utf-8')

# 将函数注册为群成员增加通知处理器


# 获取头像
def get_tx(qq):
    url = 'https://api.ghser.com/qq/?get=' + str(qq)
    res = requests.get(url,verify=False)
    c = json.loads(res)
    if not c['success']:
        return ''
    imgurl = c['imgurl']
    print(imgurl)
    return MessageSegment.image(imgurl)

# 获取昵称
def get_name(qq):
    url = 'https://api.ghser.com/qq/?get=' + str(qq)
    res = requests.get(url,verify=False)
    c = json.loads(res)
    if not c['success']:
        return ''
    name = c['name']
    print(name)
    return name

# =========入群提醒=========
increase = on_notice()

@increase.handle()
async def increase(bot: Bot, event: GroupIncreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        hello_img_path = 'file:///'+os.getcwd()+'/data/img/hello.gif'
        msg = '哇~是新的rbq！\n'
        msg += get_tx(event.get_user_id) + '\n'
        msg += '欢迎呀，很高兴为您服务呦~\n'
        msg += '博客皮肤有什么问题，可以先查看查看手册：\n'
        msg += 'https://www.yuque.com/awescnb/user/tmpomo\n'
        msg += '另外，如果需要其他的服务，可以对我说“help”\n'
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )


# =========退群提醒=========
decrease = on_notice()


@decrease.handle()
async def decrease(bot: Bot, event: GroupDecreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = ''
        name = get_name(event.get_user_id)
        if name != '':
            msg += '[CQ:at,qq="' + name + '"]'
        else:
            msg += '[CQ:at,qq="' + event.get_user_id + '"]'
        msg += '离开了，好难过~\n'
        msg += get_tx(event.get_user_id) + '\n'        
        await bot.send(
            event=event,
            message=msg
        )

# =========上传提醒=========
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


# =========撤回提醒=========
ch = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui.txt',
                 sep=' ', encoding='utf-8')

chehui = on_notice()


@chehui.handle()
async def cheh(bot: Bot, event: GroupRecallNoticeEvent):
    if event.is_tome():
        k = (random.randint(1, 10000)) % len(chehui_tome)
        coin = random.randint(0, 3)
        word = ''
        pic = ''
        if coin != 1:
            word = chehui_tome.loc[k]['chehui_tome']
            print(word)
        if coin != 0:
            pic = get_picture()

        result = ''
        if word != '':
            result = word + '\n' + MessageSegment.image(pic)
        elif pic != '':
            result = MessageSegment.image(pic)
        if result != '':
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


# =========红包提醒=========
regbag = on_notice()


@regbag.handle()
async def redb(bot: Bot, event: LuckyKingNotifyEvent):
    atmsg = MessageSegment.at(event.target_id)
    await bot.send(
        event=event,
        message=atmsg+'恭喜你是运气王',
    )
