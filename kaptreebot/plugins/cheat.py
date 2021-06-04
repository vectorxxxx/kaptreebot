import json
import requests
import urllib
import urllib.parse
import urllib.request
import random
from nonebot import on_message,on_command
from nonebot.adapters.cqhttp import Bot, Event, Message, PRIVATE

def get_n(text):
    if text.find('小知酱') != -1 :
        return get_n0(text)
    if text.find('小灵酱') != -1 :
        return get_n1(text)
    if text.find('小思酱') != -1 :
        return get_n2(text)
    num = random.randint(0,2)
    if num == 0 :
        return get_n0(text)
    if num == 1 :
        return get_n1(text)
    if num == 2 :
        return get_n2(text)  

    
# 认知机器人
ren_zhi_url = 'http://www.weilaitec.com/cigirlrobot.cgr'
ren_zhi_appid = '1622741989812'
ren_zhi_appkey = 'HFQ25DXLHBFZKFAHU3GLX398Q2N0N4BQFDUWYZ59ZTZ8K16K6J'
ren_zhi_ip = "119.25.36.48vec"
ren_zhi_userid = "VectorX"

def get_n0(text):
    try:
        # 定义请求数据，并且对数据进行赋值
        values={}
        values['key']= ren_zhi_appkey
        values['msg']= text.encode('utf-8')
        values['ip']= ren_zhi_ip
        values['userid']= ren_zhi_userid
        values['appid']= ren_zhi_appid
        # 对请求数据进行编码
        data = urllib.parse.urlencode(values)
        # 将数据与url进行拼接
        req = ren_zhi_url + '?' + data
        r = requests.post(req)
        # 中文编码格式打印数据
        result = r.content.decode('utf-8')
        if result == '亲爱的用户您好。您当天的授权用量已用完(或未升级成会员)，请到平台升级会员，或者等明天可继续使用机器人大脑。有任何疑问，请您登陆官网联系客服服务。www.weilaitec.com。' :
            return get_n1(text)
        print('小知酱：' + result)    
        return result
    except TypeError:
        return '完了完了，突然好难受啊，小知感觉整个人都不好了~~'
        

#图灵机器人
def get_n1(text_input:str):
    try:
        api_url = "http://openapi.tuling123.com/openapi/api/v2"
        req = {
            "reqType": 0,  # 输入类型 0-文本, 1-图片, 2-音频
            "perception":  # 信息参数
            {
                "inputText":  # 文本信息
                {
                    "text": text_input
                },

                "selfInfo":  # 用户参数
                {
                    "location":
                    {
                        "city": "苏州",  # 所在城市
                        "province": "江苏",  # 省份
                        "street": "香山"  # 街道
                    }
                }
            },
            "userInfo":
            {
                "apiKey": "285364d8c0844621ac183ac615e36bd5",  # 改为自己申请的key
                "userId": "0001"  # 用户唯一标识(随便填, 非密钥)
            }
        }
        # 将字典格式的req编码为utf8
        req = json.dumps(req).encode('utf8')
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        response_dic = json.loads(response_str)
        intent_code = response_dic['intent']['code']
        results_text = response_dic['results'][0]['values']['text']
        if str(results_text) == '请求次数超限制!':
            return get_n2(text_input)
        print('小灵酱：', results_text)    
        return str(results_text)
    except KeyError:
        if KeyError == '4003':
            return '今天的智能对话次数用完了呢QAQ,请输入help查看其他玩法叭'
        else:
            return '来大姨妈了，不想理你~'

# 小思机器人
si_zhi_url = 'https://api.ownthink.com/bot'
appid = 'c8278e2921b4bc31f8974ad58dec13ba'

def get_n2(text):
    try:
        data = {
            "spoken": text,
            "appid": appid,
            "userid": "HRPVyRSl"
        }
        r = requests.post(si_zhi_url, data=json.dumps(data))
        result = json.loads(r.content)
        message = result['data']['info']['text']
        if 'heuristic' in result['data']['info'] and result['data']['info']['heuristic']:
            for item in result['data']['info']['heuristic']:
                message += ',  ' + item
        print('小思：', message)
        return message
    except KeyError:
        return '这个问题好头疼呀，问点别的叭'
    except BaseException:
        return '呸！渣男~'

tuling = on_message(priority=5) # permission= PRIVATE
@tuling.handle()
async def cheatt_(bot:Bot,event:Event):
    if event.is_tome():
        print("YES")
    if event.is_tome() and event.user_id!=event.self_id:
        mysay = event.get_message()
        mysay = get_n(str(mysay))
        await bot.send(
            event=event,
            message=mysay
        )

