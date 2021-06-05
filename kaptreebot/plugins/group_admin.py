from nonebot import on_notice
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.event import GroupIncreaseNoticeEvent,GroupUploadNoticeEvent,GroupDecreaseNoticeEvent,GroupRequestEvent

# 将函数注册为群成员增加通知处理器

# 入群提醒
increase = on_notice()
@increase.handle()
async def increase(bot: Bot, event: GroupIncreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = event.operator_id + '哇~是新的rbq！'
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )


# 退群提醒
decrease = on_notice()
@decrease.handle()
async def decrease(bot: Bot, event: GroupDecreaseNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = event.operator_id + '离开了，好难过~'
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )

# 上传提醒
upload = on_notice()
@upload.handle()
async def upload(bot: Bot, event: GroupUploadNoticeEvent):
    if event.get_user_id != event.self_id:
        msg = '有人上传了：' + event.file.name + '好像打开看看呢~',
        await bot.send(
            event=event,
            message=msg,
            at_sender=True
        )
