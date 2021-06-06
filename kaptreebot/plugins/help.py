from ctypes import Union

from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot import on_keyword, on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from prettytable import PrettyTable

help = on_command(
    "查看说明", aliases={'help', '帮助', '菜单', '手册', '功能'}, priority=2)


@help.handle()
async def help_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['序号', '命令', '示例'])
        table.add_row(['1', '句子', '每日一句'])
        table.add_row(['2', '天气', '天气 成都'])
        table.add_row(['3', '翻译', '翻译 中出'])
        table.add_row(['4', '戳一戳', '戳头像'])
        table.add_row(['5', '图片', 'R18'])
        table.add_row(['6', '抱抱', '我要抱抱'])
        table.add_row(['7', '语录', '开始网抑'])
        table.add_row(['8', '注意', '群聊@我或/'])
        table.add_row(['9', '更多', '请体验触发'])
        await bot.send(
            event=event,
            message=str(table)
        )

help_hide = on_command(
    "隐藏菜单", aliases={'隐藏帮助', '隐藏功能', '其他菜单',  '其他帮助', '其他功能'}, priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['序号', '命令', '示例'])
        table.add_row(['1', '疫情', '新冠疫情'])
        table.add_row(['2', '热点', '微信热点,每日简报'])
        table.add_row(['3', '健康', '健康知识'])
        table.add_row(['4', '对联', '经典对联'])
        table.add_row(['5', '台词', '经典台词'])
        table.add_row(['6', '名句', '古籍名句,民国句子'])
        table.add_row(['7', '十万个为什么', ''])
        table.add_row(['8', '谚语', '文化谚语'])
        table.add_row(['9', '故事', '讲个故事'])
        table.add_row(['10', '占卜', '手机号占卜'])
        table.add_row(['11', '王者', '王者图片/语音'])
        await bot.send(
            event=event,
            message=str(table)
        )
