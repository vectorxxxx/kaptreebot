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

# 获取图片


# se图
def get_setu():
    urls = ['https://api.ixiaowai.cn/api/api.php',
            'http://api.mtyqx.cn/api/random.php']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url, headers=headers, verify=False)
    c = res.url
    return c


# MC酱的表情包
def get_mc():
    url = 'https://api.ixiaowai.cn/mcapi/mcapi.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url, headers=headers, verify=False)
    c = res.url
    return c


# 有一定概率刷出R18的图
def get_R18():
    url = 'https://api.yimian.xyz/img/?type=koino&R18=true'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url, headers=headers, verify=False)
    c = res.url
    return c


st = on_keyword(['setu', '涩图', '色图', '每日一图', '黄图',
                '福利', '富婆', '老婆', '萝莉'], priority=2)


@st.handle()
async def st_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_setu()),
        )


R18 = on_keyword(['r18', 'R18', 'r19', 'R19', 'r28', 'R28', '二次元'], priority=2)


@R18.handle()
async def R18_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_R18()),
        )


mc = on_keyword(['mc表情包', 'MC酱', 'Mc酱', 'mC酱', "mc酱"], priority=2)


@mc.handle()
async def mcpo(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message=MessageSegment.image(get_mc()),
            at_sender=True
        )
