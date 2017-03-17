"""import nltk
import collections
complete= nltk.corpus.gutenberg.words()
#Find the words with length of at least 7 characters in the complete Gutenberg corpus.
collCom = collections.Counter(complete)
temp = []
for w in collCom:
    if(len(w)>=7):
        temp.append(w)
print(list(temp[:10]))
"""

#Week 2
#import nltk, re
#nltk.download('brown')
#tagged = nltk.corpus.brown.tagged_words(categories='news')
#print(tagged[:500])
#tokens = [w for (w,t) in tagged]
#print(tokens[:5])
# 3.1 Write code that finds all the numbers (items tagged with 'CD') from the list tagged and stores them in a new variable numbers.
# How many numbers are there? How many different numbers are there?
#temp = [w for w in tagged]
#temp=[]
#temp=[w for(w,t) in tagged if t=='CD']
#temp=re.findall('RE',tagged)
#for one,tag in tagged:
#    if(tag=="CD"):
#        temp.append(tag)
    #if(re.search('CD',str(tag))):
    #    temp.append(tag)
#print(len(temp))
#print(len(set(temp)))

# 3.2 Find all the items in tokens that match the following regular expression: ^[0-9]+$. Write the result as a list of pairs
# (word,annotation) so that, if the word is a number, the annotation is 'CD', and if it is not a number, the annotation is ''.
"""
def annotateNum(listoftokens):
    pattern = re.compile('^[0-9]+$')
    result=[]
    for w in listoftokens:
        if pattern.match(str(w[0])):
            print("ADDED")
            result.append((w[0],'CD'))
        else:
            result.append((w[0],''))
    return result"""
#nltk.download('brown')
#tokens = [w for (w,t) in tagged]
#temp=[]
#print(tagged[:40])
#temp=[w for(w) in tagged if re.search(r'[0-9]+$',w[0])]
#print(annotateNum(tagged)[:500])



#Week 3
"""import ohsumed
print(len(ohsumed.index))
print(list(ohsumed.index.keys())[:10])
print(ohsumed.index['87073365'])
print(len(ohsumed.questions))
print(list(ohsumed.questions.keys())[:10])
print(ohsumed.questions['OHSU7'])"""
