from typing import Any, Dict
from nonebot import get_driver, on_command
from nonebot.adapters.cqhttp import Bot, Event, GroupMessageEvent, PrivateMessageEvent
from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State, T_CalledAPIHook
from .config import Config
import pandas as pd
import os
import random

global_config = get_driver().config
withdraw_config = Config(**global_config.dict())

msg_ids = {}
max_size = withdraw_config.withdraw_max_size

chehui_tome_exception = pd.read_csv('file:///' + os.getcwd() + '/data/pokeme/chehui_tome_exception.txt',
                                    sep=' ', encoding='utf-8')


def get_key(msg_type, id):
    return f'{msg_type}_{id}'


async def save_msg_id(bot: Bot, e: Exception, api: str, data: Dict[str, Any], result: Any) -> T_CalledAPIHook:
    try:
        if api == 'send_msg':
            msg_type = data['message_type']
            id = data['group_id'] if msg_type == 'group' else data['user_id']
        elif api == 'send_private_msg':
            msg_type = 'private'
            id = data['user_id']
        elif api == 'send_group_msg':
            msg_type = 'group'
            id = data['group_id']
        else:
            return
        key = get_key(msg_type, id)
        msg_id = result['message_id']

        if key not in msg_ids:
            msg_ids[key] = []
        msg_ids[key].append(msg_id)
        if len(msg_ids) > max_size:
            msg_ids[key].pop(0)
    except:
        pass


Bot._called_api_hook.add(save_msg_id)


withdraw = on_command(
    '你撤回', aliases={'你快撤回', '你给我撤回', '你赶快撤回', '撤回'}, rule=to_me(), priority=2)


@withdraw.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if isinstance(event, GroupMessageEvent):
        msg_type = 'group'
        id = event.group_id
    elif isinstance(event, PrivateMessageEvent):
        msg_type = 'private'
        id = event.user_id
    else:
        return
    key = get_key(msg_type, id)

    num = event.get_plaintext().strip()
    if not num:
        num = 0
    elif num.isdigit() and 0 <= int(num) < len(msg_ids[key]):
        num = int(num)
    else:
        return

    try:
        idx = -num - 1
        await bot.delete_msg(message_id=msg_ids[key][idx])
        msg_ids[key].pop(idx)
    except:
        k = (random.randint(1, 10000)) % len(chehui_tome_exception)
        result = chehui_tome_exception.loc[k]['chehui_tome_exception']
        print(result)
        await withdraw.finish(result)
