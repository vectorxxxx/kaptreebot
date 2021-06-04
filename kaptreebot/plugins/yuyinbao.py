import os
from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event, Message
from aiocqhttp import MessageSegment

#语音包指令


#早上好啊，小哥哥
cmd1 = on_command('早上好',aliases={'早安','早'},priority=2)
@cmd1.handle()
async def cmd1_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\zsh.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我傻呗
cmd2 = on_command('你为什么喜欢我',aliases={'你为什么喜欢上我'},priority=2)
@cmd2.handle()
async def cmd2_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我傻呗.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#晚安咯，我要去睡觉了，不然该不漂亮了
cmd3 = on_command('晚安',aliases={'安'},priority=2)
@cmd3.handle()
async def cmd3_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\晚安咯，我要去睡觉了，不然该不漂亮了.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#
cmd4 = on_command('今晚到我房间来',aliases={'今晚来我房间','今晚找你算账','今晚找你','躺平','躺好了吗','躺好了么','躺好了没','跟你睡觉','和你睡觉'},priority=2)
@cmd4.handle()
async def cmd4_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我已经躺床上了.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#能做你女朋友吗
cmd5 = on_keyword(['单身','一个人','找对象','恋爱'],priority=2)
@cmd5.handle()
async def cmd5_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我能做你女朋友吗？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#哎呀好的啦 小哥哥不要生气了嘛
cmd6 = on_keyword(['生气','气死','服了','醉了','不高兴','不开心','烦','难受','无语'],priority=2)
@cmd6.handle()
async def cmd6_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\。哎呀好的啦 小哥哥不要生气了嘛.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你好小哥哥，需要服务吗？
cmd7 = on_keyword(['嗨喽','哈喽','你好','您好','hello','Hello','Hi'],priority=2)
@cmd7.handle()
async def cmd7_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你好小哥哥，需要服务吗？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不要想那么多。想太多不好
cmd8 = on_command('我总是想太多',aliases={'我想多了','我多想了','我多虑了','想那么多干嘛','不要想那么多','不要想太多','别想那么多','别想太多'},priority=2)
@cmd8.handle()
async def cmd8_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不要想那么多。想太多不好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#忙什么，都不知道找我聊聊天
cmd9 = on_keyword(['好忙','事情好多','事好多','没空','好多事','没时间','太忙','忙人'],priority=2)
@cmd9.handle()
async def cmd9_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\忙什么，都不知道找我聊聊天.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#才不话音视频呢，太轻浮了。
cmd10 = on_command('来视频吧',aliases={'视频','打视频','裸聊','视频聊天'},priority=2)
@cmd10.handle()
async def cmd10_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\才不话音视频呢，太轻浮了。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我会努力的
cmd11 = on_command('加油',aliases={'好好干'},priority=2)
@cmd11.handle()
async def cmd11_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我会努力的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我的红包呢
cmd12 = on_keyword(['红包'],priority=2)
@cmd12.handle()
async def cmd12_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我的红包呢.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#我这不方便接语音，打字聊行么？
cmd13 = on_command('语音吗',aliases={'语音','发语音','语音聊天'},priority=2)
@cmd13.handle()
async def cmd13_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我这不方便接语音，打字聊行么？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#拜拜咯，我去洗澡了。.mp3
cmd14 = on_command('待会聊',aliases={'干活','干活喽','干活咯','拜拜','再见'},priority=2)
@cmd14.handle()
async def cmd14_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\拜拜咯，我去洗澡了。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#叫我小仙女
cmd15 = on_command('怎么称呼你呢',aliases={'叫你什么呢','你叫什么呢','你叫啥','你的名字是什么','你是机器人吗','你叫什么名字','你叫什么'},priority=2)
@cmd15.handle()
async def cmd15_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\叫我小仙女.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你好帅啊
cmd16 = on_command('我帅吗',aliases={'我长得怎么样','我好看吗','我怎么样','我帅不','颜值代表'},priority=2)
@cmd16.handle()
async def cmd16_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你好帅啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我单身啊
cmd17 = on_command('你有男朋友吗',aliases={'单身吗','你有对象吗','你结婚了吗'},priority=2)
@cmd17.handle()
async def cmd17_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我单身啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你为什么会问这个问题~1.mp3
cmd18 = on_command('我和你妈掉进水里',priority=2)
@cmd18.handle()
async def cmd18_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你为什么会问这个问题~1.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我tm说我不是女的，你tm是要搞基。.mp3
cmd19 = on_command('小姐姐处CP吗',aliases={'谈恋爱吗','网恋吗','处CP吗'},priority=2)
@cmd19.handle()
async def cmd19_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我tm说我不是女的，你tm是要搞基。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我的错咯。要不要道个歉？
cmd20 = on_command('都怪你',aliases={'都是你的错','都怨你','揍你','打你','滚'},priority=2)
@cmd20.handle()
async def cmd20_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我的错咯。要不要道个歉？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我平常不喜欢语音的，很少说话.mp3
cmd21 = on_command('你很喜欢发语音吗',aliases={'你怎么总是发语音','你怎么老是发语音','你说什么？','你说啥呢'},priority=2)
@cmd21.handle()
async def cmd21_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我平常不喜欢语音的，很少说话.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我身体不舒服就别强迫我啦。.mp3
cmd22 = on_command('今晚来玩吗',aliases={'出来玩'},priority=2)
@cmd22.handle()
async def cmd22_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我身体不舒服就别强迫我啦。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我身体不舒服就别强迫我啦。.mp3
cmd23 = on_command('抱抱',priority=2)
@cmd23.handle()
async def cmd23_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我要抱抱.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

