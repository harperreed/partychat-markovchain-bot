import tornado.httpserver
import tornado.ioloop
import tornado.web

penis = 'harper'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world" + penis)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
