from nonebot.permission import SUPERUSER
import requests
from nonebot import on_command, on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import random
from aiocqhttp import MessageSegment
import urllib3


# 去除SSL证书验证
urllib3.disable_warnings()


# ============每日一图============
dailypic = on_command('每日一图', priority=2)


@dailypic.handle()
async def dailypic_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_dailypic()
        await bot.send(
            event=event,
            message=msg
        )


def get_dailypic():
    urls = ['https://cdn.seovx.com/?mom=302',
            'https://api.btstu.cn/sjbz/api.php']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============古风============
gf = on_command('古风', priority=2)


@gf.handle()
async def gf_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_gf()
        await bot.send(
            event=event,
            message=msg
        )


def get_gf():
    urls = ['https://cdn.seovx.com/ha/?mom=302']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============setu============
st = on_keyword(['setu', '涩图', '色图', '福利姬'], priority=2)


@st.handle()
async def st_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_setu()
        await bot.send(
            event=event,
            message=msg
        )


def get_setu():
    urls = ['https://api.vvhan.com/api/mobil.girl',
            'https://api.vvhan.com/api/girl',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F1.php',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F2.php',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F3.php',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F4.php',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F5.php',
            'https://api.r10086.com/%E5%B0%91%E5%A5%B3%E5%86%99%E7%9C%9F6.php',
            'https://api.r10086.com/%E6%AD%BB%E5%BA%93%E6%B0%B4%E8%90%9D%E8%8E%89.php',
            'https://api.r10086.com/%E8%90%9D%E8%8E%89.php',
            'https://api.r10086.com/%E6%9E%81%E5%93%81%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87.php',
            'https://api.r10086.com/%E6%97%A5%E6%9C%ACCOS%E4%B8%AD%E5%9B%BDCOS.php'
            ]
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============二次元============
acgn = on_command('二次元', aliases={'萝莉'}, priority=2)


@acgn.handle()
async def acgn_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_acgn()
        await bot.send(
            event=event,
            message=msg
        )


def get_acgn():
    urls = ['https://api.ixiaowai.cn/api/api.php',
            'http://api.mtyqx.cn/api/random.php',
            'https://img.xjh.me/random_img.php',
            'https://www.dmoe.cc/random.php',
            'https://www.rrll.cc/tuceng/ecy.php',
            'https://api.ghser.com/random/api.php',
            'https://acg.yanwz.cn/wallpaper/api.php',
            'https://acg.yanwz.cn/api.php',
            'https://api.vvhan.com/api/acgimg',
            'https://api.yimian.xyz/img?type=moe',
            'https://cdn.seovx.com/d/?mom=302']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============二次元头像============
acgn_head = on_command('二次元头像', priority=2)


@acgn_head.handle()
async def acgn_head_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_acgn_head()
        await bot.send(
            event=event,
            message=msg
        )


def get_acgn_head():
    urls = ['https://api.yimian.xyz/img?type=head']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============R18============
R18 = on_keyword(['r18', 'R18'], priority=2)


@R18.handle()
async def R18_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_R18()
        await bot.send(
            event=event,
            message=msg
        )


def get_R18():
    urls = ['https://api.yimian.xyz/img/?type=koino&R18=true']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============MC酱============
mc = on_keyword(['mc表情包', 'MC酱', 'Mc酱', 'mC酱', "mc酱"], priority=2)


@mc.handle()
async def mc_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_mc()
        await bot.send(
            event=event,
            message=msg
        )


def get_mc():
    urls = ['https://api.ixiaowai.cn/mcapi/mcapi.php',
            'https://acg.yanwz.cn/menhera/api.php']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)


# ============猫娘============
cat = on_keyword(['猫娘'], priority=2)


@cat.handle()
async def cat_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        msg = get_cat()
        await bot.send(
            event=event,
            message=msg
        )


def get_cat():
    urls = ['https://api.r10086.com/%E7%8C%AB%E5%A8%981.php']
    url = urls[random.randint(0, len(urls) - 1)]
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    res = requests.get(url, headers=headers, verify=False)
    imgurl = res.url
    return MessageSegment.image(imgurl)
