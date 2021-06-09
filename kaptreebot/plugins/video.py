from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from requests_html import HTMLSession
import random
import urllib3
import json

# 将函数注册为群成员增加通知处理器

urllib3.disable_warnings()

error_info = '没有查询到呢~'


# ============快手小姐姐============
kuaishou = on_command('快手小姐姐', priority=2)


@kuaishou.handle()
async def kuaishou_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        video_r = get_kuaishou()
        await bot.send(
            event=event,
            message=video_r
        )


def get_kuaishou():
    url = 'https://ks.ghser.com/video.php'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    r = session.get(url, headers=headers, verify=False)
    video_url = json.loads(r.text)
    return MessageSegment.video(file=str(video_url))


# ============小姐姐视频============
sister = on_command('小姐姐视频', priority=2)


@sister.handle()
async def sister_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        video_r = get_sister()
        await bot.send(
            event=event,
            message=video_r
        )


def get_sister():
    urls = ['https://api.r10086.com/%E8%88%9E%E8%B9%88%E8%A7%86%E9%A2%91.php',
            'https://api.r10086.com/鹿鸣系列视频.php']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    r = session.get(url, headers=headers, verify=False)
    video_url = json.loads(r.text)
    return MessageSegment.video(file=str(video_url))
