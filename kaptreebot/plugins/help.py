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
        table = PrettyTable(['命令'])
        table.add_row(['1、句子：每日一句'])
        table.add_row(['2、天气查询：天气 成都'])
        table.add_row(['3、翻译：翻译 什么他妈的叫他妈的惊喜'])
        table.add_row(['4、戳一戳：手机上双击戳我头像'])
        table.add_row(['5、精彩图片：setu，R18，MC酱'])
        table.add_row(['6、亲亲抱抱：我要亲亲，我要抱抱'])
        table.add_row(['7、语录：毒鸡汤，开始网抑，彩虹屁，朋友圈文案'])
        table.add_row(['8、注意：群聊需要@我或者开头加上/'])
        table.add_row(['9、学习功能：健康知识，名句，谚语'])
        table.add_row(['10、隐藏功能：༼ つ ◕_◕ ༽つ'])
        await bot.send(
            event=event,
            message=str(table)
        )

help_hide = on_command('其他菜单', aliases={'其他帮助', '其他功能'}, priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['序号', '命令', '示例'])
        table.add_row(['1', '疫情', '新冠疫情'])
        table.add_row(['2', '热点', '微信热点，每日简报'])
        table.add_row(['3', '健康', '健康知识'])
        table.add_row(['4', '对联', '经典对联'])
        table.add_row(['5', '台词', '经典台词'])
        table.add_row(['6', '名句', '古籍名句，民国句子'])
        table.add_row(['7', '十万个为什么', '十万个为什么'])
        table.add_row(['8', '谚语', '文化谚语'])
        table.add_row(['9', '故事', '讲个故事'])
        table.add_row(['10', '占卜', '手机号占卜'])
        table.add_row(['11', '王者', '王者图片，王者语音'])
        await bot.send(
            event=event,
            message=str(table)
        )

help_hide = on_command('隐藏菜单', aliases={'隐藏帮助', '隐藏功能'}, priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['序号', '命令', '示例'])
        table.add_row(['1', '疫情', '新冠疫情'])
        table.add_row(['2', '热点', '微信热点，每日简报'])
        table.add_row(['3', '健康', '健康知识'])
        table.add_row(['4', '对联', '经典对联'])
        table.add_row(['5', '台词', '经典台词'])
        table.add_row(['6', '名句', '古籍名句，民国句子'])
        table.add_row(['7', '十万个为什么', '十万个为什么'])
        table.add_row(['8', '谚语', '文化谚语'])
        table.add_row(['9', '故事', '讲个故事'])
        table.add_row(['10', '占卜', '手机号占卜'])
        table.add_row(['11', '王者', '王者图片，王者语音'])
        await bot.send(
            event=event,
            message=str(table)
        )
