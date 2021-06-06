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
        str1 = ''
        str1 += '1、句子：每日一句\n'
        str1 += '2、天气查询：天气 成都\n'
        str1 += '3、翻译：翻译 什么他妈的叫他妈的惊喜\n'
        str1 += '4、戳一戳：手机上双击戳我头像\n'
        str1 += '5、精彩图片：setu，R18，MC酱\n'
        str1 += '6、亲亲抱抱：我要亲亲，我要抱抱\n'
        str1 += '7、语录：毒鸡汤，开始网抑，彩虹屁，朋友圈文案\n'
        str1 += '8、注意：群聊需要@我或者开头加上/\n'
        str1 += '9、其他功能：健康知识，名句，谚语等，需输入指令：其他菜单\n'
        str1 += '10、隐藏功能：你懂的༼ つ ◕_◕ ༽つ'
        await bot.send(
            event=event,
            message=str1
        )

help_hide = on_command('其他菜单', aliases={'其他帮助', '其他功能'}, priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = ''
        str1 += '1、疫情：新冠疫情\n'
        str1 += '2、热点：微信热点，每日简报\n'
        str1 += '3、健康：健康知识\n'
        str1 += '4、对联：经典对联\n'
        str1 += '5、台词：经典台词\n'
        str1 += '6、名句：古籍名句，民国句子\n'
        str1 += '7、百科：十万个为什么\n'
        str1 += '8、谚语：文化谚语\n'
        str1 += '9、故事：讲个故事\n'
        str1 += '10、占卜：手机号占卜\n'
        await bot.send(
            event=event,
            message=str1
        )

help_hide = on_command('隐藏菜单', aliases={'隐藏帮助', '隐藏功能'}, priority=2)


@ help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = ''
        str1 += '1、王者荣耀：王者图片，王者语音\n'
        str1 += '2、网易云点歌：（网易云音乐）点歌 稻香\n'
        str1 += '3、以图搜图：在ex/nao/trace/iqdb/ascii2d上搜索相似图片(●´ω｀●)\n'
        str1 += '*.°☀️·🛸🌏°🌓•.°•🚀\n'
        str1 += '✯✯　　★　*°　　　　🛰　°·\n'
        str1 += ' .　　　•　°★　•\n'
        str1 += ' ▁▂▃▄▅▆▇▇▆▅▄▃▁▂▃.\n'
        await bot.send(
            event=event,
            message=str1
        )
