# coding: utf-8
import tornado.web
import tornado.websocket
import tornado.ioloop
from tornado.options import define, options, parse_command_line

define("port", default = 3000, help = "run on the given port", type = int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('index.htm')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def on_message(self, msg):
        print(msg)
        self.write_message('You said: {}'.format(msg))


app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
