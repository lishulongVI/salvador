# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/19 上午1:37
"""
from sanic import response
from sanic.views import HTTPMethodView


class IndexView(HTTPMethodView):
    @staticmethod
    async def get(request):
        return response.json({'status': 'ok', 'method': request.method})

    @staticmethod
    async def post(request):
        return response.json({'status': 'ok', 'method': request.method})
