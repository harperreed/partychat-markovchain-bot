import sys,os
from markov import Markov
import tornado.httpserver
import tornado.ioloop
import tornado.web


markovchain = Markov()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        names = markovchain.generate_simple_sentence(number_names)
        n = "<br />".join(names)
        self.write(n)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    #Usage: python baby_chains.py <length>
    if len(sys.argv) == 2:
        number_names = int(sys.argv[1])
    else:
        number_names = 30

    training_text = 'names.lst'
    f = open(training_text, 'r')
    print "Loading "+training_text+" into brain."
    markovchain.load_brain(f)
    print 'Brain Reloaded'
    f.close()
    print "Outputting " + str(number_names) + " generated names"
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

