# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/18 下午8:25
"""
from config.config import Config


class DevConfig(Config):
    """
    DevConfig
    """
    DEBUG = True
    KEEP_ALIVE_TIMEOUT = 5
    WEBSOCKET_MAX_SIZE = 3 ** 20
