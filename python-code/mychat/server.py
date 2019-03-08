
import pymysql
import redis
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import config,urls

from tornado.options import options


tornado.options.define('port',type=int,default=8080,help='服务器端口')


class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.db = pymysql.Connect(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    # options.log_file_prefix = config.log_path
    # options.logging = config.log_level
    tornado.options.parse_command_line()
    app = Application(
       urls.urlpatterns,
       **config.settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()