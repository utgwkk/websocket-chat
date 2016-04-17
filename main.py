# coding: utf-8
import os
import time
import tornado.web
import tornado.websocket
import tornado.ioloop
from tornado.options import define, options, parse_command_line

define("port", default = os.environ.get('PORT', 3000), help = "run on the given port", type = int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render('index.htm')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    cons = set()

    def open(self):
        self.cons.add(self)

    def on_message(self, msg):
        self.write_message_for_all(u'{}: {}'.format(time.strftime("%y-%M-%d %H:%M:%S"), msg))

    def write_message_for_all(self, msg):
        for con in self.cons:
            con.write_message(msg)


    def on_close(self):
        self.cons.remove(self)


app = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/ws", WebSocketHandler),
    ])

if __name__ == "__main__":
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
