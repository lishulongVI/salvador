# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/19 上午12:02
"""
from .app import app


@app.middleware('request')
async def rewrite_request(request):
    print('rewrite_request accept request')


@app.middleware('response')
async def rewrite_response(request, response):
    """
    Connection: keep-alive
    Content-Length: 17
    Content-Type: application/json
    Keep-Alive: 5
    server: sanic server
    :param request:
    :param response:
    :return:
    """
    response.headers['server'] = 'sanic server'
    print('rewrite_response accept response')


@app.listener('before_server_start')
async def before_server_start(app, loop):
    """
    before_server_start... ready
    server... success
    :param app:
    :param loop:
    :return:
    """
    print('before_server_start... ready')


@app.listener('after_server_start')
async def after_server_start(app, loop):
    """
    before_server_start... ready
    server... success
    :param app:
    :param loop:
    :return:
    """
    print('server... success')


@app.listener('before_server_stop')
async def before_server_stop(app, loop):
    """
    [2019-05-18 23:57:57 +0800] [18596] [INFO] Goin' Fast @ http://0.0.0.0:8000
    before_server_start... ready
    server... success
    [2019-05-18 23:57:57 +0800] [18598] [INFO] Starting worker [18598]
    [2019-05-18 23:58:11 +0800] [18598] [INFO] Stopping worker [18598]
    before_server_stop... ready
    after_server_stop... resource close
    [2019-05-18 23:58:11 +0800] [18598] [INFO] Server Stopped
    :param app:
    :param loop:
    :return:
    """
    print('before_server_stop... ready')


@app.listener('after_server_stop')
async def before_server_stop(app, loop):
    print('after_server_stop... resource close')
