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


help = on_command(
    "查看说明", aliases={'help', '帮助', '菜单', '手册', '功能'}, priority=2)


@help.handle()
async def help_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        await bot.send(
            event=event,
            message='1.每日一句 eg:/每日一句\n\n'
                    '2.天气查询 eg:/天气 成都\n\n'
                    '3.翻译 eg:/翻译 cat\n\n'
                    '4.戳一戳 eg:手机戳我头像\n\n'
                    '5.精彩图片 eg:关键词匹配("/每日一图"，/mc酱，/R18")\n\n'
                    '6.我要抱抱 eg 我要抱抱\n\n'
                    '7.朋友圈文案/彩虹屁/开始网抑/毒鸡汤 eg:(“/开始网抑，/彩虹屁，/朋友圈文案，/毒鸡汤”)\n\n'
                    '8.注意私聊的时候可以不加前缀/，群聊的时候可以@我或者/\n\n'
                    '9.更多功能请亲自体验触发……'
        )
