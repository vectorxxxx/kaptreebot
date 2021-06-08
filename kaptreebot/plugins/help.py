from ctypes import Union

from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot import on_keyword, on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from prettytable import PrettyTable


# 总菜单
help = on_command("help", aliases={'菜单'}, priority=2)


@help.handle()
async def help_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = ''
        str1 += '1、天气查询：天气 成都\n'
        str1 += '2、翻译：翻译 什么他妈的叫他妈的惊喜\n'
        str1 += '3、戳一戳：手机上双击戳我头像\n'
        str1 += '4、亲亲抱抱：我要亲亲，我要抱抱\n'
        str1 += '5、注意：群聊需要@我或者开头加上/\n'
        str1 += '6、更多功能：详见新闻菜单、文艺菜单、娱乐菜单、舔狗菜单\n'
        str1 += '7、隐藏功能：༼ つ ◕_◕ ༽つ你懂的'
        await bot.send(
            event=event,
            message=str1
        )


# 新闻菜单
news_hide = on_command('新闻菜单', priority=2)


@news_hide.handle()
async def news_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['新闻菜单'])
        table.add_row(['今日疫情'])
        table.add_row(['今日热点'])
        table.add_row(['今日简报'])
        table.add_row(['今日IT'])
        await bot.send(
            event=event,
            message=str(table)
        )


# 文艺菜单
literature_hide = on_command('文艺菜单', priority=2)


@literature_hide.handle()
async def literature_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['序号','文艺菜单'])
        table.align['文艺菜单'] = 'l'
        table.add_row(['每日一句'])
        table.add_row(['每日百科'])
        table.add_row(['每日历史'])
        table.add_row(['每日唐诗'])
        table.add_row(['每日谚语'])
        table.add_row(['每日对联'])
        table.add_row(['每日台词'])
        table.add_row(['每日故事'])
        table.add_row(['每日健康'])
        table.add_row(['歇后语'])
        await bot.send(
            event=event,
            message=str(table)
        )

# 娱乐菜单
help_hide = on_command('娱乐菜单', priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['娱乐菜单'])
        table.add_row(['点歌'])
        table.add_row(['王者图片/语音'])
        table.add_row(['召唤妲己'])
        table.add_row(['周公解梦'])
        table.add_row(['绕口令'])
        table.add_row(['占卜'])
        await bot.send(
            event=event,
            message=str(table)
        )

# 舔狗菜单
help_hide = on_command('舔狗菜单', priority=2)


@help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        table = PrettyTable(['舔狗菜单'])
        table.add_row(['每日必舔'])
        table.add_row(['每日绿茶'])
        table.add_row(['每日情话'])
        table.add_row(['每日情诗'])
        table.add_row(['每日土味'])
        await bot.send(
            event=event,
            message=str(table)
        )

# 隐藏菜单
help_hide = on_command('隐藏菜单', priority=2)


@ help_hide.handle()
async def hhelp_hide_(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        str1 = ''
        str1 += '1、精彩图片：setu，R18，MC酱\n'
        str1 += '2、以图搜图：在ex/nao/trace/iqdb/ascii2d上搜索相似图片(●´ω｀●)\n'
        str1 += '*.°☀️·🛸🌏°🌓•.°•🚀\n'
        str1 += '✯✯　　★　*°　　　　🛰　°·\n'
        str1 += ' .　　　•　°★　•\n'
        str1 += ' ▂▃▄▅▆▇▇▆▅▄▃.\n'
        await bot.send(
            event=event,
            message=str1
        )
