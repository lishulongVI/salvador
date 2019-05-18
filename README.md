# salvador
sanic

<table>
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>不会js不会js</title>
</head>
<div class="single-content">  <p>Sanic作为一款应用比较广泛的异步web框架，已经形成了比较成熟的技术链，其周边的各种扩展应有尽有。</p>
<h2 id="_1">扩展和插件开发</h2>
<ul>
<li><a href="https://github.com/ashleysommer/sanicpluginsframework">Sanic-Plugins-Framework</a>：轻松创建和使用Sanic插件的库。</li>
<li><a href="https://github.com/tim2anna/sanic-script">sanic-script</a>：给应用程序添加编写命令支持的Sanic扩展。</li>
</ul>
<h2 id="_2">安全</h2>
<ul>
<li><a href="https://github.com/ahopkins/sanic-jwt">Sanic JWT</a>：身份认证，JWT和权限范围。</li>
<li><a href="https://github.com/cakinney/secure">Secure</a>：为Python web 框架添加可选的安全头和cookies的轻量级包。</li>
<li><a href="https://github.com/subyraman/sanic_session">Sessions</a>：对session的支持，允许使用redis，memcache或内存。</li>
<li><a href="https://github.com/ashleysommer/sanic-cors">CORS</a>：对flask-cors的移植。</li>
<li><a href="https://github.com/devArtoria/Sanic-JWT-Extended">Sanic-JWT-Extended</a>：提供对JWT的支持。</li>
<li><a href="https://github.com/lixxu/sanic-useragent">UserAgent</a>：给request添加<code>user_agent</code>。</li>
<li><a href="https://github.com/bohea/sanic-limiter">Limiter</a>：为sanic添加频率限制。</li>
<li><a href="https://gitlab.com/SirEdvin/sanic-oauth">sanic-oauth</a>：支持多家的OAuth1/OAuth2的OAuth库。</li>
<li><a href="https://github.com/pyx/sanic-auth">Sanic-Auth</a>：Sanic的一种最小后端不可知的以session为基础的用户身份验证机制。</li>
<li><a href="https://github.com/pyx/sanic-cookiesession">Sanic-CookieSession</a>：仅限客户端基于cookie的session，类似于Flask的内置session。</li>
</ul>
<h2 id="_3">文档</h2>
<ul>
<li><a href="https://github.com/channelcat/sanic-openapi">OpenAPI/Swagger</a>：支持OpenAPI及Swagger UI。</li>
<li><a href="https://github.com/ashleysommer/sanic-restplus">Sanic-RestPlus</a>：对Flask-RestPlus的移植。拥有SwaggerUI生成功能的全功能REST API。</li>
<li><a href="https://github.com/yunstanford/sanic-transmute">sanic-transmute</a>：从Python函数和类生成API，并自动生成Swagger UI或文档的Sanic扩展。</li>
</ul>
<h2 id="orm">ORM和数据库集成</h2>
<ul>
<li><a href="https://github.com/lixxu/sanic-motor">Motor</a>：对moter的简单包装。</li>
<li><a href="https://github.com/Typhon66/sanic_crud">Sanic CRUD</a>：使用peewee模型生成CRUD REST API。</li>
<li><a href="https://github.com/graphql-python/sanic-graphql">sanic-graphql</a>：GraphQL与Sanic的集成。</li>
<li><a href="https://github.com/fantix/gino">GINO</a>： 在SQLAIchemy核心之上的异步ORM。</li>
<li><a href="https://github.com/encode/databases">Databases</a>：SQLAIchemy核心的异步数据库访问，支持PostgreSQL，MySQL和SQLite。</li>
</ul>
<h2 id="_4">单元测试</h2>
<ul>
<li><a href="https://github.com/yunstanford/pytest-sanic">pytest-sanic</a>：Sanic的pytest插件，进行异步测试。</li>
</ul>
<h2 id="_5">项目创建模板</h2>
<ul>
<li><a href="https://github.com/harshanarayana/cookiecutter-sanic">cookiecutter-sanic</a>：在明确定义的项目结构中，可以在几秒钟内启动并运行sanic应用程序。包括用于部署，单元测试，自动发布管理和更改日志生成的电池。</li>
</ul>
<h2 id="_6">模板</h2>
<ul>
<li><a href="https://github.com/pyx/sanic-wtf">Sanic-WTF</a>：让Sanic使用WTForm和CSRF（跨站点请求伪造）保护更容易。</li>
<li><a href="https://github.com/lixxu/sanic-jinja2">Jinja2</a>：支持Jinja2模板。</li>
<li><a href="https://github.com/yunstanford/jinja2-sanic">jinja2-sanic</a>：Sanic的jinja2模板渲染器。</li>
</ul>
<h2 id="api-helper">API Helper实用程序</h2>
<ul>
<li><a href="https://github.com/inn0kenty/sanic_sse">sanic-sse</a>： Sanic的<code>Server-Sent Event</code>实现。</li>
<li><a href="https://github.com/subyraman/sanic_compress">Compress</a>：对Flask-Compress的移植，轻松实现对Sanic响应的gzip压缩。</li>
<li><a href="https://github.com/lixxu/python-paginate">Pagination</a>：简单的分页支持。</li>
<li><a href="https://github.com/jamesstidard/sanic-envconfig">Sanic EnvConfig</a>：将环境变量拉入sanic配置。</li>
</ul>
<h2 id="i18nl10n">i18n/l10n （国际化/本地化）支持</h2>
<ul>
<li><a href="https://github.com/lixxu/sanic-babel">Babel</a>：在<code>Babel</code>库的帮助下让Sanic应用支持国际化和本地化。</li>
</ul>
<h2 id="_7">自定义中间件</h2>
<ul>
<li><a href="https://github.com/ashleysommer/sanic-dispatcher">Dispatch</a>：受werkzeug的DispatcherMiddleware启发的调度器，可以充当Sanic-to-WSGI的适配器。</li>
</ul>
<h2 id="_8">监测和报告</h2>
<ul>
<li><a href="https://github.com/dkruchinin/sanic-prometheus">sanic-prometheus</a>：Sanic的Prometheus指标。</li>
<li><a href="https://github.com/kevinqqnj/sanic-zipkin">sanic-zipkin</a>：通过aiozipkin轻松向zipkin / jaeger报告请求/功能/ RPC跟踪。</li>
</ul>
<h2 id="_9">应用例子</h2>
<ul>
<li><a href="https://github.com/itielshwartz/sanic-nginx-docker-example">Sanic-nginx-docker-example</a>：使用docker-compose简单易用的Sanic behined nginx示例。</li>
</ul> </div>
</table>