import sys,os
from markov import Markov
import tornado.httpserver
import tornado.ioloop
import tornado.web

import logging


markovchain = Markov()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        alias = self.get_argument('alias')
        names = markovchain.generate_simple_sentence(number_names)
        n = "<br />".join(names)
        logging.warning('asd')
        self.write(n)
    def post(self):
        message_body = self.get_argument('body')
        self.write(message_body)
        print message_body

        pass

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    training_text = 'names.lst'
    f = open(training_text, 'r')
    print "Loading "+training_text+" into brain."
    markovchain.load_brain(f)
    print 'Brain Reloaded'
    f.close()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

