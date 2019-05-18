# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/18 下午8:24
"""
import os


class Config:
    """
    Config
    REQUEST_MAX_SIZE	100000000	请求数据的最大值 (bytes)
    REQUEST_BUFFER_QUEUE_SIZE	100	流缓存队列的大小
    REQUEST_TIMEOUT	60	请求超时时间 (sec)
    RESPONSE_TIMEOUT	60	响应超时时间 (sec)
    KEEP_ALIVE	True	是否保持长链接
    KEEP_ALIVE_TIMEOUT	5	保持TCP链接的时间 (sec)
    GRACEFUL_SHUTDOWN_TIMEOUT	15.0	等待强制关闭非空闲链接的时间 (sec)
    ACCESS_LOG	True	是否启用访问日志
    """
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    VIDEO_DIR = '{}/video'.format(BASE_DIR)
    HOST = '0.0.0.0'


    if os.path.exists(VIDEO_DIR):
        pass
    else:
        os.makedirs(VIDEO_DIR)
