# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/18 下午8:23
"""
import os


def load_conf():
    mode = os.environ.get('MODE', 'DEV')

    if mode == 'DEV':
        from .dev import DevConfig
        return DevConfig
    elif mode == 'PRO':
        from .prod import ProConfig
        return ProConfig
    else:
        from .dev import DevConfig
        return DevConfig


CONFIG = load_conf()

