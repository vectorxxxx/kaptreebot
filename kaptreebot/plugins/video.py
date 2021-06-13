from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from requests_html import HTMLSession
from lxml import etree
from urllib import request
from urllib.error import HTTPError, URLError
import random
import urllib3


urllib3.disable_warnings()

opener = request.build_opener()

error_info = '小撸怡情，大撸伤身，要适度哦~'


# ============快手小姐姐============
xiaojj = on_command('小姐姐', priority=2)


@xiaojj.handle()
async def xiaojj_(bot: Bot, event: Event):
    if event.get_user_id != event.self_id:
        video_r = get_xiaojj()
        await bot.send(
            event=event,
            message=video_r
        )


def get_xiaojj():
    ram_num = random.randint(0, 1)
    if ram_num == 0:
        return get_kuaishou()
    else:
        return get_rewu()


def get_kuaishou():
    print('快手小姐姐')
    url = 'https://ks.ghser.com/video.php'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }

    try:
        r = session.get(url, headers=headers, verify=False)
        video_url = r.url
        print(video_url)
        return get_video(video_url)
    except Exception:
        return error_info


def get_rewu():
    print('美女热舞')
    url = 'https://imyshare.com/hot-girl/'
    session = HTMLSession()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }

    try:
        r = session.get(url, headers=headers, verify=False)
        selector = etree.HTML(r.content)
        video_urls = selector.xpath('//*[@id="video"]/@src')
        print(video_urls)
        video_url = video_urls[0].replace('\n', '')
        print(video_url)
        return get_video(video_url)
    except Exception:
        return error_info


def get_video(video_url):
    try:
        opener.open(video_url)
        video = MessageSegment.video(file=str(video_url))
        if video is not None:
            return video
        else:
            return error_info
    except (HTTPError, URLError) as e:
        return error_info
    except Exception:
        return error_info
