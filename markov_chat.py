import sys,os
from markov import Markov
import tornado.httpserver
import tornado.ioloop
import tornado.web

import logging
import urllib, urllib2


markovchain = Markov()
command = '/markov'
training_text = 'chat.log'
webhook_url = 'http://partychat-hooks.appspot.com/post/p_zjrhnzm1'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        chattiness = self.get_augument('chattiness',1)
        names = markovchain.generate_simple_sentence()
        self.write(names)
    def post(self):
        message_body = self.get_argument('body')
        message_parts = message_body.split("] ")
        user = message_parts[0].replace("[",'')
        message = message_parts[1]
        if command in message:
            #chattiness = self.get_augument('chattiness',1)
            sentence = markovchain.generate_simple_sentence()
            print sentence
            values = {'message' :sentence }
            data = urllib.urlencode(values)
            req = urllib2.Request(webhook_url+"?message="+str(urllib.quote(sentence)))
            response = urllib2.urlopen(req)
            print response
            response.close()

        else:
            training_file.write(message+"\n")
            markovchain.load_brain(message)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    training_file = open(training_text, 'r+')
    print "Loading "+training_text+" into brain."
    markovchain.load_brain(training_file)
    print training_file
    print 'Brain Reloaded'
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

