#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
from nonebot.log import default_format, logger
from os import path
# Custom your logger
#
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)


nonebot.load_builtin_plugins()
# nonebot.load_plugin("nonebot_plugin_withdraw")
nonebot.load_plugin("nonebot_plugin_apscheduler")  # 加上此行代码
nonebot.load_plugin('nonebot_plugin_picsearcher')
nonebot.load_plugins("kaptreebot/plugins")

# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...

logger.add(path.join('log', "error.log"),
           rotation="00:00",
           retention='1 week',
           diagnose=False,
           level="ERROR",
           format=default_format,
           encoding='utf-8'
           )

if __name__ == "__main__":
    nonebot.run(app="bot:app")
