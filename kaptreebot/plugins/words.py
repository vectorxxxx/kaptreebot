from ctypes import Union

from nonebot.permission import SUPERUSER
from requests_html import HTMLSession
import requests
from nonebot import on_command
from nonebot import on_keyword, on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, Message
import random
from aiocqhttp import MessageSegment
import json

kiss = ['么么哒', '不要这样嘛!', '你好讨厌哦!', '你好坏哦，欺负人家，哼！', '不要酱紫嘛', '一天没和你聊天，就觉得哪里不对劲！', '快亲亲人家啦!!', '不理你了，真讨厌。', '人家不要了啦!', '你今天有没有想念人家呀!',
        '别这样啦，人家是个女孩子嘛!', '(✿◡‿◡)', '(*/ω＼*)', 'つ﹏⊂', 'ヾ(≧O≦)〃嗷~', '(>▽<)，好呀', '恶心心', 'mu--a', '可以教我写代码吗', '记得AK比赛哦', '能AK比赛吗？']


# 毒鸡汤语录
def get_dujit():
    url = 'https://du.liuzhijin.cn/'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    r = session.get(url, headers=headers, verify=False)
    sel = '#text'
    s = r.html.find(sel)
    str1 = s[0].text
    print('毒鸡汤+', str1)
    return str1


# 朋友圈文案
def get_wenan():
    url = 'https://pyq.shadiao.app/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    t = requests.get(url, headers=headers, verify=False)
    c = t.text
    print('朋友圈文案', c)
    return c


# 彩虹屁
def get_caihongpi():
    url = 'https://chp.shadiao.app/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    t = requests.get(url, headers=headers, verify=False)
    c = t.text
    print('彩红屁', c)
    return c


# 网易语录
def get_wangyi():
    url = 'https://v1.hitokoto.cn/?c=j&c=k'
    res = requests.get(url)
    c = json.loads(res.text)
    ans = c['hitokoto']+'---->'+c['from']
    print(ans)
    return ans


explain = on_command("我要亲亲", aliases={'我要抱抱'}, priority=2)


@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        k = (random.randint(0, 10000)+random.randint(0, 10000)) % len(kiss)
        s = kiss[k]
        print('kiss总数目', len(kiss), '我要抱抱指令输出:', s)
        await bot.send(
            event=event,
            message=s,
            at_sender=True
        )


dudu = on_keyword(['毒鸡汤'], priority=2)


@dudu.handle()
async def getdu_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_dujit())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


wangyi = on_command('开始网抑', priority=2)


@wangyi.handle()
async def wangyi_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_wangyi())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


caihong = on_command('彩虹屁', priority=2)


@caihong.handle()
async def caihong_(bot: Bot, event: Event, state: dict):

    str1 = str(get_caihongpi())
    await bot.send(
        event=event,
        message=str1,
        at_sedner=True
    )


pyqwenan = on_command('朋友圈文案', priority=2)


@pyqwenan.handle()
async def pyqwenan_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = str(get_wenan())
        await bot.send(
            event=event,
            message=str1,
            at_sedner=True
        )


k_master = ['我的主人就是您丫~',
            '我的主人？我就是自己的主人呀。我想说就说，想语音就语音，先发图就发图，想挂机就挂机', '我的主人？远在天边，近在眼前~']

master = on_keyword(['主人', '你是谁的'], priority=2)


@master.handle()
async def master_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        k = (random.randint(0, 10000)+random.randint(0, 10000)) % len(k_master)
        s = k_master[k]
        await bot.send(
            event=event,
            message=s
        )
