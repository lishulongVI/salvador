# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2019/5/18 下午4:21
"""
import random
import os
import asyncio
import datetime
from sanic import Sanic
from sanic import Blueprint
from sanic import response
from sanic.exceptions import NotFound

from sanic.response import json, text

from config import CONFIG

# strict_slashes trip 调最后的/
from sanic_.services.middleware import bp_middle
from sanic_.services.ws import wc, ws_index

app = Sanic('name', strict_slashes=True)
app.config.from_object(CONFIG)


@app.route('/')
async def index(request):
    return json(
        body={
            'args': request.args,
            'query': request.query_string,
            'raw_args': request.raw_args,  # deprecated
            'query_args': request.query_args,
            'cookies': request.cookies,
            'ip': request.ip,
        }, status=200,
        content_type='application/json'
    )


@app.route('/json', methods=['POST'])
async def json_(request):
    return json({'received': request.json()})


@app.route('/upload', strict_slashes=False)
async def upload(request):
    html = ('<html><body align="center">'
            '<form action="/files" method="post" enctype="multipart/form-data">'
            '<input type="file" name="file1" /> <br />'
            '<input type="file" name="file2" /> <br />'
            '<input type="submit" value="Upload" />'
            '</form>'
            '</body></html>')
    return response.html(html)


@app.route('/files', methods=['POST'])
async def file(request):
    files = request.files
    names = files.keys()
    for i in names:
        b = files.get(i)
        if not b.body:
            continue
        path = '{}/{}'.format(app.config.VIDEO_DIR, b.name)
        with open(path, 'wb') as fl:
            fl.write(b.body)
    return json(
        body={
            'file_len': [len(request.files.get(f).body) for f in request.files],
            'file_name': [request.files.get(f).name for f in request.files]
        }
    )


@app.route('/look')
async def look_file(request):
    ls = os.listdir(app.config.VIDEO_DIR)
    return await response.file(location='{}/{}'.format(app.config.VIDEO_DIR, ls[random.randrange(len(ls))]))


@app.route('/redirect')
async def redirect(request):
    """
    Sanic 返回一个重定向URL让浏览器去访问。它是通过在响应头headers里面设置 Location 来实现的。
    :param request:
    :return:
    """
    return response.redirect('http://www.baidu.com')


@app.route('/steam')
async def streaming(request):
    """
    返回流数据给浏览器。流数据的意思就是，不是一次性把所有数据返回，而是一部分一部分地返回。
    :param request:
    :return:
    """

    async def streaming_fn(response):
        await response.write('date :{} \n'.format(datetime.datetime.now()))
        await asyncio.sleep(5)
        await response.write('date :{} \n'.format(datetime.datetime.now()))

    return response.stream(streaming_fn=streaming_fn)


@app.route('/file_stream')
async def file_stream(request):
    """
    适合文件非mp4的
    :param request:
    :return:
    """
    ls = os.listdir(app.config.VIDEO_DIR)
    return await response.file_stream(location='{}/{}'.format(app.config.VIDEO_DIR, ls[random.randrange(len(ls))]),
                                      chunk_size=4096)


@app.get('/cid/<cid:int>')
async def args(request, cid):
    return json(body={'cid1': cid, 'args': request.args})


# @app.get('/cid/<cid:int>', host='config.media.interet.com')
# async def args(request, cid):
#     return json(body={'cid2': cid})


async def favicon(request):
    return await response.file('{}/favicon.ico'.format(app.config.BASE_DIR))


@app.get('/index')
async def index_url_for(request):
    # 不支持method
    url = app.url_for('args', cid=3,
                      args=request.args, _anchor='anchor', _scheme='http', _external=True,
                      _server='config.media.interet.com:8000')
    return response.redirect(url)


app.add_websocket_route(wc, uri='/wc')

app.add_route(handler=favicon, uri='/favicon.ico', methods=['GET'])

index_bp = Blueprint('index_bp', strict_slashes=False, url_prefix='/heheda', version=1)

# http://127.0.0.1:8000/heheda/static/image.jpg
# http://127.0.0.1:8000/heheda/static/%E8%90%8D%E5%A7%90-95984272643--44.mp4
# index_bp.static('/static', './video', stream_large_files=True)
# 当stream_large_files为True时，Sanic将会使用file_stream()替代file()来提供静态文件访问。它默认的块大小是1KB，当然你可以根据需要修改块大小
chunk_size = 1024 * 1024 * 8  # 8kb
index_bp.static('/static', './video', stream_large_files=chunk_size)
index_bp.static('/template', './sanic_/template', stream_large_files=chunk_size)


@index_bp.get('/bp/get', version=1)
async def index_bb(request):
    """
     http://127.0.0.1:8000/v1/heheda/bp/get/
    :param request:
    :return:
    """
    return json({'c1': request.args})


@index_bp.get('/bp/get', version=2)
async def index_bb(request):
    """
    http://127.0.0.1:8000/v2/heheda/bp/get/
    :param request:
    :return:
    """
    return json({'c2': request.args})


app.blueprint(index_bp)

app.blueprint(bp_middle)


# 一个后台任务在事件循环开始后执行，Sanic提供了add_task方法轻松实现。
async def notify_task(app):
    await asyncio.sleep(4)
    print('server success:', datetime.datetime.now())


app.add_task(notify_task)

app.add_route(ws_index, uri='/heheda/ws')


@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))
