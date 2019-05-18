# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/19 上午12:02
"""
from sanic_ import app

if __name__ == '__main__':
    """
    # web server 
    # gunicorn server:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker
    """
    app.run(debug=app.config.DEBUG, host=app.config.HOST, workers=4)
