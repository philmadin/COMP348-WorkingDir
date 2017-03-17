__author__ = '41511905'
import ohsumed, nltk, collections, pickle
print(len(ohsumed.index))
print(list(ohsumed.index.keys())[:10])
print(ohsumed.index['87073365'])
print(len(ohsumed.questions))
#print(list(ohsumed.questions.keys())[:10])
#print(ohsumed.questions['OHSU7'])

"""stop = nltk.corpus.stopwords.words('english')
wordcounter = collections.Counter([w.lower() for k in ohsumed.index
                                             for s in nltk.sent_tokenize(ohsumed.index[k])
                                             for w in nltk.word_tokenize(s)])
print(wordcounter.most_common(10))
inverted = dict()
for d in ohsumed.index:
    for w in nltk.word_tokenize(ohsumed.index[d]):
        w = w.lower()
        if w in stop or wordcounter[w] <= 5:
            continue
        if w in inverted:
            inverted[w].add(d)
        else:
            inverted[w] = set([d])
print(sorted(list(inverted.keys()))[3000:3010])
print(inverted['acceptability'])
with open('inverted.pickle','wb') as f:
    pickle.dump(inverted,f)"""
"""with open('inverted.pickle','rb') as f:
    inverted = pickle.load(f)
print((inverted['menopausal'] | inverted['pregnant']) & inverted['woman'] - inverted['healthy'])"""



