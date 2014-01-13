# This lemmatizer is based on the Princeton WordNet lemmatizer, however, it is better for that it can detect the
# most probable pos and returns its original form. For example, checks can be understood as both the variant of check
# which could be noun or verb. But the point is to get 'check', the original form. That's where LeeLemmatizer is the
# most useful. It doesn't care whether really checks here is a verb or the plural of a noun, it just returns the
# original form, which is check, whereas in Princeton WordNet, or other lemmatizer, they always require the input of
# pos, which makes the process, in most case, to have the necessity of human intervention.

'''ATTENTION: !!!for some reason, please use "from LeeLemmatizer import *!!!"'''

from nltk.stem.wordnet import WordNetLemmatizer


class LeeLemmatizer:

    # Class attributes
    pos_info = {}
    wordNetLemmatizer = WordNetLemmatizer()

    # def __hash__(self):
    #     return int.hash(n)
    # def __eq__(self, p):
    #     return self.n == p.n

    def __init__(self):
        pos_file = open('words_and_pos_simplified', 'r')

        # Loading the file
        print "LeeLemmatizer: loading file, this could take a while"

        for line in pos_file:
            word = line.split()[0]
            pos = line.split()[1]

            if word not in LeeLemmatizer.pos_info:  # Ignore low probability pos
                LeeLemmatizer.pos_info.update({word:pos})

        print "Loaded"

    def lemmatize(self, to_be_lemmatized):

        if to_be_lemmatized not in LeeLemmatizer.pos_info:
            pos = 'n'
        else:
            pos = LeeLemmatizer.pos_info[to_be_lemmatized]

        if pos == 'x':
            pos = 'n'

        result = LeeLemmatizer.wordNetLemmatizer.lemmatize(to_be_lemmatized, pos)

        print result

        return result