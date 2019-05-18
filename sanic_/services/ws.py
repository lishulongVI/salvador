# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/19 上午12:09
"""
import asyncio
import datetime
from sanic import response


async def ws_index(request):
    return response.redirect('template/websocket.html')


async def wc(request, ws):
    """
    wsUri = 'ws://127.0.0.1:8000/wc'
    websocket = new WebSocket(wsUri);
    websocket.onopen = function(evt) {
        console.log('open',evt)
    };
    websocket.onclose = function(evt) {
        console.log('onclose',evt)
    };
    websocket.onmessage = function(evt) {
        console.log('onmessage',evt.data)
    };
    websocket.onerror = function(evt) {
         console.log('onerror',evt)
    };

    websocket.send(new Date())
    websocket.send('over')
    :param request:
    :param ws:
    :return:
    """
    while True:
        await ws.send('{}'.format(datetime.datetime.now()))
        await asyncio.sleep(1)
        await ws.send('{}'.format(datetime.datetime.now()))
        data = await  ws.recv()
        if data == 'over':
            ws.close()
            return
        await ws.send(data)
