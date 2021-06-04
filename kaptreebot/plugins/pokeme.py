from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import Event, PokeNotifyEvent,LuckyKingNotifyEvent,GroupRecallNoticeEvent
from nonebot.adapters.cqhttp.message import Message
import random
from aiocqhttp import MessageSegment

a = ['那...那里...那里不能戳...绝对...','嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳了，戳怀孕了',
   '嘤嘤嘤，人家痛痛','我错了我错了，别戳了','桥豆麻袋,别戳老子','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？','不要啦，别戳啦','你好坏啊~','不要酱紫啦~','好讨厌~','你真无聊','死鬼~','干嘛吗~','很烦啊你！',
   '要点脸行吗，咸猪手！','再这样我报警了！','你戳啥呢','非礼啊~','坏死了~','别戳了，戳坏了你赔得起吗','让你别戳，让你别戳！还戳？',
   '敢戳老娘，不想好了是吗？','老娘是你想戳就戳的？','别惹急了老娘，惹急了让你断子绝孙！','说了多少次，不要戳那里！','还戳？',
   '不给你点颜色看看，你都不知道什么叫濒临死亡！','今天想骂人，所以不骂你','你嘴里怎么镶着象牙','傻子都说自己不傻，你傻吗？']

pre = 0
poke=on_notice()
@poke.handle()
async def _(bot:Bot,event:Event):
    if isinstance(event,PokeNotifyEvent):
        if event.is_tome() and event.user_id!=event.self_id:
            l = len(a)
            k = random.randint(0,l-1)
            while pre == k:
                k = random.randint(0,l-1)
            last = k
            await bot.send(
                event=event,
                message=a[k],
                at_sender=True
            )

b = ['喜欢人家就直说啊,我还没说不同意呢~','撤回也没用我已经看到，还截屏了','怀孕了就直说，大家一起想办法啊，撤回干什么','看，撤回了，又撤回了……见不得人的勾当',
'你现在撤回还得及','撤回没用，拍照了','再撤回就一枪毙了你！','撤你妹消息','人在做，朝阳区群众在看','有个大傻子撤回了消息，大家快来看鸭！','我错过了什么！？！？！？',
'WTF!!??']

pre = 0
chehui = on_notice()
@chehui.handle()
async def cheh(bot:Bot,event:GroupRecallNoticeEvent):
    if event.get_user_id != event.self_id:
        l = len(b)
        k = random.randint(0,l-1)
        await bot.send(
                event=event,
                message=b[k],
                at_sender=True
              )

regbag = on_notice()
@regbag.handle()
async def redb(bot:Bot,event:LuckyKingNotifyEvent):
    atmsg = MessageSegment.at(event.target_id)
    await bot.send(
        event=event,
        message = atmsg+'恭喜你是运气王',
    )
