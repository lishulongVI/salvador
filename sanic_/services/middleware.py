# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/18 下午11:37
"""
from sanic import Blueprint
from sanic import response

bp_middle = Blueprint(name='bp_middle', url_prefix='/middle', version=1)


@bp_middle.get('/index')
async def middle_(request):
    """
    rewrite_request accept request
    middle_
    rewrite_response accept response
    :param request:
    :return:
    """
    print('middle_')
    return response.json(body={
        'content': request.query_string
    })
