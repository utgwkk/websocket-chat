# coding: utf-8
import tornado.web
import tornado.ioloop
from tornado.options import define, options, parse_command_line

define("port", default = 3000, help = "run on the given port", type = int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('index.htm')

app = tornado.web.Application([
    (r"/", IndexHandler),
    ])

if __name__ == "__main__":
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
