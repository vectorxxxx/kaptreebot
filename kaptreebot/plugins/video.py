# from nonebot import on_command
# from nonebot.permission import SUPERUSER
# from nonebot.adapters.cqhttp import Bot, Event
# from aiocqhttp import MessageSegment
# import requests
# import json
# import random


# error_info = '没有查询到呢~'


# # ============抖音视频榜============
# tiktok = on_command('抖音', aliases={'抖音热榜', '抖音视频', '抖音短视频'}, priority=2)


# @tiktok.handle()
# async def wzpic_(bot: Bot, event: Event):
#     if event.get_user_id != event.self_id:
#         video = get_tiktok()
#         await bot.send(
#             event=event,
#             message=MessageSegment.video(file=str(video))
#         )

# # 深度学习过程中，需要制作训练集和验证集、测试集


# def get_tiktok():
#     url = 'https://ks.ghser.com/'
#     res = requests.get(url)
#     text = res.text
#     print(text)
#     return src_video
