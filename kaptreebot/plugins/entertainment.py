from nonebot import on_command
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, Event
from aiocqhttp import MessageSegment
from commons import property
import requests
import json
import os

# 要操作的properties文件的路径
file_path = os.getcwd() + '/properties/cheat/others.properties'
# 读取文件
props = property.parse(file_path)
tianxing_api = props.get('tianxing_api')
tianxing_key = props.get('tianxing_key')
error_info = '没有查询到呢~'


# ============手机号占卜============
jixiong = on_command('手机号占卜', aliases={'手机号算卦', '手机号占卦', '手机号算命', '手机号占星',
                     '手机算卦', '手机占卦', '手机算命', '手机占星', '占卜', '算卦', '占卦', '算命', '占星'}, priority=2)


@jixiong.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            state["phone"] = args  # 如果用户发送了参数则直接赋值


@jixiong.got("phone", prompt="请输入您的手机号")
async def handle_hero(bot: Bot, event: Event, state: dict):
    phone = state["phone"]
    result = await get_jixiong(phone)
    await jixiong.finish(result)


async def get_jixiong(phone: str):
    url = tianxing_api + 'jixiong/index?key=' + tianxing_key + '&number=' + phone
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200:
        return error_info
    result = ''
    for news in c['newslist']:
        result += news['conclusion'] + '\n'
        result += '              坤              ' + '\n'
        result += '              ▔              ' + '\n'
        result += '   兑╱              ╲巽   ' + '\n'
        result += '\n'
        result += '离▏         ' + news['result'] + '          ▕坎' + '\n'
        result += '\n'
        result += '   震╲              ╱艮   ' + '\n'
        result += '              ▁              ' + '\n'
        result += '              乾              ' + '\n'
        result += '★★★' + news['score'] + '分'
        print(result)
        return result

# 周公解梦
zgjm = on_command('周公解梦', priority=2)


@zgjm.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            state["text"] = args  # 如果用户发送了参数则直接赋值


@zgjm.got("text", prompt="你梦见了什么？")
async def handle_hero(bot: Bot, event: Event, state: dict):
    text = state["text"]
    result = await get_zgjm(text)
    await zgjm.finish(result)


async def get_zgjm(text: str):
    url = tianxing_api + 'dream/index?key=' + tianxing_key + '&word=' + text
    res = requests.get(url)
    c = json.loads(res.text)
    if c['code'] != 200 or c['msg'] !='success':
        print('code: '+str(c['code']))
        print('msg: '+c['msg'])
        return '天机不可泄露~'
    result = ''    
    for news,i in c['newslist']:
        result += str(i+1) + '、' + news['result'] + '\n'
    print('梦见' + text + '：\n' + result)
    return result
   