cmd24 = on_command('你在想什么',aliases={'你想啥呢','你想谁呢','你想什么呢','你在想啥','你想干啥'},priority=2)
@cmd24.handle()
async def cmd24_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我再想你啊小笨蛋.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我最喜欢喝牛奶了 旺仔牛奶耶耶耶
cmd25 = on_command('你喜欢喝什么',aliases={'你最喜欢喝什么','你有什么爱好吗'},priority=2)
@cmd25.handle()
async def cmd25_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我最喜欢喝牛奶了 旺仔牛奶耶耶耶.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#油嘴滑舌的
cmd26 = on_command('你真好看',aliases={'你好漂亮','你真美','你真漂亮','你好好看','你好美','你最好看','你最漂亮','你最美'},priority=2)
@cmd26.handle()
async def cmd26_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\油嘴滑舌的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#就算搞基我也只做攻 就是把你压在身下那种。
cmd27 = on_command('击剑吗',aliases={'击剑嘛','来击剑'},priority=2)
@cmd27.handle()
async def cmd27_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\就算搞基我也只做攻 就是把你压在身下那种。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不要因为我可爱你就欺负我.mp3
cmd28 = on_command('你好可爱',aliases={'你真可爱','你那么可爱，你家里人知道吗','可爱','你怪可爱的','你挺可爱的'},priority=2)
@cmd28.handle()
async def cmd28_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不要因为我可爱你就欺负我.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#对对对，这是下载的.mp3
cmd29 = on_command('你这是下载的吗',aliases={'你的语音是下载','你下载的？'},priority=2)
@cmd29.handle()
async def cmd29_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\对对对，这是下载的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#嗯嗯，你对我真好.mp3
cmd30 = on_command('我对你好吗',aliases={'我对你好不好','我对你怎么样','我好吗','你觉得我对你怎么样'},priority=2)
@cmd30.handle()
async def cmd30_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\嗯嗯，你对我真好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#哇你好棒棒哦.mp3
cmd31 = on_command('我棒不棒',aliases={'厉害吧','牛逼吧','我厉害吗','我厉害么','我棒不','怎么样','你觉得我怎么样','觉得我怎么样'},priority=2)
@cmd31.handle()
async def cmd31_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\哇你好棒棒哦.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我不信.mp3
cmd32 = on_command('我不喜欢你了',aliases={'你不好看','你信不信','你不信','你信吗','你相信我','你相信我吗','你相信吗'},priority=2)
@cmd32.handle()
async def cmd32_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我不信.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#其实我也腼腆.mp3
cmd33 = on_command('我有点害羞',aliases={'我有点内向','我很内向','我很害羞','我是一个不善言辞的人','我是一个害羞的人','我是一个内向的人','我好害羞'},priority=2)
@cmd33.handle()
async def cmd33_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\其实我也腼腆.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你再这样我不理你了啊.mp3
cmd34 = on_command('跳个舞',aliases={'来跳个舞','一起洗澡吗','一起睡觉吗','一起洗澡','一起睡觉','跟你睡觉','跟你洗澡','帮我搓澡'},priority=2)
@cmd34.handle()
async def cmd34_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你再这样我不理你了啊.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你以后要只对我一个人好.mp3
cmd35 = on_command('我喜欢你',aliases={'我稀饭你','我爱你','你爱我吗','你喜欢我吗'},priority=2)
@cmd35.handle()
async def cmd35_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你以后要只对我一个人好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#别老色迷迷的好不好.mp3
cmd36 = on_command('欸嘿嘿',aliases={'嘿嘿','嘿嘿嘿','嘿嘿嘿嘿','嘿嘿嘿嘿嘿','嘿嘿嘿嘿嘿嘿','嘿嘿嘿嘿嘿嘿嘿','嘿嘿嘿嘿嘿嘿嘿嘿','嘿嘿嘿嘿嘿嘿嘿嘿嘿','嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿'},priority=2)
@cmd36.handle()
async def cmd36_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\别老色迷迷的好不好.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我刚刚刷抖音.mp3
cmd37 = on_command('你刚才在干什么',aliases={'你刚刚在干什么','你刚刚在干嘛','你怎么回事','你咋回事','你怎么回事？','你咋回事？','你在干嘛','你在干嘛呢','你在干吗','你在干吗呢'},priority=2)
@cmd37.handle()
async def cmd37_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我刚刚刷抖音.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#要亲亲抱抱举高高.mp3
cmd38 = on_command('要举高高吗',aliases={'要亲亲吗','要抱抱吗'},priority=2)
@cmd38.handle()
async def cmd38_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\要亲亲抱抱举高高.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#只有我一个人的呢.mp3
cmd39 = on_command('你一个人在家吗',aliases={'你一个人在家嘛','你爸妈在家吗','你家里有人吗','就你自己吗','你一个人吗','你自己吗','就你一个人吗'},priority=2)
@cmd39.handle()
async def cmd39_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\只有我一个人的呢.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#在的呢。小哥哥。.mp3
cmd40 = on_command('在吗',aliases={'在嘛','在么'},priority=2)
@cmd40.handle()
async def cmd40_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\在的呢。小哥哥。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#没钱吃饭，你请我啊？.mp3
cmd41 = on_command('一起吃饭吗',aliases={'吃饭吗','吃饭','吃饭去','干饭','干饭了','干饭人'},priority=2)
@cmd41.handle()
async def cmd41_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\没钱吃饭，你请我啊？.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#主人，您在用我吗.mp3
cmd42 = on_command('召唤kaptree',aliases={'出来挨打','妹妹','妹子','小美人'},priority=2)
@cmd42.handle()
async def cmd42_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\主人，您在用我吗.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#先说好 我不露脸.mp3
cmd43 = on_command('直播吗',aliases={'裸聊吗','视频吗','开视频吗','来视频吗','裸聊','视频','开视频','来视频','想吃你下面','想吃你下的面','想吃你下的面条'},priority=2)
@cmd43.handle()
async def cmd43_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\先说好 我不露脸.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你叫我不生气我就不生气啊 那多没面子。.mp3
cmd44 = on_command('别生气了',aliases={'生啥气吗','就知道生气','生气干嘛','生什么气','你还生气了','你倒生气了'},priority=2)
@cmd44.handle()
async def cmd44_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你叫我不生气我就不生气啊 那多没面子。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#为什么想骂我，小心我拉黑你.mp3
cmd45 = on_command('我想骂你',priority=2)
@cmd45.handle()
async def cmd45_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\为什么想骂我，小心我拉黑你.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#我不是懒猪，我是世界上最勤快的小仙女。.mp3
cmd46 = on_command('小懒猪',aliases={'你好懒','你真懒','你懒的很','你怎么那么懒','你太懒了','你懒到家了'},priority=2)
@cmd46.handle()
async def cmd46_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\我不是懒猪，我是世界上最勤快的小仙女。.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )


