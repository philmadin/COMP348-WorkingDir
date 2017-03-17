__author__ = '41511905'
import nltk, collections, pickle
"""gutenberg=dict()
for d in nltk.corpus.gutenberg.fileids():
    words=nltk.corpus.gutenberg.words(d)
    for w in words:
        if w in gutenberg:
            gutenberg[w].add(d)
        else:
            gutenberg[w]=set([d])
with open('gutenbergindex.pickle','wb') as f:
    pickle.dump(gutenberg,f)"""

with open('gutenbergindex.pickle','rb') as f:
    gutenberg=pickle.load(f)
print (gutenberg['Brutus']-gutenberg['Caesar'])


"""stop = nltk.corpus.stopwords.words('english')
wordcounter = collections.Counter([w.lower() for k in nltk.corpus.gutenberg.fileids()
                                             for s in nltk.sent_tokenize(nltk.corpus.gutenberg.raw(k))
                                             for w in nltk.word_tokenize(s)])
with open('gutenbergindex.pickle','wb') as f:
    pickle.dump(wordcounter,f)"""

"""with open('gutenbergindex.pickle','rb') as f:
    words = pickle.load(f)
print(words.most_common(10))"""