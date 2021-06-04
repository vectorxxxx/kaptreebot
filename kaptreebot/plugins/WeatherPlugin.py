import urllib.request
import gzip
import json
import re
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event



weather = on_command("天气", priority=2)
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if args:
            state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马城市的天气(@_@)...")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname) # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    weather_data = urllib.request.urlopen(url).read() # 发出请求并读取到weather_data
    weather_data = gzip.decompress(weather_data).decode('utf-8') # 以utf-8的编码方式解压数据
    weather_dict = json.loads(weather_data) # 将json数据转化为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        return f"这个地方人家没去过呢，要不你带我去一次叭♥~"
    elif weather_dict.get('desc') =='OK' :
        forecast = weather_dict.get('data').get('forecast')
        fengli = forecast[0].get('fengli')
        rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
        match = rgx.search(fengli)
        print(match.group(1))
        startoday = '城市：'+weather_dict.get('data').get('city') +'\n' \
                  +'日期：'+forecast[0].get('date') + '\n'\
                  +'温度：'+weather_dict.get('data').get('wendu') + '℃\n' \
                  +'高温：'+forecast[0].get('high') + '\n' \
                  +'低温: '+forecast[0].get('low') + '\n' \
                  +'风向：'+forecast[0].get('fengxiang') +'\n'\
                  +'风力：'+match.group(1) + '\n'\
                  +'天气：'+forecast[0].get('type') + '\n'\
                  +'感冒：'+weather_dict.get('data').get('ganmao') + '\n'
        return startoday
