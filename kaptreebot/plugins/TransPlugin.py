from urllib import request,parse
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import json
import http.client
import hashlib
import urllib
import random


trans = on_command("翻译", priority=2)
@trans.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    if event.get_user_id != event.self_id:
        args = str(event.message).strip()  # 首次发送命令时跟随的参数
        if args:
            state["trans"] = args  # 如果用户发送了参数则直接赋值


@trans.got("trans", prompt="你想翻译什么呢...")
async def handle_trans(bot: Bot, event: Event, state: dict):
    text = state["trans"]
    text_trans = await get_baidufanyi(text)
    await trans.finish(text_trans)


async def get_trans(trans: str):
    base_url = 'https://fanyi.baidu.com/sug'
    # 构建请求对象
    data = {
        'kw': trans
    }
    data = parse.urlencode(data)
    # 模拟浏览器
    header = {"User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    req = request.Request(url=base_url,data=bytes(data,encoding='utf-8'),headers=header)
    res = request.urlopen(req)
    # 获取响应的json字符串
    str_json = res.read().decode('utf-8')
    # 把json转换成字典
    myjson = json.loads(str_json)
    try:
        transinfo = myjson['data'][0]['v']
    except Exception as e:
        return f"翻译错误：{e}"
    else:
        return f"{trans}的翻译内容：{transinfo}"

toLangs = ['wyw','yue','kor','en','jp']

async def get_baidufanyi(trans: str):
    appid = '20190417000288999'  # 填写你的appid
    secretKey = '0sOZGqbzw5agcdiAWlCZ'  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'   #原文语种
    toLang = toLangs[random.randint(0,len(toLangs)-1)]   #译文语种
    salt = random.randint(32768, 65536)
    q = trans
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print(result)
        c='翻译结果: '+result['trans_result'][0]['dst']
        print (c)
        return c
    except Exception as e:
        print (e)
        return '嗯~人家还来不了这个嘛！不要这样子说话啦，好讨厌！'
    finally:
        if httpClient:
            httpClient.close()