#以后你不要叫我宝贝，你要叫我爸爸.mp3
cmd47= on_command('宝贝',aliases={'叫爸爸','宝贝儿','baby','honey','亲爱的'},priority=2)
@cmd47.handle()
async def cmd47_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\以后你不要叫我宝贝，你要叫我爸爸.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#不原谅.mp3
cmd48 = on_command('你原谅我了吗',aliases={'原谅我','能原谅我吗','不能原谅我吗','会原谅我吗','会原谅我的吧'},priority=2)
@cmd48.handle()
async def cmd48_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\不原谅.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#今晚有事,改天吧.mp3
cmd49 = on_command('今晚约吗',aliases={'今晚吃个饭','今晚一起吃饭','今晚怎么样','今晚行吗','今晚好吗','今晚？','今晚吧'},priority=2)
@cmd49.handle()
async def cmd49_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\今晚有事,改天吧.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )

#你个大叔，怎么那么坏，老是要看这看那的.mp3
cmd50 = on_command('我想看看',aliases={'看看照片','爆照','发裸照','发张裸照'},priority=2)
@cmd50.handle()
async def cmd50_(bot:Bot,event:Event):
    if event.get_user_id != event.self_id:
        path_=os.getcwd()
        path_=path_+'\yuyinbao\你个大叔，怎么那么坏，老是要看这看那的.mp3'
        mypath='file:///'+path_
        print(mypath)
        sst = MessageSegment.record(file=str(mypath))
        await bot.send(
            event=event,
            message=Message(sst)
        )
