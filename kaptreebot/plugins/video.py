from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from requests_html import HTMLSession
import random
import urllib3

# 将函数注册为群成员增加通知处理器

urllib3.disable_warnings()

error_info = '没有查询到呢~'


# ============抖音视频榜============
tiktok = on_command('抖音', aliases={'抖音热榜', '抖音视频', '抖音短视频'}, priority=2)


@tiktok.handle()
async def wzpic_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        video_r = get_tiktok()
        await bot.send(
            event=event,
            message=video_r
        )

# 深度学习过程中，需要制作训练集和验证集、测试集


def get_tiktok():
    url = 'http://c.3g.163.com/nc/video/home/0-10.html'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    r = session.get(url, headers=headers)
    sel = '#text'
    s = r.html.find(sel)
    c = s[0].text

    video_info = c['videoList'][random.randint(0, 10)]
    video_title = video_info['title']
    video_url = video_info['mp4_url']
    result = video_title + '\n'
    result += MessageSegment.video(file=str(video_url))
    return result
