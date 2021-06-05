import urllib.request
import gzip
import json
import re
from nonebot import on_command
from nonebot.rule import to_me,on_natural_language, NLPSession, IntentCommand
from nonebot.adapters.cqhttp import Bot, Event
from jieba import posseg

weather = on_command("天气", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想知道哪座城市的天气状况呢\(≧▽≦)/")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + \
        urllib.parse.quote(
            cityname)  # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    weather_data = urllib.request.urlopen(url).read()  # 发出请求并读取到weather_data
    weather_data = gzip.decompress(
        weather_data).decode('utf-8')  # 以utf-8的编码方式解压数据
    weather_dict = json.loads(weather_data)  # 将json数据转化为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        return f"这个地方人家没去过呢，要不你带我去一次叭♥~"
    elif weather_dict.get('desc') == 'OK':
        forecast = weather_dict.get('data').get('forecast')
        fengli = forecast[0].get('fengli')
        rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
        match = rgx.search(fengli)
        startoday = '城市：'+weather_dict.get('data').get('city') + '\n' \
            + '日期：'+forecast[0].get('date') + '\n'\
            + '温度：'+weather_dict.get('data').get('wendu') + '℃\n' \
            + '高温：'+forecast[0].get('high') + '\n' \
            + '低温: '+forecast[0].get('low') + '\n' \
            + '风向：'+forecast[0].get('fengxiang') + '\n'\
            + '风力：'+match.group(1) + '\n'\
            + '天气：'+forecast[0].get('type') + '\n'\
            + '感冒：'+weather_dict.get('data').get('ganmao') + '\n'
        return startoday

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    city = None
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'ns':
            # ns 词性表示地名
            city = word.word
            break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'weather', current_arg=city or '')