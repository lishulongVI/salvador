# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/19 上午1:37
"""
from sanic import response
from sanic.response import text
from sanic.views import HTTPMethodView, stream


class IndexView(HTTPMethodView):
    @staticmethod
    async def get(request):
        return response.json({'status': 'ok', 'method': request.method})

    @staticmethod
    async def post(request):
        return response.json({'status': 'ok', 'method': request.method})


class SimpleView(HTTPMethodView):
    @stream
    async def post(self, request):
        result = ''
        while True:
            body = await request.stream.read()
            if body is None:
                break
            result += body.decode('utf-8')
        return text(result)
