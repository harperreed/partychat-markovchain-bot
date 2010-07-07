import sys,os
from markov import Markov
import tornado.httpserver
import tornado.ioloop
import tornado.web

import logging


markovchain = Markov()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        names = markovchain.generate_simple_sentence()
        self.write(names)
    def post(self):
        message_body = self.get_argument('body')
        self.write(message_body)
        message_parts = message_body.split("] ")
        user = message_parts[0].replace("[",'')
        message = message_parts[1]
        training_file.write(message+"\n")
        markovchain.load_brain(message)
        
        print message_parts
        print user
        print message

        pass

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    training_text = 'chat.log'
    training_file = open(training_text, 'r+')
    print "Loading "+training_text+" into brain."
    markovchain.load_brain(training_file)
    print training_file
    print 'Brain Reloaded'
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

