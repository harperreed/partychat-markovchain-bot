import random

class Markov():

    markovtable = {} #defaultdict(list)
    reverse_markovtable = {}
    stopword = "\n"
    w1 = stopword
    w2 = stopword

    stopsentence = (".", "!", "?","\n",) # Cause a "new sentence" if found at the end of a word
    sentencesep  = "\n" #String used to seperate sentences

    def load_brain(self, text):
        for line in text:
            self.add_to_brain(line)
        # Mark the end of the file
        self.markovtable.setdefault( (self.w1, self.w2), [] ).append(self.stopword)        

    def load_brain2(self, text):
        for line in text:
            for word in line.split():
                if word[-1] in self.stopsentence:
                    self.markovtable.setdefault( (self.w1, self.w2), [] ).append(word[0:-1])
                    self.w1, self.w2 = self.w2, word[0:-1]
                    word = word[-1]
                self.markovtable.setdefault( (self.w1, self.w2), [] ).append(word)
                self.reverse_markovtable.setdefault( word, [] ).append((self.w1, self.w2))
                self.w1, self.w2 = self.w2, word
        # Mark the end of the file
        self.markovtable.setdefault( (self.w1, self.w2), [] ).append(self.stopword)        

    def add_to_brain(self, line):
        for word in line.split():
                if word[-1] in self.stopsentence:
                    self.markovtable.setdefault( (self.w1, self.w2), [] ).append(word[0:-1])
                    self.w1, self.w2 = self.w2, word[0:-1]
                    word = word[-1]
                self.markovtable.setdefault( (self.w1, self.w2), [] ).append(word)
                self.reverse_markovtable.setdefault( word, [] ).append((self.w1, self.w2))
                self.w1, self.w2 = self.w2, word


    def generate_simple_sentence(self):
        maxsentences= 10
        sentencecount = 0 
        sentence = []
        self.w1 = self.stopword
        self.w2 = self.stopword
        while sentencecount < maxsentences:
            newword = random.choice(self.markovtable[(self.w1, self.w2)])
	    if self.w1 == "\n" and self.w2 == "\n":
            	self.w1, self.w2 = self.w2, newword
           	newword = random.choice(self.markovtable[(self.w1, self.w2)])
            if newword == self.stopword: return 
            if newword in self.stopsentence:
                final_sentence = "%s%s" % (" ".join(sentence), newword)
                sentence = []
                sentencecount += 1
            else:
                sentence.append(newword)
            self.w1, self.w2 = self.w2, newword
        return final_sentence

    def generate_sentence(self, msg='', chain_length=2, max_words=10000):
        if msg == '':
            buf = []
            try:
                word = (random.choice(self.markovtable[random.choice(self.markovtable.keys())]))
                chain = random.choice(self.reverse_markovtable[word])
            except:
                return None
            buf.append(chain[0])
            buf.append(chain[1])
        else:
            #buf = msg.split().reverse()[:chain_length]
            buf = msg.split()[:chain_length]
            
        message = buf[:]
                
        for i in xrange(max_words):
            try:
                next_word = random.choice(self.markovtable[tuple(buf)])
            except IndexError:
                continue
            if next_word in self.stopsentence:
                break
            message.append(next_word)
            del buf[0]
            buf.append(next_word)
        return ' '.join(message)

